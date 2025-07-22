"""Constants for the `lib` module."""

from enum import IntEnum, StrEnum
from typing import Any, Dict, Final

from comb_utils import DocString


class Columns:
    """Column name constants."""

    # TODO: Replace dict names with these.

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


class Flow(StrEnum):
    """Options for the flow field."""

    T = "T"
    M = "M"
    H = "H"


class FlowComparedToExpected(StrEnum):
    """Options for the flow compared to expected field."""

    LOWER = "Lower"
    NORMAL = "Normal"
    HIGHER = "Higher"


class FormType(StrEnum):
    """Options for the form type field."""

    FIELD_DATASHEET_FOSS = "field_datasheet_FOSS"


class Rank(IntEnum):
    """Options for the rank field."""

    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3


class Weather(StrEnum):
    """Options for the weather field."""

    # TODO: Consider splitting out to precipitation/cloud types and severities.

    CLOUD_CLEAR = "cloud_clear"
    CLOUD_PART = "cloud_part"
    CLOUD_OVER = "cloud_over"
    PRECIP_RAIN_LIGHT = "precip_rain_light"
    PRECIP_RAIN_MOD = "precip_rain_mod"
    PRECIP_RAIN_HEAVY = "precip_rain_heavy"
    PRECIP_SNOW = "precip_snow"


DATE_FORMAT: Final[str] = "YYYY-MM-DD"
TIME_FORMAT: Final[str] = "HH:MM"

FIELD_DATA_DEFINITION: Final[Dict[str, Any]] = {
    # TODO: Resolve these notes.
    # TODO: Create enums for categorical data.
    "dev_notes": [
        (
            "For pre-DB validation, will need to consult target DB for nullability and other "
            "constraints (uniqueness, character limits, etc.)."
        ),
        (
            "Should decide whether and how to differentiate null types, like empty fields "
            "vs. user-entered nulls (e.g., 'N/A', 'none', null sign), vs. 0."
        ),
        "See also dev_notes/notes fields in metadata section, like for the weather field.",
        (
            "The example doc has the metadata block included. It's just a copy of the "
            "metadata block in the data dictionary, so we could just leave it out of the "
            "extraction docs themselves. The advantage of doing that would be saving a "
            "little space, as well as avoiding some types of unintentional data anomalies in "
            "the case of accidental changes to the metadata. But, I chose to include "
            "metadata as part of the actual extraction document as a confirmation of "
            "provenance. This allows us to more easily handle anomalies should they arise, "
            "such as in the outside chance that we intentionally change the form (change "
            "thresholds, etc.) or the data dictionary itself. Without the metadata included "
            "with each raw extraction, in order to maintain tight provenance, we'd need to "
            "add version numbers to the metadata and put those in each extraction instead -- "
            "which is totally doable. Another advantage of including the metadata with the "
            "extraction document is for easier processing when programming or simply reading "
            "by a human. It also may prove useful if we take on other forms. Anyway, I'm "
            "open to using a metadata versioning system instead to save a little space. Or, "
            "we might want to include both a copy of the metadata and a metadata version in "
            "the extraction documents.",
        ),
        (
            "CAVEAT TO ABOVE: I just noticed a version number in the title of the "
            "downloadable empty form, so we could easily use that without having to build "
            "out our own form versioning system. I'll leave the metadata block as part of "
            "the extraction for now as a sanity check, but add the form version number field."
        ),
    ],
    "forms": {
        "form_id": {
            "form_type": str,
            "form_version": str,
            "city": str,
            "date": str,
            "notes": str,
            "investigators": {"name": {"start_time": str, "end_time": str}},
            "observations": {
                "field": {
                    "tide_height": float,
                    "tide_time": str,
                    "past_24hr_rainfall": float,
                    Columns.WEATHER: Weather,
                },
                "site": [
                    {
                        "site_id": str,
                        "bacteria_bottle_no": str,
                        "dry_outfall": bool,
                        "arrival_time": str,
                        Columns.FLOW: Flow,
                        Columns.FLOW_COMPARED_TO_EXPECTED: FlowComparedToExpected,
                        "air_temp": float,
                        "water_temp": float,
                        "DO_mg_per_l": float,
                        "SPS micro_S_per_cm": float,
                        "salinity_ppt": float,
                        "pH": float,
                        "color": {Columns.RANK: Rank, "description": str},
                        "odor": {Columns.RANK: Rank, "description": str},
                        "visual": {Columns.RANK: Rank, "description": str},
                    }
                ],
            },
        }
    },
    "metadata": {
        "date": {"format": DATE_FORMAT},
        "form_id": {
            "type": str,
            "note": (
                "Unique identifier of completed form. Different than DB's form ID if it "
                "exists, and won't likely be entered into DB, and is not found on the "
                "forms themselves. Just for convenience and to avoid trouble with "
                "accidentally sorted lists. Maybe use image filename and/or timestamp."
            ),
        },
        "form_type": {"options": list(FormType)},
        "investigators": {
            "name": str,
            "end_time": {"format": TIME_FORMAT},
            "start_time": {"format": TIME_FORMAT},
        },
        "observations": {
            "field": {
                "past_24hr_rainfall": {"units": "inches"},
                "tide_height": {"units": "feet"},
                "tide_time": {"format": TIME_FORMAT},
                Columns.WEATHER: {
                    "options": list(Weather),
                    "dev_notes": [
                        (
                            "Took a liberty to create our own str values for optional "
                            "rankings, clarity. But, likely need to convert to DB values."
                        ),
                        (
                            "It's unclear at this time if they can only select one. But, "
                            "common sense says cloud cover and precipitation levels are not "
                            "mutually exclusive. If there can be multiple weather "
                            "conditions, this will need to be a list of StrEnums (to be "
                            "validated as a set outside of JSON, along with other "
                            "validations, like no two-rain observations)."
                        ),
                    ],
                },
            },
            "site": {
                "air_temp": {"units": "Celsius"},
                "arrival_time": {"format": TIME_FORMAT},
                "color": {
                    Columns.RANK: {"options": list(Rank)},
                    "thresholds": {
                        "outfall": "Any non-natural phenomena.",
                        "creek": "Any non-natural phenomena.",
                    },
                },
                "DO_mg_per_l": {
                    "units": "mg/l",
                    "thresholds": {
                        "outfall": {"lower": {"value": 6, "inclusive": True}},
                        "creek": {"lower": {"value": 10, "inclusive": True}},
                    },
                },
                Columns.FLOW: {"options": list(Flow)},
                Columns.FLOW_COMPARED_TO_EXPECTED: {"options": list(FlowComparedToExpected)},
                "odor": {
                    Columns.RANK: {"options": list(Rank)},
                    "thresholds": {
                        "outfall": "Any non-natural phenomena.",
                        "creek": "Any non-natural phenomena.",
                    },
                },
                "pH": {
                    "units": "pH",
                    "thresholds": {
                        "outfall": {
                            "lower": {"value": 5, "inclusive": True},
                            "upper": {"value": 9, "inclusive": True},
                        },
                        "creek": {
                            "lower": {"value": 6.5, "inclusive": True},
                            "upper": {"value": 8.5, "inclusive": True},
                        },
                    },
                },
                "salinity_ppt": {"units": "ppt"},
                "SPS micro_S_per_cm": {
                    "units": "microS/cm",
                    "thresholds": {
                        "outfall": {"upper": {"value": 500, "inclusive": True}},
                        "creek": {"upper": {"value": 500, "inclusive": True}},
                    },
                },
                "visual": {
                    Columns.RANK: {"options": list(Rank)},
                    "thresholds": {
                        "outfall": "Any non-natural phenomena.",
                        "creek": "Any non-natural phenomena.",
                    },
                },
                "water_temp": {
                    "units": "Celsius",
                    "thresholds": {
                        "outfall": {
                            "upper": {"reference_value": "air_temp", "inclusive": True}
                        },
                        "creek": {
                            "habitat": {"upper": {"value": 16, "inclusive": True}},
                            "spawn": {"upper": {"value": 17.5, "inclusive": True}},
                            "rear": {"upper": {"value": 17.5, "inclusive": True}},
                            "migrate": {"upper": {"value": 17.5, "inclusive": True}},
                        },
                    },
                },
            },
        },
    },
    "example_extraction_document": {
        "metadata": {
            "date": {"format": DATE_FORMAT},
            "form_id": "str",
            "form_type": {"options": list(FormType)},
            "form_version": "str",
            "investigators": {
                "name": "str",
                "end_time": {"format": TIME_FORMAT},
                "start_time": {"format": TIME_FORMAT},
            },
            "observations": {
                "field": {
                    "past_24hr_rainfall": {"units": "inches"},
                    "tide_height": {"units": "feet"},
                    "tide_time": {"format": TIME_FORMAT},
                    Columns.WEATHER: {
                        "options": list(Weather),
                    },
                },
                "site": {
                    "air_temp": {"units": "Celsius"},
                    "arrival_time": {"format": TIME_FORMAT},
                    "color": {
                        Columns.RANK: {"options": list(Rank)},
                        "thresholds": {
                            "outfall": "Any non-natural phenomena.",
                            "creek": "Any non-natural phenomena.",
                        },
                    },
                    "DO_mg_per_l": {
                        "units": "mg/l",
                        "thresholds": {
                            "outfall": {"lower": {"value": 6, "inclusive": True}},
                            "creek": {"lower": {"value": 10.0, "inclusive": True}},
                        },
                    },
                    Columns.FLOW: {"options": list(Flow)},
                    Columns.FLOW_COMPARED_TO_EXPECTED: {
                        "options": list(FlowComparedToExpected)
                    },
                    "odor": {
                        Columns.RANK: {"options": list(Rank)},
                        "thresholds": {
                            "outfall": "Any non-natural phenomena.",
                            "creek": "Any non-natural phenomena.",
                        },
                    },
                    "pH": {
                        "units": "pH",
                        "thresholds": {
                            "outfall": {
                                "lower": {"value": 5, "inclusive": True},
                                "upper": {"value": 9, "inclusive": True},
                            },
                            "creek": {
                                "lower": {"value": 6.5, "inclusive": True},
                                "upper": {"value": 8.5, "inclusive": True},
                            },
                        },
                    },
                    "salinity_ppt": {"units": "ppt"},
                    "SPS micro_S_per_cm": {
                        "units": "microS/cm",
                        "thresholds": {
                            "outfall": {"upper": {"value": 500, "inclusive": True}},
                            "creek": {"upper": {"value": 500, "inclusive": True}},
                        },
                    },
                    "visual": {
                        Columns.RANK: {"options": list(Rank)},
                        "thresholds": {
                            "outfall": "Any non-natural phenomena.",
                            "creek": "Any non-natural phenomena.",
                        },
                    },
                    "water_temp": {
                        "units": "Celsius",
                        "thresholds": {
                            "outfall": {
                                "upper": {"reference_value": "air_temp", "inclusive": True}
                            },
                            "creek": {
                                "habitat": {"upper": {"value": 16, "inclusive": True}},
                                "spawn": {"upper": {"value": 17.5, "inclusive": True}},
                                "rear": {"upper": {"value": 17.5, "inclusive": True}},
                                "migrate": {"upper": {"value": 17.5, "inclusive": True}},
                            },
                        },
                    },
                },
            },
        },
        "forms": {
            "IMG_9527.jpg": {
                "form_type": FormType.FIELD_DATASHEET_FOSS,
                "form_version": "4.4-1-29-2025",
                "city": "BELLINGHAM",
                "date": "2025-04-17",
                "notes": "C ST: MICROBIAL MAT RETREATED ...",
                "investigators": {
                    "CIARA H": {"start_time": "14:40", "end_time": "15:23"},
                    "ANNA B": {"start_time": "14:40", "end_time": "15:23"},
                    "ZOE F": {"start_time": "15:09", "end_time": "15:23"},
                },
                "observations": {
                    "field": {
                        "tide_height": -0.7,
                        "tide_time": "14:39",
                        "past_24hr_rainfall": 0.0,
                        Columns.WEATHER: Weather.CLOUD_CLEAR,
                    },
                    "site": [
                        {
                            "site_id": "C ST",
                            "bacteria_bottle_no": "B1",
                            "dry_outfall": False,
                            "arrival_time": "14:41",
                            Columns.FLOW: Flow.M,
                            Columns.FLOW_COMPARED_TO_EXPECTED: FlowComparedToExpected.NORMAL,
                            "air_temp": 21.0,
                            "water_temp": 11.6,
                            "DO_mg_per_l": 10.35,
                            "SPS micro_S_per_cm": 414.1,
                            "salinity_ppt": 0.2,
                            "pH": 5.91,
                            "color": {Columns.RANK: Rank.ONE, "description": "YELLOW"},
                            "odor": {Columns.RANK: Rank.ONE, "description": "SULPHUR"},
                            "visual": {Columns.RANK: None, "description": None},
                        },
                        {
                            "site_id": "C ST",
                            "bacteria_bottle_no": "B2",
                            "dry_outfall": False,
                            "arrival_time": "14:41",
                            Columns.FLOW: Flow.M,
                            Columns.FLOW_COMPARED_TO_EXPECTED: FlowComparedToExpected.NORMAL,
                            "air_temp": 21.0,
                            "water_temp": 11.2,
                            "DO_mg_per_l": 10.41,
                            "SPS micro_S_per_cm": 369.9,
                            "salinity_ppt": 0.18,
                            "pH": 5.5,
                            "color": {Columns.RANK: Rank.ONE, "description": "YELLOW"},
                            "odor": {Columns.RANK: Rank.ONE, "description": "SULPHUR"},
                            "visual": {Columns.RANK: None, "description": None},
                        },
                        {
                            "site_id": "BROADWAY",
                            "bacteria_bottle_no": "B3",
                            "dry_outfall": False,
                            "arrival_time": "15:09",
                            Columns.FLOW: Flow.M,
                            Columns.FLOW_COMPARED_TO_EXPECTED: FlowComparedToExpected.NORMAL,
                            "air_temp": 22.0,
                            "water_temp": 11.1,
                            "DO_mg_per_l": 10.73,
                            "SPS micro_S_per_cm": 314.1,
                            "salinity_ppt": 0.15,
                            "pH": 7.40,
                            "color": {Columns.RANK: Rank.ONE, "description": "YELLOW"},
                            "odor": {Columns.RANK: Rank.ONE, "description": "SULPHUR"},
                            "visual": {Columns.RANK: None, "description": None},
                        },
                    ],
                },
            },
            "sheet1.jpg": {
                "form_type": FormType.FIELD_DATASHEET_FOSS,
                "form_version": "4.4-1-29-2025",
                "city": "BELLINGHAM",
                "date": "2025-04-21",
                "notes": "Padden - DO%",
                "investigators": {
                    "ANNA": {"start_time": "17:10"},
                    "PAT": {"start_time": "17:10"},
                    "CHRIS": {"start_time": "17:10"},
                },
                "observations": {
                    "field": {
                        "tide_height": 0.22,
                        "tide_time": "17:10",
                        "past_24hr_rainfall": None,
                        Columns.WEATHER: Weather.CLOUD_CLEAR,
                    },
                    "site": [
                        {
                            "site_id": "PADDEN",
                            "bacteria_bottle_no": "B5",
                            "dry_outfall": False,
                            "arrival_time": "17:10",
                            Columns.FLOW: Flow.H,
                            Columns.FLOW_COMPARED_TO_EXPECTED: FlowComparedToExpected.NORMAL,
                            "air_temp": 16,
                            "water_temp": 11.6,
                            "DO_mg_per_l": 102.1,
                            "SPS micro_S_per_cm": 151.0,
                            "salinity_ppt": 0.07,
                            "pH": 7.73,
                            "color": {Columns.RANK: Rank.ONE, "description": "TAN"},
                            "odor": {Columns.RANK: Rank.ZERO, "description": None},
                            "visual": {Columns.RANK: Rank.ZERO, "description": None},
                        },
                        {
                            "site_id": "BENASFASDF",
                            "bacteria_bottle_no": "B6",
                            "dry_outfall": False,
                            "arrival_time": "17:33",
                            Columns.FLOW: Flow.H,
                            Columns.FLOW_COMPARED_TO_EXPECTED: FlowComparedToExpected.NORMAL,
                            "air_temp": 18,
                            "water_temp": 11.4,
                            "DO_mg_per_l": 11.03,
                            "SPS micro_S_per_cm": 234.7,
                            "salinity_ppt": 0.11,
                            "pH": 7.87,
                            "color": {Columns.RANK: Rank.ONE, "description": "Tan/brown"},
                            "odor": {Columns.RANK: None, "description": None},
                            "visual": {Columns.RANK: None, "description": None},
                        },
                        {
                            "site_id": "BEPSODF72",
                            "bacteria_bottle_no": "B7",
                            "dry_outfall": False,
                            "arrival_time": "17:40",
                            Columns.FLOW: Flow.H,
                            Columns.FLOW_COMPARED_TO_EXPECTED: FlowComparedToExpected.NORMAL,
                            "air_temp": None,
                            "water_temp": 11.4,
                            "DO_mg_per_l": 11.17,
                            "SPS micro_S_per_cm": 235.1,
                            "salinity_ppt": 0.11,
                            "pH": 7.82,
                            "color": {Columns.RANK: Rank.ONE, "description": "Brown"},
                            "odor": {Columns.RANK: None, "description": None},
                            "visual": {Columns.RANK: None, "description": None},
                        },
                    ],
                },
            },
        },
    },
}
