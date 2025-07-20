# noqa: D100
__doc__ = """
.. click:: stormwater_monitoring_datasheet_extraction.cli.run_etl:main
    :prog: run_etl
    :nested: full
"""

from pathlib import Path

import click
from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.api.public import run_etl
from stormwater_monitoring_datasheet_extraction.lib.constants import DocStrings


@click.command(help=DocStrings.RUN_ETL.cli_docstring)
@click.option(
    "--input_dir",
    type=str,
    required=True,
    help=DocStrings.RUN_ETL.args["input_dir"],
)
@click.option(
    "--output_dir",
    type=str,
    required=False,
    default="",
    help=DocStrings.RUN_ETL.args["output_dir"],
)
@typechecked
def main(input_dir: str, output_dir: str) -> None:  # noqa: D103
    final_output_path = run_etl(input_dir=Path(input_dir), output_dir=Path(output_dir))
    click.echo(f"ETL process completed. Final output saved to: {final_output_path}")
    # TODO: See `bfb_delivery` for how to return path and test CLI.
