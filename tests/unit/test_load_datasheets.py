"""Test the load_datasheets module."""

# TODO: Test that returns correct path, using pytest.mark.parametrize.
from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import Final
from unittest.mock import patch

import pandas as pd
import pytest
from tests.unit.conftest import site_creek_type_parametrize
from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib import constants, load_datasheets
from stormwater_monitoring_datasheet_extraction.lib.constants import Columns

# TODO: Test that returns correct path, using pytest.mark.parametrize.

_EMPTY_FORM_METADATA: Final[pd.DataFrame] = pd.DataFrame(
    {
        Columns.FORM_ID: pd.Series(dtype=str),
        Columns.FORM_TYPE: pd.Series(
            dtype=pd.CategoricalDtype(categories=list(constants.FormType))
        ),
        Columns.FORM_VERSION: pd.Series(dtype=str),
        Columns.DATE: pd.Series(dtype=str),
        Columns.CITY: pd.Series(dtype=pd.CategoricalDtype(categories=list(constants.City))),
        Columns.TIDE_HEIGHT: pd.Series(dtype=float),
        Columns.TIDE_TIME: pd.Series(dtype=str),
        Columns.PAST_24HR_RAINFALL: pd.Series(dtype=float),
        Columns.WEATHER: pd.Series(
            dtype=pd.CategoricalDtype(categories=list(constants.Weather))
        ),
        Columns.NOTES: pd.Series(dtype=str),
    },
).set_index(Columns.FORM_ID)
_EMPTY_INVESTIGATORS: Final[pd.DataFrame] = pd.DataFrame(
    {
        Columns.FORM_ID: pd.Series(dtype=str),
        Columns.INVESTIGATOR: pd.Series(dtype=str),
        Columns.START_TIME: pd.Series(dtype=str),
        Columns.END_TIME: pd.Series(dtype=str),
    }
).set_index([Columns.FORM_ID, Columns.INVESTIGATOR])
_EMPTY_SITE_VISITS: Final[pd.DataFrame] = pd.DataFrame(
    {
        Columns.FORM_ID: pd.Series(dtype=str),
        Columns.SITE_ID: pd.Series(dtype=str),
        Columns.ARRIVAL_TIME: pd.Series(dtype=str),
    }
).set_index([Columns.FORM_ID, Columns.SITE_ID])
_EMPTY_QUAN_OBS: Final[pd.DataFrame] = pd.DataFrame(
    {
        Columns.FORM_ID: pd.Series(dtype=str),
        Columns.SITE_ID: pd.Series(dtype=str),
        Columns.BACTERIA_BOTTLE_NO: pd.Series(dtype=str),
        Columns.FLOW: pd.Series(dtype=pd.CategoricalDtype(categories=list(constants.Flow))),
        Columns.FLOW_COMPARED_TO_EXPECTED: pd.Series(
            dtype=pd.CategoricalDtype(categories=list(constants.FlowComparedToExpected))
        ),
        Columns.AIR_TEMP: pd.Series(dtype=float),
        Columns.WATER_TEMP: pd.Series(dtype=float),
        Columns.DO_MG_PER_L: pd.Series(dtype=float),
        Columns.SPS_MICRO_S_PER_CM: pd.Series(dtype=float),
        Columns.SALINITY_PPT: pd.Series(dtype=float),
        Columns.PH: pd.Series(dtype=float),
    }
).set_index([Columns.FORM_ID, Columns.SITE_ID])
_EMPTY_QUAL_OBS: Final[pd.DataFrame] = pd.DataFrame(
    {
        Columns.FORM_ID: pd.Series(dtype=str),
        Columns.SITE_ID: pd.Series(dtype=str),
        Columns.OBSERVATION_TYPE: pd.Series(
            dtype=pd.CategoricalDtype(
                categories=list(constants.QualitativeSiteObservationTypes)
            )
        ),
        Columns.RANK: pd.Series(dtype="int64"),
        Columns.DESCRIPTION: pd.Series(dtype=str),
    }
).set_index([Columns.FORM_ID, Columns.SITE_ID, Columns.OBSERVATION_TYPE])


@site_creek_type_parametrize
@pytest.mark.parametrize(
    "fx, kwargs",
    [
        (load_datasheets._get_site_creek_maps, {}),
        (
            load_datasheets.verify,
            {
                "precleaned_form_metadata": _EMPTY_FORM_METADATA,
                "precleaned_investigators": _EMPTY_INVESTIGATORS,
                "precleaned_site_visits": _EMPTY_SITE_VISITS,
                "precleaned_quantitative_observations": _EMPTY_QUAN_OBS,
                "precleaned_qualitative_observations": _EMPTY_QUAL_OBS,
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
                "observations": _EMPTY_QUAN_OBS,
            },
        ),
        (
            load_datasheets.clean,
            {
                "verified_form_metadata": _EMPTY_FORM_METADATA,
                "verified_investigators": _EMPTY_INVESTIGATORS,
                "verified_site_visits": _EMPTY_SITE_VISITS,
                "verified_quantitative_observations": _EMPTY_QUAN_OBS,
                "verified_qualitative_observations": _EMPTY_QUAL_OBS,
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
