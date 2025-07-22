"""Constants for the `lib` module."""

from typing import Final

from comb_utils import DocString


class Columns:
    """Column name constants."""

    # Form metadata.
    FORM_ID: Final[str] = "form_id"
    CITY: Final[str] = "city"
    DATE: Final[str] = "date"
    NOTES: Final[str] = "notes"

    # Investigators.
    INVESTIGATOR: Final[str] = "investigator"
    START_TIME: Final[str] = "start_time"
    END_TIME: Final[str] = "end_time"

    # Field observations.
    TIDE_HEIGHT: Final[str] = "tide_height"
    TIDE_TIME: Final[str] = "tide_time"
    PAST_24HR_RAINFALL: Final[str] = "past_24hr_rainfall"
    WEATHER: Final[str] = "weather"


class DocStrings:
    """Docstrings for top-level modules."""

    RUN_ETL: Final[DocString] = DocString(
        opening="""Extracts, verifies, cleans, and loads datasheet images.

    Extracts data from the images in the input directory, verifies the extraction with the
    user, cleans and validates the data, and loads it into the output directory.
""",
        args={
            "input_dir": "Path to the input directory containing datasheet images.",
            "output_dir": (
                "Path to the output directory where processed data will be saved."
                " If empty path, defaults to a dated directory in the current working"
                " directory."
            ),
        },
        # TODO: Create custom errors module.
        raises=[],
        returns=["Path to the saved cleaned data file."],
    )
