"""This is an example module."""

import time

from typeguard import typechecked

from reference_package.lib.constants import DocStrings


@typechecked
def wait_a_second(seconds: int = 1, extra_string: str = "") -> None:  # noqa: D103
    print(f"Waiting {seconds} seconds.{' ' + extra_string if extra_string else ''}")
    time.sleep(seconds)


wait_a_second.__doc__ = DocStrings.EXAMPLE_INTERNAL.api_docstring
