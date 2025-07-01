# noqa: D100
__doc__ = """
.. click:: stormwater_monitoring_datasheet_extraction.cli.example:main
    :prog: example
    :nested: full
"""

import click
from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib import example
from stormwater_monitoring_datasheet_extraction.lib.constants import DocStrings


@click.command(help=DocStrings.EXAMPLE.cli_docstring)
@click.option(
    "--seconds", type=int, required=False, default=1, help=DocStrings.EXAMPLE.args["seconds"]
)
@typechecked
def main(seconds: int = 1) -> None:  # noqa: D103
    example.wait_a_second(seconds=seconds)
