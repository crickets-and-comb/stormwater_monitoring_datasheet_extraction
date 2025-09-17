"""Test the load_datasheets module."""

# TODO: Test that returns correct path, using pytest.mark.parametrize.
import re
from contextlib import AbstractContextManager, nullcontext
from unittest.mock import patch

import pandas as pd
import pytest
from pydantic_core._pydantic_core import ValidationError

from stormwater_monitoring_datasheet_extraction.lib import load_datasheets
from stormwater_monitoring_datasheet_extraction.lib.constants import (
    Columns,
    CreekType,
    OutfallType,
)
from stormwater_monitoring_datasheet_extraction.lib.db.tables import CREEKS, SITES

# TODO: Test that returns correct path, using pytest.mark.parametrize.


@pytest.mark.parametrize(
    "site_type_map, creek_type_map, error_context",
    [
        (SITES, CREEKS, nullcontext()),
        # Creek.site_id not in Site.site_id.
        (
            pd.concat(
                [
                    SITES,
                    pd.DataFrame(
                        {
                            Columns.SITE_ID: ["Nonexistent Creek"],
                            Columns.OUTFALL_TYPE: [OutfallType.CREEK],
                            Columns.CREEK_SITE_ID: ["Nonexistent Creek"],
                        }
                    ).set_index(Columns.SITE_ID),
                ],
            ),
            CREEKS,
            pytest.raises(
                ValueError,
                match=re.escape(
                    "Creek site IDs in site_type_map not in creek_type_map: "
                    "['Nonexistent Creek']"
                ),
            ),
        ),
        # Site.creek_site_id not in Creek.site_id.
        (
            SITES,
            pd.concat(
                [
                    CREEKS,
                    pd.DataFrame(
                        {
                            Columns.SITE_ID: ["Nonexistent Site"],
                            Columns.CREEK_TYPE: [CreekType.SPAWN],
                        }
                    ).set_index(Columns.SITE_ID),
                ],
            ),
            pytest.raises(
                ValueError,
                match=re.escape(
                    "Creek site IDs in creek_type_map not found in site_type_map: "
                    "['Nonexistent Site']"
                ),
            ),
        ),
        # Site.creek_site_id not null for non-creek outfall type.
        (
            pd.concat(
                [
                    SITES,
                    pd.DataFrame(
                        {
                            Columns.SITE_ID: ["Non-Creek with Creek ID"],
                            Columns.OUTFALL_TYPE: [OutfallType.OUTFALL],
                            Columns.CREEK_SITE_ID: ["Non-Creek with Creek ID"],
                        }
                    ).set_index(Columns.SITE_ID),
                ],
            ),
            CREEKS,
            pytest.raises(
                ValidationError,
                match=(
                    "Value error, DataFrameSchema 'Site' failed element-wise validator "
                    "number 0: <Check creek_site_id_valid> failure cases: outfall, "
                    "Non-Creek with Creek ID"
                ),
            ),
        ),
        # Site.creek_site_id null for creek outfall type.
        (
            pd.concat(
                [
                    SITES,
                    pd.DataFrame(
                        {
                            Columns.SITE_ID: ["Creek without Creek ID"],
                            Columns.OUTFALL_TYPE: [OutfallType.CREEK],
                            Columns.CREEK_SITE_ID: [pd.NA],
                        }
                    ).set_index(Columns.SITE_ID),
                ],
            ),
            CREEKS,
            pytest.raises(
                ValidationError,
                match=(
                    "Value error, DataFrameSchema 'Site' failed element-wise validator "
                    "number 0: <Check creek_site_id_valid> failure cases: creek, nan"
                ),
            ),
        ),
        # Null Site.site_id.
        (
            pd.concat(
                [
                    SITES,
                    pd.DataFrame(
                        {
                            Columns.SITE_ID: [pd.NA],
                            Columns.OUTFALL_TYPE: [OutfallType.CREEK],
                            Columns.CREEK_SITE_ID: [pd.NA],
                        }
                    ).set_index(Columns.SITE_ID),
                ],
            ),
            CREEKS,
            pytest.raises(
                ValidationError,
                match="Value error, non-nullable series 'site_id' contains null values",
            ),
        ),
        # Null Creek.site_id.
        (
            SITES,
            pd.concat(
                [
                    CREEKS,
                    pd.DataFrame(
                        {
                            Columns.SITE_ID: [pd.NA],
                            Columns.CREEK_TYPE: [CreekType.SPAWN],
                        }
                    ).set_index(Columns.SITE_ID),
                ],
            ),
            pytest.raises(
                ValidationError,
                match="Value error, non-nullable series 'site_id' contains null values",
            ),
        ),
    ],
)
def test_get_site_creek_maps(
    site_type_map: pd.DataFrame,
    creek_type_map: pd.DataFrame,
    error_context: AbstractContextManager,
) -> None:
    """Tests that _get_site_creek_maps returns valid tables."""
    with error_context, patch(
        "stormwater_monitoring_datasheet_extraction.lib.db.read.get_site_type_map",
        return_value=site_type_map,
    ), patch(
        "stormwater_monitoring_datasheet_extraction.lib.db.read.get_creek_type_map",
        return_value=creek_type_map,
    ):
        maps = load_datasheets._get_site_creek_maps()
        assert maps == (site_type_map, creek_type_map)
