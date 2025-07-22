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

    # Site observations.
    SITE_ID: Final[str] = "site_id"
    BOTTLE_NO: Final[str] = "bottle_no"
    DRY_OUTFALL: Final[str] = "dry_outfall"
    ARRIVAL_TIME: Final[str] = "arrival_time"
    FLOW: Final[str] = "flow"
    FLOW_COMPARED_TO_EXPECTED: Final[str] = "flow_compared_to_expected"
    AIR_TEMP: Final[str] = "air_temp"
    WATER_TEMP: Final[str] = "water_temp"
    DO_MG_PER_L: Final[str] = "DO_mg_per_l"
    SPS_MICRO_S_PER_CM: Final[str] = "SPS micro_S_per_cm"
    SALINITY_PPT: Final[str] = "salinity_ppt"
    PH: Final[str] = "pH"

    # Qualitative site observations: color, odor, visual.
    TYPE: Final[str] = "type"
    RANK: Final[str] = "rank"
    DESCRIPTION: Final[str] = "description"


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
