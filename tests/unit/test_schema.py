"""Test the schema module."""

from contextlib import AbstractContextManager

import pandas as pd
from tests.unit.conftest import site_creek_type_parametrize
from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib.schema.checks import relational

# TODO: Test that returns correct path, using pytest.mark.parametrize.


@site_creek_type_parametrize
@typechecked
def test_validate_site_creek_map(
    site_type_map: pd.DataFrame,
    creek_type_map: pd.DataFrame,
    error_context: AbstractContextManager,
) -> None:
    """Tests that the site/creek map validation works."""
    with error_context:
        relational.validate_site_creek_map(
            site_type_map=site_type_map, creek_type_map=creek_type_map
        )
