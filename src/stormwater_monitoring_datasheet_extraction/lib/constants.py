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
    BACTERIA_BOTTLE_NO: Final[str] = "bacteria_bottle_no"
    DRY_OUTFALL: Final[str] = "dry_outfall"
    ARRIVAL_TIME: Final[str] = "arrival_time"
    FLOW: Final[str] = "flow"
    FLOW_COMPARED_TO_EXPECTED: Final[str] = "flow_compared_to_expected"
    AIR_TEMP: Final[str] = "air_temp"
    WATER_TEMP: Final[str] = "water_temp"
    DO_MG_PER_L: Final[str] = "DO_mg_per_l"
    SPS_MICRO_S_PER_CM: Final[str] = "SPS_micro_S_per_cm"
    SALINITY_PPT: Final[str] = "salinity_ppt"
    PH: Final[str] = "pH"

    # Qualitative site observations: color, odor, visual.
    OBSERVATION_TYPE: Final[str] = "observation_type"
    RANK: Final[str] = "rank"
    DESCRIPTION: Final[str] = "description"

    # Other
    COLOR: Final[str] = "color"
    CREEK: Final[str] = "creek"
    DATA_TYPE: Final[str] = "data_type"
    FIELD: Final[str] = "field"
    FORM_TYPE: Final[str] = "form_type"
    FORM_VERSION: Final[str] = "form_version"
    FORMAT: Final[str] = "format"
    FORMS: Final[str] = "forms"
    HABITAT: Final[str] = "habitat"
    INCLUSIVE: Final[str] = "inclusive"
    INVESTIGATORS: Final[str] = "investigators"
    LOWER: Final[str] = "lower"
    METADATA: Final[str] = "metadata"
    MIGRATE: Final[str] = "migrate"
    OBSERVATIONS: Final[str] = "observations"
    ODOR: Final[str] = "odor"
    OPTIONS: Final[str] = "options"
    OUTFALL: Final[str] = "outfall"
    REAR: Final[str] = "rear"
    REFERENCE_VALUE: Final[str] = "reference_value"
    SITE: Final[str] = "site"
    SPAWN: Final[str] = "spawn"
    THRESHOLDS: Final[str] = "thresholds"
    UNITS: Final[str] = "units"
    UPPER: Final[str] = "upper"
    VALUE: Final[str] = "value"
    VISUAL: Final[str] = "visual"


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


class QualitativeSiteObservationTypes(StrEnum):
    """Options for the qualitative site observation types field."""

    COLOR = Columns.COLOR
    ODOR = Columns.ODOR
    VISUAL = Columns.VISUAL


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
    Columns.FORMS: {
        Columns.FORM_ID: {
            Columns.FORM_TYPE: str,
            Columns.FORM_VERSION: str,
            Columns.CITY: str,
            Columns.DATE: str,
            Columns.NOTES: str,
            Columns.INVESTIGATORS: {
                Columns.INVESTIGATOR: {Columns.START_TIME: str, Columns.END_TIME: str}
            },
            Columns.OBSERVATIONS: {
                Columns.FIELD: {
                    Columns.TIDE_HEIGHT: float,
                    Columns.TIDE_TIME: str,
                    Columns.PAST_24HR_RAINFALL: float,
                    Columns.WEATHER: Weather,
                },
                Columns.SITE: [
                    {
                        Columns.SITE_ID: str,
                        Columns.BACTERIA_BOTTLE_NO: str,
                        Columns.DRY_OUTFALL: bool,
                        Columns.ARRIVAL_TIME: str,
                        Columns.FLOW: Flow,
                        Columns.FLOW_COMPARED_TO_EXPECTED: FlowComparedToExpected,
                        Columns.AIR_TEMP: float,
                        Columns.WATER_TEMP: float,
                        Columns.DO_MG_PER_L: float,
                        Columns.SPS_MICRO_S_PER_CM: float,
                        Columns.SALINITY_PPT: float,
                        Columns.PH: float,
                        QualitativeSiteObservationTypes.COLOR: {
                            Columns.RANK: Rank,
                            Columns.DESCRIPTION: str,
                        },
                        QualitativeSiteObservationTypes.ODOR: {
                            Columns.RANK: Rank,
                            Columns.DESCRIPTION: str,
                        },
                        QualitativeSiteObservationTypes.VISUAL: {
                            Columns.RANK: Rank,
                            Columns.DESCRIPTION: str,
                        },
                    }
                ],
            },
        }
    },
    Columns.METADATA: {
        Columns.DATE: {Columns.FORMAT: DATE_FORMAT},
        Columns.FORM_ID: {
            Columns.DATA_TYPE: str,
            # TODO: Make dev_notes into comments.
            "dev_notes": (
                "Unique identifier of completed form. Different than DB's form ID if it "
                "exists, and won't likely be entered into DB, and is not found on the "
                "forms themselves. Just for convenience and to avoid trouble with "
                "accidentally sorted lists. Maybe use image filename and/or timestamp."
            ),
        },
        Columns.FORM_TYPE: {Columns.OPTIONS: list(FormType)},
        Columns.INVESTIGATORS: {
            Columns.INVESTIGATOR: str,
            Columns.END_TIME: {Columns.FORMAT: TIME_FORMAT},
            Columns.START_TIME: {Columns.FORMAT: TIME_FORMAT},
        },
        Columns.OBSERVATIONS: {
            Columns.FIELD: {
                Columns.PAST_24HR_RAINFALL: {Columns.UNITS: "inches"},
                Columns.TIDE_HEIGHT: {Columns.UNITS: "feet"},
                Columns.TIDE_TIME: {Columns.FORMAT: TIME_FORMAT},
                Columns.WEATHER: {
                    Columns.OPTIONS: list(Weather),
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
            Columns.SITE: {
                Columns.AIR_TEMP: {Columns.UNITS: "Celsius"},
                Columns.ARRIVAL_TIME: {Columns.FORMAT: TIME_FORMAT},
                QualitativeSiteObservationTypes.COLOR: {
                    Columns.RANK: {Columns.OPTIONS: list(Rank)},
                    Columns.THRESHOLDS: {
                        Columns.OUTFALL: "Any non-natural phenomena.",
                        Columns.CREEK: "Any non-natural phenomena.",
                    },
                },
                Columns.DO_MG_PER_L: {
                    Columns.UNITS: "mg/l",
                    Columns.THRESHOLDS: {
                        Columns.OUTFALL: {
                            Columns.LOWER: {Columns.VALUE: 6, Columns.INCLUSIVE: True}
                        },
                        Columns.CREEK: {
                            Columns.LOWER: {Columns.VALUE: 10, Columns.INCLUSIVE: True}
                        },
                    },
                },
                Columns.FLOW: {Columns.OPTIONS: list(Flow)},
                Columns.FLOW_COMPARED_TO_EXPECTED: {
                    Columns.OPTIONS: list(FlowComparedToExpected)
                },
                QualitativeSiteObservationTypes.ODOR: {
                    Columns.RANK: {Columns.OPTIONS: list(Rank)},
                    Columns.THRESHOLDS: {
                        Columns.OUTFALL: "Any non-natural phenomena.",
                        Columns.CREEK: "Any non-natural phenomena.",
                    },
                },
                Columns.PH: {
                    Columns.UNITS: "pH",
                    Columns.THRESHOLDS: {
                        Columns.OUTFALL: {
                            Columns.LOWER: {Columns.VALUE: 5, Columns.INCLUSIVE: True},
                            Columns.UPPER: {Columns.VALUE: 9, Columns.INCLUSIVE: True},
                        },
                        Columns.CREEK: {
                            Columns.LOWER: {Columns.VALUE: 6.5, Columns.INCLUSIVE: True},
                            Columns.UPPER: {Columns.VALUE: 8.5, Columns.INCLUSIVE: True},
                        },
                    },
                },
                Columns.SALINITY_PPT: {Columns.UNITS: "ppt"},
                Columns.SPS_MICRO_S_PER_CM: {
                    Columns.UNITS: "microS/cm",
                    Columns.THRESHOLDS: {
                        Columns.OUTFALL: {
                            Columns.UPPER: {Columns.VALUE: 500, Columns.INCLUSIVE: True}
                        },
                        Columns.CREEK: {
                            Columns.UPPER: {Columns.VALUE: 500, Columns.INCLUSIVE: True}
                        },
                    },
                },
                QualitativeSiteObservationTypes.VISUAL: {
                    Columns.RANK: {Columns.OPTIONS: list(Rank)},
                    Columns.THRESHOLDS: {
                        Columns.OUTFALL: "Any non-natural phenomena.",
                        Columns.CREEK: "Any non-natural phenomena.",
                    },
                },
                Columns.WATER_TEMP: {
                    Columns.UNITS: "Celsius",
                    Columns.THRESHOLDS: {
                        Columns.OUTFALL: {
                            Columns.UPPER: {
                                Columns.REFERENCE_VALUE: Columns.AIR_TEMP,
                                Columns.INCLUSIVE: True,
                            }
                        },
                        Columns.CREEK: {
                            Columns.HABITAT: {
                                Columns.UPPER: {Columns.VALUE: 16, Columns.INCLUSIVE: True}
                            },
                            Columns.SPAWN: {
                                Columns.UPPER: {Columns.VALUE: 17.5, Columns.INCLUSIVE: True}
                            },
                            Columns.REAR: {
                                Columns.UPPER: {Columns.VALUE: 17.5, Columns.INCLUSIVE: True}
                            },
                            Columns.MIGRATE: {
                                Columns.UPPER: {Columns.VALUE: 17.5, Columns.INCLUSIVE: True}
                            },
                        },
                    },
                },
            },
        },
    },
    "example_extraction_document": {
        Columns.METADATA: {
            Columns.DATE: {Columns.FORMAT: DATE_FORMAT},
            Columns.FORM_ID: str,
            Columns.FORM_TYPE: {Columns.OPTIONS: list(FormType)},
            Columns.FORM_VERSION: str,
            Columns.INVESTIGATORS: {
                Columns.INVESTIGATOR: str,
                Columns.END_TIME: {Columns.FORMAT: TIME_FORMAT},
                Columns.START_TIME: {Columns.FORMAT: TIME_FORMAT},
            },
            Columns.OBSERVATIONS: {
                Columns.FIELD: {
                    Columns.PAST_24HR_RAINFALL: {Columns.UNITS: "inches"},
                    Columns.TIDE_HEIGHT: {Columns.UNITS: "feet"},
                    Columns.TIDE_TIME: {Columns.FORMAT: TIME_FORMAT},
                    Columns.WEATHER: {
                        Columns.OPTIONS: list(Weather),
                    },
                },
                Columns.SITE: {
                    Columns.AIR_TEMP: {Columns.UNITS: "Celsius"},
                    Columns.ARRIVAL_TIME: {Columns.FORMAT: TIME_FORMAT},
                    QualitativeSiteObservationTypes.COLOR: {
                        Columns.RANK: {Columns.OPTIONS: list(Rank)},
                        Columns.THRESHOLDS: {
                            Columns.OUTFALL: "Any non-natural phenomena.",
                            Columns.CREEK: "Any non-natural phenomena.",
                        },
                    },
                    Columns.DO_MG_PER_L: {
                        Columns.UNITS: "mg/l",
                        Columns.THRESHOLDS: {
                            Columns.OUTFALL: {
                                Columns.LOWER: {Columns.VALUE: 6, Columns.INCLUSIVE: True}
                            },
                            Columns.CREEK: {
                                Columns.LOWER: {Columns.VALUE: 10.0, Columns.INCLUSIVE: True}
                            },
                        },
                    },
                    Columns.FLOW: {Columns.OPTIONS: list(Flow)},
                    Columns.FLOW_COMPARED_TO_EXPECTED: {
                        Columns.OPTIONS: list(FlowComparedToExpected)
                    },
                    QualitativeSiteObservationTypes.ODOR: {
                        Columns.RANK: {Columns.OPTIONS: list(Rank)},
                        Columns.THRESHOLDS: {
                            Columns.OUTFALL: "Any non-natural phenomena.",
                            Columns.CREEK: "Any non-natural phenomena.",
                        },
                    },
                    Columns.PH: {
                        Columns.UNITS: "pH",
                        Columns.THRESHOLDS: {
                            Columns.OUTFALL: {
                                Columns.LOWER: {Columns.VALUE: 5, Columns.INCLUSIVE: True},
                                Columns.UPPER: {Columns.VALUE: 9, Columns.INCLUSIVE: True},
                            },
                            Columns.CREEK: {
                                Columns.LOWER: {Columns.VALUE: 6.5, Columns.INCLUSIVE: True},
                                Columns.UPPER: {Columns.VALUE: 8.5, Columns.INCLUSIVE: True},
                            },
                        },
                    },
                    Columns.SALINITY_PPT: {Columns.UNITS: "ppt"},
                    Columns.SPS_MICRO_S_PER_CM: {
                        Columns.UNITS: "microS/cm",
                        Columns.THRESHOLDS: {
                            Columns.OUTFALL: {
                                Columns.UPPER: {Columns.VALUE: 500, Columns.INCLUSIVE: True}
                            },
                            Columns.CREEK: {
                                Columns.UPPER: {Columns.VALUE: 500, Columns.INCLUSIVE: True}
                            },
                        },
                    },
                    QualitativeSiteObservationTypes.VISUAL: {
                        Columns.RANK: {Columns.OPTIONS: list(Rank)},
                        Columns.THRESHOLDS: {
                            Columns.OUTFALL: "Any non-natural phenomena.",
                            Columns.CREEK: "Any non-natural phenomena.",
                        },
                    },
                    Columns.WATER_TEMP: {
                        Columns.UNITS: "Celsius",
                        Columns.THRESHOLDS: {
                            Columns.OUTFALL: {
                                Columns.UPPER: {
                                    Columns.REFERENCE_VALUE: Columns.AIR_TEMP,
                                    Columns.INCLUSIVE: True,
                                }
                            },
                            Columns.CREEK: {
                                Columns.HABITAT: {
                                    Columns.UPPER: {
                                        Columns.VALUE: 16,
                                        Columns.INCLUSIVE: True,
                                    }
                                },
                                Columns.SPAWN: {
                                    Columns.UPPER: {
                                        Columns.VALUE: 17.5,
                                        Columns.INCLUSIVE: True,
                                    }
                                },
                                Columns.REAR: {
                                    Columns.UPPER: {
                                        Columns.VALUE: 17.5,
                                        Columns.INCLUSIVE: True,
                                    }
                                },
                                Columns.MIGRATE: {
                                    Columns.UPPER: {
                                        Columns.VALUE: 17.5,
                                        Columns.INCLUSIVE: True,
                                    }
                                },
                            },
                        },
                    },
                },
            },
        },
        Columns.FORMS: {
            "IMG_9527.jpg": {
                Columns.FORM_TYPE: FormType.FIELD_DATASHEET_FOSS,
                Columns.FORM_VERSION: "4.4-1-29-2025",
                Columns.CITY: "BELLINGHAM",
                Columns.DATE: "2025-04-17",
                Columns.NOTES: "C ST: MICROBIAL MAT RETREATED ...",
                Columns.INVESTIGATORS: {
                    "CIARA H": {Columns.START_TIME: "14:40", Columns.END_TIME: "15:23"},
                    "ANNA B": {Columns.START_TIME: "14:40", Columns.END_TIME: "15:23"},
                    "ZOE F": {Columns.START_TIME: "15:09", Columns.END_TIME: "15:23"},
                },
                Columns.OBSERVATIONS: {
                    Columns.FIELD: {
                        Columns.TIDE_HEIGHT: -0.7,
                        Columns.TIDE_TIME: "14:39",
                        Columns.PAST_24HR_RAINFALL: 0.0,
                        Columns.WEATHER: Weather.CLOUD_CLEAR,
                    },
                    Columns.SITE: [
                        {
                            Columns.SITE_ID: "C ST",
                            Columns.BACTERIA_BOTTLE_NO: "B1",
                            Columns.DRY_OUTFALL: False,
                            Columns.ARRIVAL_TIME: "14:41",
                            Columns.FLOW: Flow.M,
                            Columns.FLOW_COMPARED_TO_EXPECTED: FlowComparedToExpected.NORMAL,
                            Columns.AIR_TEMP: 21.0,
                            Columns.WATER_TEMP: 11.6,
                            Columns.DO_MG_PER_L: 10.35,
                            Columns.SPS_MICRO_S_PER_CM: 414.1,
                            Columns.SALINITY_PPT: 0.2,
                            Columns.PH: 5.91,
                            QualitativeSiteObservationTypes.COLOR: {
                                Columns.RANK: Rank.ONE,
                                Columns.DESCRIPTION: "YELLOW",
                            },
                            QualitativeSiteObservationTypes.ODOR: {
                                Columns.RANK: Rank.ONE,
                                Columns.DESCRIPTION: "SULPHUR",
                            },
                            QualitativeSiteObservationTypes.VISUAL: {
                                Columns.RANK: None,
                                Columns.DESCRIPTION: None,
                            },
                        },
                        {
                            Columns.SITE_ID: "C ST",
                            Columns.BACTERIA_BOTTLE_NO: "B2",
                            Columns.DRY_OUTFALL: False,
                            Columns.ARRIVAL_TIME: "14:41",
                            Columns.FLOW: Flow.M,
                            Columns.FLOW_COMPARED_TO_EXPECTED: FlowComparedToExpected.NORMAL,
                            Columns.AIR_TEMP: 21.0,
                            Columns.WATER_TEMP: 11.2,
                            Columns.DO_MG_PER_L: 10.41,
                            Columns.SPS_MICRO_S_PER_CM: 369.9,
                            Columns.SALINITY_PPT: 0.18,
                            Columns.PH: 5.5,
                            QualitativeSiteObservationTypes.COLOR: {
                                Columns.RANK: Rank.ONE,
                                Columns.DESCRIPTION: "YELLOW",
                            },
                            QualitativeSiteObservationTypes.ODOR: {
                                Columns.RANK: Rank.ONE,
                                Columns.DESCRIPTION: "SULPHUR",
                            },
                            QualitativeSiteObservationTypes.VISUAL: {
                                Columns.RANK: None,
                                Columns.DESCRIPTION: None,
                            },
                        },
                        {
                            Columns.SITE_ID: "BROADWAY",
                            Columns.BACTERIA_BOTTLE_NO: "B3",
                            Columns.DRY_OUTFALL: False,
                            Columns.ARRIVAL_TIME: "15:09",
                            Columns.FLOW: Flow.M,
                            Columns.FLOW_COMPARED_TO_EXPECTED: FlowComparedToExpected.NORMAL,
                            Columns.AIR_TEMP: 22.0,
                            Columns.WATER_TEMP: 11.1,
                            Columns.DO_MG_PER_L: 10.73,
                            Columns.SPS_MICRO_S_PER_CM: 314.1,
                            Columns.SALINITY_PPT: 0.15,
                            Columns.PH: 7.40,
                            QualitativeSiteObservationTypes.COLOR: {
                                Columns.RANK: Rank.ONE,
                                Columns.DESCRIPTION: "YELLOW",
                            },
                            QualitativeSiteObservationTypes.ODOR: {
                                Columns.RANK: Rank.ONE,
                                Columns.DESCRIPTION: "SULPHUR",
                            },
                            QualitativeSiteObservationTypes.VISUAL: {
                                Columns.RANK: None,
                                Columns.DESCRIPTION: None,
                            },
                        },
                    ],
                },
            },
            "sheet1.jpg": {
                Columns.FORM_TYPE: FormType.FIELD_DATASHEET_FOSS,
                Columns.FORM_VERSION: "4.4-1-29-2025",
                Columns.CITY: "BELLINGHAM",
                Columns.DATE: "2025-04-21",
                Columns.NOTES: "Padden - DO%",
                Columns.INVESTIGATORS: {
                    "ANNA": {Columns.START_TIME: "17:10"},
                    "PAT": {Columns.START_TIME: "17:10"},
                    "CHRIS": {Columns.START_TIME: "17:10"},
                },
                Columns.OBSERVATIONS: {
                    Columns.FIELD: {
                        Columns.TIDE_HEIGHT: 0.22,
                        Columns.TIDE_TIME: "17:10",
                        Columns.PAST_24HR_RAINFALL: None,
                        Columns.WEATHER: Weather.CLOUD_CLEAR,
                    },
                    Columns.SITE: [
                        {
                            Columns.SITE_ID: "PADDEN",
                            Columns.BACTERIA_BOTTLE_NO: "B5",
                            Columns.DRY_OUTFALL: False,
                            Columns.ARRIVAL_TIME: "17:10",
                            Columns.FLOW: Flow.H,
                            Columns.FLOW_COMPARED_TO_EXPECTED: FlowComparedToExpected.NORMAL,
                            Columns.AIR_TEMP: 16,
                            Columns.WATER_TEMP: 11.6,
                            Columns.DO_MG_PER_L: 102.1,
                            Columns.SPS_MICRO_S_PER_CM: 151.0,
                            Columns.SALINITY_PPT: 0.07,
                            Columns.PH: 7.73,
                            QualitativeSiteObservationTypes.COLOR: {
                                Columns.RANK: Rank.ONE,
                                Columns.DESCRIPTION: "TAN",
                            },
                            QualitativeSiteObservationTypes.ODOR: {
                                Columns.RANK: Rank.ZERO,
                                Columns.DESCRIPTION: None,
                            },
                            QualitativeSiteObservationTypes.VISUAL: {
                                Columns.RANK: Rank.ZERO,
                                Columns.DESCRIPTION: None,
                            },
                        },
                        {
                            Columns.SITE_ID: "BENASFASDF",
                            Columns.BACTERIA_BOTTLE_NO: "B6",
                            Columns.DRY_OUTFALL: False,
                            Columns.ARRIVAL_TIME: "17:33",
                            Columns.FLOW: Flow.H,
                            Columns.FLOW_COMPARED_TO_EXPECTED: FlowComparedToExpected.NORMAL,
                            Columns.AIR_TEMP: 18,
                            Columns.WATER_TEMP: 11.4,
                            Columns.DO_MG_PER_L: 11.03,
                            Columns.SPS_MICRO_S_PER_CM: 234.7,
                            Columns.SALINITY_PPT: 0.11,
                            Columns.PH: 7.87,
                            QualitativeSiteObservationTypes.COLOR: {
                                Columns.RANK: Rank.ONE,
                                Columns.DESCRIPTION: "Tan/brown",
                            },
                            QualitativeSiteObservationTypes.ODOR: {
                                Columns.RANK: None,
                                Columns.DESCRIPTION: None,
                            },
                            QualitativeSiteObservationTypes.VISUAL: {
                                Columns.RANK: None,
                                Columns.DESCRIPTION: None,
                            },
                        },
                        {
                            Columns.SITE_ID: "BEPSODF72",
                            Columns.BACTERIA_BOTTLE_NO: "B7",
                            Columns.DRY_OUTFALL: False,
                            Columns.ARRIVAL_TIME: "17:40",
                            Columns.FLOW: Flow.H,
                            Columns.FLOW_COMPARED_TO_EXPECTED: FlowComparedToExpected.NORMAL,
                            Columns.AIR_TEMP: None,
                            Columns.WATER_TEMP: 11.4,
                            Columns.DO_MG_PER_L: 11.17,
                            Columns.SPS_MICRO_S_PER_CM: 235.1,
                            Columns.SALINITY_PPT: 0.11,
                            Columns.PH: 7.82,
                            QualitativeSiteObservationTypes.COLOR: {
                                Columns.RANK: Rank.ONE,
                                Columns.DESCRIPTION: "Brown",
                            },
                            QualitativeSiteObservationTypes.ODOR: {
                                Columns.RANK: None,
                                Columns.DESCRIPTION: None,
                            },
                            QualitativeSiteObservationTypes.VISUAL: {
                                Columns.RANK: None,
                                Columns.DESCRIPTION: None,
                            },
                        },
                    ],
                },
            },
        },
    },
}
