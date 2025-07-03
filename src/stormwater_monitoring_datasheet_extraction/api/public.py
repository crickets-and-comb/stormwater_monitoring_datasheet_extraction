"""Public functions for the stormwater monitoring datasheet extraction API."""

from pathlib import Path

from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.api import internal
from stormwater_monitoring_datasheet_extraction.lib.constants import DocStrings


@typechecked
def run_etl(input_dir: Path, output_dir: Path) -> Path:  # noqa: D103
    return internal.run_etl(input_dir=input_dir, output_dir=output_dir)


run_etl.__doc__ = DocStrings.RUN_ETL.api_docstring
