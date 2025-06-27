"""Public functions wrap internal functions which wrap library functions.

This allows separation of API from implementation. It also allows a simplified public API
separate from a more complex internal API with more options for power users.
"""

from typeguard import typechecked

from reference_package.api.internal import example
from reference_package.lib.constants import DocStrings


@typechecked
def wait_a_second(seconds: int = 1) -> None:  # noqa: D103
    example.wait_a_second(seconds=seconds)


wait_a_second.__doc__ = DocStrings.EXAMPLE.api_docstring
