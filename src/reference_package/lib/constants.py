"""Constants for the `lib` module."""

from typing import Final

from comb_utils import DocString


class DocStrings:
    """Docstrings for the `example` module."""

    EXAMPLE: Final[DocString] = DocString(
        opening="""Just wait a second, or however many seconds you want.

    Also prints a message with the number you passed.
""",
        args={"seconds": "How many seconds to wait."},
        raises=[],
        returns=[],
    )

    EXAMPLE_INTERNAL: Final[DocString] = DocString(
        opening="""Just wait a second, or however many seconds you want.

    Also prints a message with the number you passed.
""",
        args={
            "seconds": "How many seconds to wait.",
            "extra_string": "Extra message to add on tail of existing message.",
        },
        raises=[],
        returns=[],
    )
