"""Constants for the `lib` module."""

from typing import Any, Dict, Final

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


FIELD_DATA_DEFINITION: Final[Dict[str, Any]] = {
    # TODO: Resolve these notes.
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
            "investigators": {"name": {"start_time": str, "end_time": str}},
            "notes": str,
            "observations": {
                "field": {
                    "tide_height": float,
                    "tide_time": str,
                    "past_24hr_rainfall": float,
                    "weather": str,
                },
                "site": [
                    {
                        "site_id": str,
                        "bacteria_bottle_no": str,
                        "dry_outfall": bool,
                        "arrival_time": str,
                        "flow": str,
                        "flow_compared_to_expected": str,
                        "air_temp": float,
                        "water_temp": float,
                        "DO_mg_per_l": float,
                        "SPS micro_S_per_cm": float,
                        "salinity_ppt": float,
                        "pH": float,
                        "color": {"rank": int, "description": str},
                        "odor": {"rank": int, "description": str},
                        "visual": {"rank": int, "description": str},
                    }
                ],
            },
        }
    },
    "metadata": {
        "date": {"format": "YYYY-MM-DD"},
        "form_id": {
            "note": (
                "Unique identifier of completed form. Different than DB's form ID if it "
                "exists, and won't likely be entered into DB, and is not found on the "
                "forms themselves. Just for convenience and to avoid trouble with "
                "accidentally sorted lists. Maybe use image filename and/or timestamp."
            )
        },
        "form_type": {
            "options": ["field_datasheet_stormwater_monitoring_friends_of_salish_sea"]
        },
        "investigators": {
            "name": str,
            "end_time": {"format": "HH:MM"},
            "start_time": {"format": "HH:MM"},
        },
        "observations": {
            "field": {
                "past_24hr_rainfall": {"units": "inches"},
                "tide_height": {"units": "feet"},
                "tide_time": {"format": "HH:MM"},
                "weather": {
                    "options": [
                        "cloud_clear",
                        "cloud_part",
                        "cloud_over",
                        "precip_rain_light",
                        "precip_rain_mod",
                        "precip_rain_heavy",
                        "precip_snow",
                    ],
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
                "arrival_time": {"format": "HH:MM"},
                "color": {
                    "rank": {"options": [0, 1, 2, 3]},
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
                "flow": {"options": ["T", "M", "H"]},
                "flow_compared_to_expected": {"options": ["Lower", "Normal", "Higher"]},
                "odor": {
                    "rank": {"options": [0, 1, 2, 3]},
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
                    "rank": {"options": [0, 1, 2, 3]},
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
}
