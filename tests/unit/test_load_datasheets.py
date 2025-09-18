"""Test the load_datasheets module."""

# TODO: Test that returns correct path, using pytest.mark.parametrize.
from collections.abc import Callable
from contextlib import AbstractContextManager
from unittest.mock import patch

import pandas as pd
import pytest
from tests.unit.conftest import site_creek_type_parametrize
from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib import load_datasheets
from stormwater_monitoring_datasheet_extraction.lib.constants import Columns

# TODO: Test that returns correct path, using pytest.mark.parametrize.


@site_creek_type_parametrize
@pytest.mark.parametrize(
    "fx, kwargs",
    [
        (load_datasheets._get_site_creek_maps, {}),
        (
            load_datasheets.verify,
            {
                "precleaned_form_metadata": pd.DataFrame(columns=[Columns.FORM_ID]).set_index(
                    Columns.FORM_ID
                ),
                "precleaned_investigators": pd.DataFrame(
                    columns=[Columns.FORM_ID, Columns.INVESTIGATOR]
                ).set_index([Columns.FORM_ID, Columns.INVESTIGATOR]),
                "precleaned_site_visits": pd.DataFrame(
                    columns=[Columns.FORM_ID, Columns.SITE_ID]
                ).set_index([Columns.FORM_ID, Columns.SITE_ID]),
                "precleaned_quantitative_observations": pd.DataFrame(
                    columns=[Columns.FORM_ID, Columns.SITE_ID]
                ).set_index([Columns.FORM_ID, Columns.SITE_ID]),
                "precleaned_qualitative_observations": pd.DataFrame(
                    columns=[Columns.FORM_ID, Columns.SITE_ID, Columns.OBSERVATION_TYPE]
                ).set_index([Columns.FORM_ID, Columns.SITE_ID, Columns.OBSERVATION_TYPE]),
            },
        ),
    ],
)
@typechecked
def test_validate_site_creek_maps_in_verify(
    site_type_map: pd.DataFrame,
    creek_type_map: pd.DataFrame,
    error_context: AbstractContextManager,
    fx: Callable,
    kwargs: dict,
) -> None:
    """Tests that _get_site_creek_maps returns valid tables."""
    with error_context, patch(
        "stormwater_monitoring_datasheet_extraction.lib.db.read.get_site_type_map",
        return_value=site_type_map,
    ), patch(
        "stormwater_monitoring_datasheet_extraction.lib.db.read.get_creek_type_map",
        return_value=creek_type_map,
    ):
        maps = fx(**kwargs)
        site_creek_merged = site_type_map.reset_index().merge(
            creek_type_map.reset_index(),
            how="outer",
            left_on=Columns.CREEK_SITE_ID,
            right_on=Columns.SITE_ID,
            suffixes=("_site", "_creek"),
        )
        returned_site_creek_merged = (
            maps[-2]
            .reset_index()
            .merge(
                maps[-1].reset_index(),
                how="outer",
                left_on=Columns.CREEK_SITE_ID,
                right_on=Columns.SITE_ID,
                suffixes=("_site", "_creek"),
            )
        )
        pd.testing.assert_frame_equal(site_creek_merged, returned_site_creek_merged)


@site_creek_type_parametrize
@pytest.mark.parametrize(
    "fx, kwargs",
    [
        (
            load_datasheets._validate_thresholds,
            {
                "observations": pd.DataFrame(
                    columns=[
                        Columns.FORM_ID,
                        Columns.SITE_ID,
                        Columns.BACTERIA_BOTTLE_NO,
                        Columns.FLOW,
                        Columns.FLOW_COMPARED_TO_EXPECTED,
                        Columns.AIR_TEMP,
                        Columns.WATER_TEMP,
                        Columns.DO_MG_PER_L,
                        Columns.SPS_MICRO_S_PER_CM,
                        Columns.SALINITY_PPT,
                        Columns.PH,
                    ]
                ).set_index([Columns.FORM_ID, Columns.SITE_ID]),
            },
        ),
        (
            load_datasheets.clean,
            {
                "verified_form_metadata": pd.DataFrame(
                    columns=[
                        Columns.FORM_ID,
                        Columns.FORM_TYPE,
                        Columns.FORM_VERSION,
                        Columns.DATE,
                        Columns.CITY,
                        Columns.TIDE_HEIGHT,
                        Columns.TIDE_TIME,
                        Columns.PAST_24HR_RAINFALL,
                        Columns.WEATHER,
                        Columns.NOTES,
                    ],
                ).set_index(Columns.FORM_ID),
                "verified_investigators": pd.DataFrame(
                    columns=[
                        Columns.FORM_ID,
                        Columns.INVESTIGATOR,
                        Columns.START_TIME,
                        Columns.END_TIME,
                    ]
                ).set_index([Columns.FORM_ID, Columns.INVESTIGATOR]),
                "verified_site_visits": pd.DataFrame(
                    columns=[
                        Columns.FORM_ID,
                        Columns.SITE_ID,
                        Columns.ARRIVAL_TIME,
                    ]
                ).set_index([Columns.FORM_ID, Columns.SITE_ID]),
                "verified_quantitative_observations": pd.DataFrame(
                    columns=[
                        Columns.FORM_ID,
                        Columns.SITE_ID,
                        Columns.BACTERIA_BOTTLE_NO,
                        Columns.FLOW,
                        Columns.FLOW_COMPARED_TO_EXPECTED,
                        Columns.AIR_TEMP,
                        Columns.WATER_TEMP,
                        Columns.DO_MG_PER_L,
                        Columns.SPS_MICRO_S_PER_CM,
                        Columns.SALINITY_PPT,
                        Columns.PH,
                    ]
                ).set_index([Columns.FORM_ID, Columns.SITE_ID]),
                "verified_qualitative_observations": pd.DataFrame(
                    columns=[
                        Columns.FORM_ID,
                        Columns.SITE_ID,
                        Columns.OBSERVATION_TYPE,
                        Columns.RANK,
                        Columns.DESCRIPTION,
                    ]
                ).set_index([Columns.FORM_ID, Columns.SITE_ID, Columns.OBSERVATION_TYPE]),
            },
        ),
    ],
)
@typechecked
def test_validate_site_creek_maps_in_clean(
    site_type_map: pd.DataFrame,
    creek_type_map: pd.DataFrame,
    error_context: AbstractContextManager,
    fx: Callable,
    kwargs: dict,
) -> None:
    """Tests that _validate_thresholds uses valid tables."""
    if fx is load_datasheets._validate_thresholds:
        kwargs["site_type_map"] = site_type_map
        kwargs["creek_type_map"] = creek_type_map
    elif fx is load_datasheets.clean:
        kwargs["verified_site_type_map"] = site_type_map
        kwargs["verified_creek_type_map"] = creek_type_map

    with error_context:
        maps = fx(**kwargs)
        if fx is load_datasheets.clean:
            site_creek_merged = site_type_map.reset_index().merge(
                creek_type_map.reset_index(),
                how="outer",
                left_on=Columns.CREEK_SITE_ID,
                right_on=Columns.SITE_ID,
                suffixes=("_site", "_creek"),
            )
            returned_site_creek_merged = (
                maps[-2]
                .reset_index()
                .merge(
                    maps[-1].reset_index(),
                    how="outer",
                    left_on=Columns.CREEK_SITE_ID,
                    right_on=Columns.SITE_ID,
                    suffixes=("_site", "_creek"),
                )
            )
            pd.testing.assert_frame_equal(site_creek_merged, returned_site_creek_merged)
