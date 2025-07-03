"""Internal functions for the stormwater monitoring datasheet extraction API."""

from pathlib import Path

from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib import load_datasheets
from stormwater_monitoring_datasheet_extraction.lib.constants import DocStrings


@typechecked
def run_etl(input_dir: Path, output_dir: Path) -> Path:  # noqa: D103
    return load_datasheets.run_etl(input_dir=input_dir, output_dir=output_dir)


run_etl.__doc__ = DocStrings.RUN_ETL.api_docstring
