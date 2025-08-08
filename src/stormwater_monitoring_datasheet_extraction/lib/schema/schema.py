"""Pandera schemas for ETL steps."""

from functools import partial
from typing import Callable, Final

import pandera as pa
from pandera.typing import Series

from stormwater_monitoring_datasheet_extraction.lib.constants import (
    CharLimits,
    City,
    Columns,
    Flow,
    FlowComparedToExpected,
    FormType,
    QualitativeSiteObservationTypes,
    Rank,
    Weather,
)
from stormwater_monitoring_datasheet_extraction.lib.schema import checks  # noqa: F401

# TODO: Set field-level checks.
# See/use field_datasheet_data_definition.json metadata.
# TODO: Set dataframe-level checks.
# See/use field_datasheet_data_definition.json metadata.
# NOTE: Validations should be lax for extraction, stricter after cleaning,
# stricter after user verification, and strictest after final cleaning.
# TODO: Implement and use `schema_error_handler` decorator.
# Helps catch/handle schema errors more gracefully.
# 0. Copy `schema_error_handler` from `bfb_delivery`.
# https://github.com/crickets-and-comb/bfb_delivery/blob/main/src/bfb_delivery/lib/schema/utils.py#L8
# https://github.com/crickets-and-comb/bfb_delivery/blob/main/src/bfb_delivery/lib/dispatch/write_to_circuit.py#L111
# 1. Move from `bfb_delivery` to `comb_utils`.
# 2. Add feature to pass in custom error handler function,
# with default that uses generally useful DataFrameModel error features.

_COERCE_FIELD: Final[Callable] = partial(pa.Field, coerce=True)
_LAX_FIELD: Final[Callable] = partial(pa.Field, coerce=False, unique=False, nullable=True)
_NULLABLE_FIELD: Final[Callable] = partial(_COERCE_FIELD, nullable=True)
_UNIQUE_FIELD: Final[Callable] = partial(_COERCE_FIELD, unique=True)


# Form metadata.
# NOTE: `form_id` is typically going to be image file name, e.g. "2025-07-22_14-41-00.jpg".
# If all files are from the same directory in a single extraction, then it will be unique.
# But, that doesn't guarantee uniqueness across multiple extractions to the same DB.
FORM_ID_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.FORM_ID)
FORM_ID_FIELD_UNQ: Final[Callable] = partial(_UNIQUE_FIELD, alias=Columns.FORM_ID)
FORM_TYPE_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.FORM_TYPE)
FORM_TYPE_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.FORM_TYPE)
FORM_VERSION_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.FORM_VERSION)
FORM_VERSION_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.FORM_VERSION)
CITY_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.CITY)
CITY_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.CITY)
DATE_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.DATE)
DATE_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.DATE)
NOTES_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.NOTES)
NOTES_FIELD: Final[Callable] = partial(_NULLABLE_FIELD, alias=Columns.NOTES)

# Form metadata: Field observations.
TIDE_HEIGHT_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.TIDE_HEIGHT)
TIDE_HEIGHT_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.TIDE_HEIGHT)
TIDE_TIME_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.TIDE_TIME)
TIDE_TIME_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.TIDE_TIME)
PAST_24HR_RAINFALL_FIELD_LAX: Final[Callable] = partial(
    _LAX_FIELD, alias=Columns.PAST_24HR_RAINFALL
)
PAST_24HR_RAINFALL_FIELD: Final[Callable] = partial(
    _COERCE_FIELD, alias=Columns.PAST_24HR_RAINFALL
)
WEATHER_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.WEATHER)
WEATHER_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.WEATHER)

# Investigators.
INVESTIGATOR_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.INVESTIGATOR)
INVESTIGATOR_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.INVESTIGATOR)
START_TIME_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.START_TIME)
START_TIME_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.START_TIME)
END_TIME_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.END_TIME)
END_TIME_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.END_TIME)

# Site observations.
SITE_ID_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.SITE_ID)
SITE_ID_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.SITE_ID)
BOTTLE_NO_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.BACTERIA_BOTTLE_NO)
BOTTLE_NO_FIELD: Final[Callable] = partial(_NULLABLE_FIELD, alias=Columns.BACTERIA_BOTTLE_NO)
DRY_OUTFALL_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.DRY_OUTFALL)
DRY_OUTFALL_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.DRY_OUTFALL)
ARRIVAL_TIME_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.ARRIVAL_TIME)
ARRIVAL_TIME_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.ARRIVAL_TIME)
FLOW_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.FLOW)
FLOW_FIELD: Final[Callable] = partial(_NULLABLE_FIELD, alias=Columns.FLOW)
FLOW_COMPARED_TO_EXPECTED_FIELD_LAX: Final[Callable] = partial(
    _LAX_FIELD, alias=Columns.FLOW_COMPARED_TO_EXPECTED
)
FLOW_COMPARED_TO_EXPECTED_FIELD: Final[Callable] = partial(
    _NULLABLE_FIELD, alias=Columns.FLOW_COMPARED_TO_EXPECTED
)
AIR_TEMP_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.AIR_TEMP)
AIR_TEMP_FIELD: Final[Callable] = partial(_NULLABLE_FIELD, alias=Columns.AIR_TEMP)
WATER_TEMP_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.WATER_TEMP)
WATER_TEMP_FIELD: Final[Callable] = partial(_NULLABLE_FIELD, alias=Columns.WATER_TEMP)
DO_MG_PER_L_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.DO_MG_PER_L)
DO_MG_PER_L_FIELD: Final[Callable] = partial(_NULLABLE_FIELD, alias=Columns.DO_MG_PER_L)
SPS_MICRO_S_PER_CM_FIELD_LAX: Final[Callable] = partial(
    _LAX_FIELD, alias=Columns.SPS_MICRO_S_PER_CM
)
SPS_MICRO_S_PER_CM_FIELD: Final[Callable] = partial(
    _NULLABLE_FIELD, alias=Columns.SPS_MICRO_S_PER_CM
)
SALINITY_PPT_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.SALINITY_PPT)
SALINITY_PPT_FIELD: Final[Callable] = partial(_NULLABLE_FIELD, alias=Columns.SALINITY_PPT)
PH_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.PH)
PH_FIELD: Final[Callable] = partial(_NULLABLE_FIELD, alias=Columns.PH)

# Qualitative site observations: color, odor, visual.
OBSERVATION_TYPE_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.OBSERVATION_TYPE)
OBSERVATION_TYPE: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.OBSERVATION_TYPE)
RANK_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.RANK)
RANK_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.RANK)
DESCRIPTION_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.DESCRIPTION)
DESCRIPTION_FIELD: Final[Callable] = partial(
    _COERCE_FIELD,
    alias=Columns.DESCRIPTION,
    str_length={"max_value": CharLimits.DESCRIPTION},
)


class FormMetadataExtracted(pa.DataFrameModel):
    """Schema for the form metadata extracted from the datasheets.

    PK: `form_id`.
    """

    #: The form ID, sole primary key.
    form_id: Series[str] = FORM_ID_FIELD_UNQ()
    #: The form type. Nullable. Unenforced `FormType`.
    form_type: Series[str] = FORM_TYPE_FIELD_LAX()
    #: The form version. Nullable.
    form_version: Series[str] = FORM_VERSION_FIELD_LAX()
    #: The date of observations. Nullable.
    date: Series[str] = DATE_FIELD_LAX()
    #: The city of observations. Nullable. Unenforced `City`.
    city: Series[str] = CITY_FIELD_LAX()
    #: The tide height at the time of observations. Nullable.
    tide_height: Series[float] = TIDE_HEIGHT_FIELD_LAX()
    #: The tide time at the time of observations. Nullable.
    tide_time: Series[str] = TIDE_TIME_FIELD_LAX()
    #: The past 24-hour rainfall. Nullable.
    past_24hr_rainfall: Series[float] = PAST_24HR_RAINFALL_FIELD_LAX()
    #: The weather at the time of observations. Nullable. Unenforced `Weather`.
    weather: Series[str] = WEATHER_FIELD_LAX()
    #: Investigator notes. Nullable.
    notes: Series[str] = NOTES_FIELD_LAX()

    class Config:
        """The configuration for the schema.

        Not a strict schema at this stage since it's the "raw" extracted data.

        We do enforce the primary key since it's created by the extraction process.
        """

        strict = False

        # Dataframe checks.
        # NOTE: Redundant to `FORM_ID_FIELD_UNQ` but included for clarity.
        pk_check = {"pk_cols": [Columns.FORM_ID]}


class InvestigatorsExtracted(pa.DataFrameModel):
    """Schema for the investigators extracted from the datasheets.

    PK: `form_id`, `investigator` (unenforced).
    FK: `FormMetadata.form_id` (unenforced).
    """

    #: The form ID, part of the primary key, foreign key to `FormMetadataExtracted.form_id`.
    form_id: Series[str] = FORM_ID_FIELD()
    #: The investigator, part of the primary key, but nullable at this stage.
    investigator: Series[str] = INVESTIGATOR_FIELD_LAX()
    #: The start time of the investigation. Nullable.
    start_time: Series[str] = START_TIME_FIELD_LAX()
    #: The end time of the investigation. Nullable.
    end_time: Series[str] = END_TIME_FIELD_LAX()

    class Config:
        """The configuration for the schema.

        Not a strict schema at this stage since it's the "raw" extracted data.
        """

        strict = False


class SiteObservationsExtracted(pa.DataFrameModel):
    """Schema for the observations precleaned.

    PK: `form_id`, `site_id` (unenforced).
    FK: `FormMetadata.form_id` (unenforced).
    FK: ?.`bottle_no` (unenforced).
    """

    #: The form ID, part of the primary key, foreign key to `FormMetadataExtracted.form_id`.
    form_id: Series[str] = FORM_ID_FIELD()
    #: The site ID, part of the primary key, but nullable at this stage.
    site_id: Series[str] = SITE_ID_FIELD_LAX()
    #: The bottle number. Nullable.
    bottle_no: Series[str] = BOTTLE_NO_FIELD_LAX()
    #: Whether the outfall was dry. Nullable.
    dry_outfall: Series[bool] = DRY_OUTFALL_FIELD_LAX()
    #: The arrival time of the investigation. Nullable.
    arrival_time: Series[str] = ARRIVAL_TIME_FIELD_LAX()
    #: The flow. Nullable. Unenforced `Flow`.
    flow: Series[str] = FLOW_FIELD_LAX()
    #: The flow compared to expected. Nullable. Unenforced `FlowComparedToExpected`.
    flow_compared_to_expected: Series[str] = FLOW_COMPARED_TO_EXPECTED_FIELD_LAX()
    #: The air temperature. Nullable.
    air_temp: Series[float] = AIR_TEMP_FIELD_LAX()
    #: The water temperature. Nullable.
    water_temp: Series[float] = WATER_TEMP_FIELD_LAX()
    #: The dissolved oxygen. Nullable.
    DO_mg_per_l: Series[float] = DO_MG_PER_L_FIELD_LAX()
    #: The specific conductance. Nullable.
    SPS_micro_S_per_cm: Series[float] = SPS_MICRO_S_PER_CM_FIELD_LAX()
    #: The salinity. Nullable.
    salinity_ppt: Series[float] = SALINITY_PPT_FIELD_LAX()
    #: The pH. Nullable.
    pH: Series[float] = PH_FIELD_LAX()

    class Config:
        """The configuration for the schema.

        Not a strict schema at this stage since it's the "raw" extracted data.
        """

        strict = False


class QualitativeSiteObservationsExtracted(pa.DataFrameModel):
    """Schema for the qualitative site observations extracted from the datasheets.

    PK: `form_id`, `site_id` (unenforced).
    FK: `FormMetadata.form_id` (unenforced).
    """

    # TODO: Type should be part of the PK.
    #: The form ID, part of the primary key, foreign key to `FormMetadataExtracted.form_id`.
    form_id: Series[str] = FORM_ID_FIELD()
    #: The site ID, part of the primary key, but nullable at this stage.
    site_id: Series[str] = SITE_ID_FIELD_LAX()
    #: The observation type. Nullable. Unenforced `QualitativeSiteObservationTypes`.
    type: Series[str] = OBSERVATION_TYPE_LAX()
    #: The rank of the observation. Nullable. Unenforced `Rank`.
    rank: Series[int] = RANK_FIELD_LAX()
    #: The description of the observation. Nullable.
    description: Series[str] = DESCRIPTION_FIELD_LAX()

    class Config:
        """The configuration for the schema.

        Not a strict schema at this stage since it's the "raw" extracted data.
        """

        strict = False


class FormMetadataPrecleaned(FormMetadataExtracted):
    """Schema for the form metadata precleaned.

    PK: `form_id`.
    """

    class Config:
        """The configuration for the schema.

        A strict schema, requires all fields to be present.
        """

        strict = True


class InvestigatorsPrecleaned(InvestigatorsExtracted):
    """Schema for the investigators precleaned.

    PK: `form_id`, `investigator` (unenforced).
    FK: `FormMetadata.form_id` (unenforced).
    """

    class Config:
        """The configuration for the schema.

        A strict schema, requires all fields to be present.
        """

        strict = True


class SiteObservationsPrecleaned(SiteObservationsExtracted):
    """Schema for the observations extracted from the datasheets.

    PK: `form_id`, `site_id` (unenforced).
    FK: `FormMetadata.form_id` (unenforced).
    FK: ?.`bottle_no` (unenforced).
    """

    class Config:
        """The configuration for the schema.

        A strict schema, requires all fields to be present.
        """

        strict = True


class QualitativeSiteObservationsPrecleaned(QualitativeSiteObservationsExtracted):
    """Schema for the qualitative site observations precleaned.

    PK: `form_id`, `site_id` (unenforced).
    FK: `FormMetadata.form_id` (unenforced).
    """

    class Config:
        """The configuration for the schema.

        A strict schema, requires all fields to be present.
        """

        strict = True


class FormMetadataVerified(FormMetadataPrecleaned):
    """Schema for the form metadata verified by the user.

    PK: `form_id`.
    """

    # TODO: If fields are not coerced before this, can't we still type them as their enums?
    #: The form type.
    form_type: Series[FormType] = FORM_TYPE_FIELD()
    #: The form version.
    form_version: Series[str] = FORM_VERSION_FIELD()
    #: The date of observations.
    date: Series[str] = DATE_FIELD()
    #: The city of observations.
    city: Series[City] = CITY_FIELD()
    #: The tide height at the time of observations.
    tide_height: Series[float] = TIDE_HEIGHT_FIELD()
    #: The tide time at the time of observations.
    tide_time: Series[str] = TIDE_TIME_FIELD()
    #: The past 24-hour rainfall.
    past_24hr_rainfall: Series[float] = PAST_24HR_RAINFALL_FIELD()
    #: The weather at the time of observations.
    weather: Series[Weather] = WEATHER_FIELD()
    #: Investigator notes.
    notes: Series[str] = NOTES_FIELD()

    class Config:
        """The configuration for the schema."""

        # Field checks.
        # TODO: Field checks:
        # - Date is formatted and valid. (Make a class for this?)
        # - Time is formatted and valid. (Make a class for this?)
        # - Rainfall is positive. (Extant class/type?)


class InvestigatorsVerified(InvestigatorsPrecleaned):
    """Schema for the investigators verified by the user.

    PK: `form_id`, `investigator`.
    FK: `FormMetadata.form_id` (unenforced).
    """

    #: The form ID, part of the primary key, foreign key to `FormMetadataExtracted.form_id`.
    form_id: Series[str] = FORM_ID_FIELD()
    #: The investigator, part of the primary key.
    investigator: Series[str] = INVESTIGATOR_FIELD()
    #: The start time of the investigation.
    start_time: Series[str] = START_TIME_FIELD()
    #: The end time of the investigation.
    end_time: Series[str] = END_TIME_FIELD()

    class Config:
        """The configuration for the schema.

        Enforces the primary key.
        """

        # Dataframe checks.
        pk_check = {"pk_cols": [Columns.FORM_ID, Columns.INVESTIGATOR]}

        # TODO: Field checks:
        # - Start time is formatted and valid. (Make a class for this?)
        # - End time is formatted and valid. (Make a class for this?)

        # TODO: Dataframe checks:
        # - Start time is before end time.


class SiteObservationsVerified(SiteObservationsPrecleaned):
    """Schema for the observations verified by the user.

    PK: `form_id`, `site_id`.
    FK: `FormMetadata.form_id` (unenforced).
    FK: ?.`bottle_no` (unenforced).
    """

    #: The form ID, part of the primary key, foreign key to `FormMetadataExtracted.form_id`.
    form_id: Series[str] = FORM_ID_FIELD()
    #: The site ID, part of the primary key.
    site_id: Series[str] = SITE_ID_FIELD()
    #: Whether the outfall was dry.
    dry_outfall: Series[bool] = DRY_OUTFALL_FIELD()
    #: The bottle number. Nullable, but only if `dry_outfall` is true.
    bottle_no: Series[str] = BOTTLE_NO_FIELD()
    #: The arrival time of the investigation.
    arrival_time: Series[str] = ARRIVAL_TIME_FIELD()
    #: The flow. Nullable, but only if `dry_outfall` is false.
    flow: Series[Flow] = FLOW_FIELD()
    #: The flow compared to expected. Nullable, but only if `dry_outfall` is false.
    flow_compared_to_expected: Series[FlowComparedToExpected] = (
        FLOW_COMPARED_TO_EXPECTED_FIELD()
    )
    #: The air temperature. Nullable, but only if `dry_outfall` is false.
    air_temp: Series[float] = AIR_TEMP_FIELD()
    #: The water temperature. Nullable, but only if `dry_outfall` is false.
    water_temp: Series[float] = WATER_TEMP_FIELD()
    #: The dissolved oxygen. Nullable, but only if `dry_outfall` is false.
    DO_mg_per_l: Series[float] = DO_MG_PER_L_FIELD()
    #: The specific conductance. Nullable, but only if `dry_outfall` is false.
    SPS_micro_S_per_cm: Series[float] = SPS_MICRO_S_PER_CM_FIELD()
    #: The salinity. Nullable, but only if `dry_outfall` is false.
    salinity_ppt: Series[float] = SALINITY_PPT_FIELD()
    #: The pH. Nullable, but only if `dry_outfall` is false.
    pH: Series[float] = PH_FIELD()

    class Config:
        """The configuration for the schema.

        Enforces the primary key.
        """

        # Dataframe checks.
        pk_check = {"pk_cols": [Columns.FORM_ID, Columns.SITE_ID]}

        # TODO: To check threshholds, need a site-type map:
        # creek or outfall, and if creek:
        # habitat, spawn, rear, or migrate.

        # TODO: Dataframe checks:
        # - `bottle_no` should be unique by `form_id`, if not overall.
        # - If dry outfall is true, then observations should be null.
        # - Otherwise, observations should be non-null (unless all null).
        # - Time should be formatted and valid. (Make a class for this?)
        # - Positives: DO_mg_per_l, SPS_micro_S_per_cm, salinity_ppt, pH.


class QualitativeSiteObservationsVerified(QualitativeSiteObservationsPrecleaned):
    """Schema for the qualitative site observations verified by the user.

    PK: `form_id`, `site_id`.
    FK: `FormMetadata.form_id` (unenforced).
    """

    #: The form ID, part of the primary key, foreign key to `FormMetadataExtracted.form_id`.
    form_id: Series[str] = FORM_ID_FIELD()
    #: The site ID, part of the primary key.
    site_id: Series[str] = SITE_ID_FIELD()
    #: The observation type.
    type: Series[QualitativeSiteObservationTypes] = OBSERVATION_TYPE()
    #: The rank of the observation.
    rank: Series[Rank] = RANK_FIELD()
    #: The description of the observation.
    description: Series[str] = DESCRIPTION_FIELD()

    class Config:
        """The configuration for the schema.

        Enforces the primary key.
        """

        # Dataframe checks.
        pk_check = {"pk_cols": [Columns.FORM_ID, Columns.SITE_ID]}


class FormMetadataCleaned(FormMetadataVerified):
    """Schema for the form metadata cleaned.

    PK: `form_id`.
    """


class InvestigatorsCleaned(InvestigatorsVerified):
    """Schema for the investigators cleaned.

    PK: `form_id`, `investigator`.
    FK: `FormMetadata.form_id` (unenforced).
    """


class SiteObservationsCleaned(SiteObservationsVerified):
    """Schema for the observations cleaned.

    PK: `form_id`, `site_id`.
    FK: `FormMetadata.form_id` (unenforced).
    FK: ?.`bottle_no` (unenforced).
    """


class QualitativeSiteObservationsCleaned(QualitativeSiteObservationsVerified):
    """Schema for the qualitative site observations cleaned.

    PK: `form_id`, `site_id` (unenforced).
    FK: `FormMetadata.form_id` (unenforced).
    """
