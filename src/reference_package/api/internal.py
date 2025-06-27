"""Internal functions overlay library and are typically wrapped by public functions.

This allows us to maintain a separation of API from implementation.
Internal functions may come with extra options that public functions don't have, say for
power users and developers who may want to use an existing DB session or something.
"""

from typeguard import typechecked

from reference_package.lib import example
from reference_package.lib.constants import DocStrings


@typechecked
def wait_a_second(seconds: int = 1, extra_string: str = "") -> None:  # noqa: D103
    extra_string = extra_string.upper().strip()
    example.wait_a_second(seconds=seconds, extra_string=extra_string)


wait_a_second.__doc__ = DocStrings.EXAMPLE_INTERNAL.api_docstring
