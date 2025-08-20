"""Pandera schemas for ETL steps."""

from collections.abc import Callable
from functools import partial
from typing import Annotated, Final

import pandas as pd
import pandera as pa
from pandera.typing import Index, Series

from stormwater_monitoring_datasheet_extraction.lib import constants
from stormwater_monitoring_datasheet_extraction.lib.schema import checks  # noqa: F401

# TODO: Set field-level checks.
# See/use field_datasheet_data_definition.json metadata.
# - Replace registered checks with class methods with `@pa.check`:
#   https://pandera.readthedocs.io/en/v0.22.1/dataframe_models.html#column-index-checks
# - Replace dataframe checks with class methods with `@pa.dataframe_check`:
#   https://pandera.readthedocs.io/en/v0.22.1/dataframe_models.html#dataframe-checks
# TODO: Set dataframe-level checks.
# See/use field_datasheet_data_definition.json metadata.
# NOTE: Validations should be lax for extraction, stricter after cleaning,
# stricter after user verification, and strictest after final cleaning.
# TODO: Use `schema_error_handler` decorator.
# Helps catch/handle schema errors more gracefully.
# 0. Copy `schema_error_handler` from `bfb_delivery`.
# https://github.com/crickets-and-comb/bfb_delivery/blob/main/src/bfb_delivery/lib/schema/utils.py#L8
# https://github.com/crickets-and-comb/bfb_delivery/blob/main/src/bfb_delivery/lib/dispatch/write_to_circuit.py#L111
# 1. Move from `bfb_delivery` to `comb_utils` and replace with imports.
# 2. Add feature to pass in custom error handler function,
# with default that uses generally useful DataFrameModel error features.

_LAX_KWARGS: Final[dict] = {
    "coerce": False,
    "nullable": True,
    "raise_warning": True,
    "unique": False,
}
_NULLABLE_KWARGS: Final[dict] = {"coerce": True, "nullable": True}


# Form metadata.
# NOTE: `form_id` is typically going to be image file name, e.g. "2025-07-22_14-41-00.jpg".
# If all files are from the same directory in a single extraction, then it will be unique.
# But, that doesn't guarantee uniqueness across multiple extractions to the same DB.
FORM_ID_FIELD: Final[Callable] = partial(
    pa.Field,
    alias=constants.Columns.FORM_ID,
    coerce=True,
    n_failure_cases=constants.N_FAILURE_CASES,
)
_FORM_TYPE_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.FORM_TYPE, n_failure_cases=constants.N_FAILURE_CASES
)
_FORM_VERSION_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.FORM_VERSION, n_failure_cases=constants.N_FAILURE_CASES
)
_CITY_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.CITY, n_failure_cases=constants.N_FAILURE_CASES
)
_DATE_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.DATE, n_failure_cases=constants.N_FAILURE_CASES
)
_NOTES_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.NOTES, n_failure_cases=constants.N_FAILURE_CASES
)

# Form metadata: Field observations.
_TIDE_HEIGHT_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.TIDE_HEIGHT, n_failure_cases=constants.N_FAILURE_CASES
)
_TIDE_TIME_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.TIDE_TIME, n_failure_cases=constants.N_FAILURE_CASES
)
_PAST_24HR_RAINFALL_FIELD: Final[Callable] = partial(
    pa.Field,
    alias=constants.Columns.PAST_24HR_RAINFALL,
    n_failure_cases=constants.N_FAILURE_CASES,
)
_WEATHER_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.WEATHER, n_failure_cases=constants.N_FAILURE_CASES
)

# Investigators.
_INVESTIGATOR_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.INVESTIGATOR, n_failure_cases=constants.N_FAILURE_CASES
)
_START_TIME_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.START_TIME, n_failure_cases=constants.N_FAILURE_CASES
)
_END_TIME_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.END_TIME, n_failure_cases=constants.N_FAILURE_CASES
)

# Site observations.
_SITE_ID_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.SITE_ID, n_failure_cases=constants.N_FAILURE_CASES
)
SITE_ID_FIELD_LAX: Final[Callable] = partial(_SITE_ID_FIELD, **_LAX_KWARGS)
SITE_ID_FIELD: Final[Callable] = partial(
    _SITE_ID_FIELD, coerce=True, n_failure_cases=constants.N_FAILURE_CASES
)
_BOTTLE_NO_FIELD: Final[Callable] = partial(
    pa.Field,
    alias=constants.Columns.BACTERIA_BOTTLE_NO,
    n_failure_cases=constants.N_FAILURE_CASES,
)
_DRY_OUTFALL_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.DRY_OUTFALL, n_failure_cases=constants.N_FAILURE_CASES
)
_ARRIVAL_TIME_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.ARRIVAL_TIME, n_failure_cases=constants.N_FAILURE_CASES
)
_FLOW_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.FLOW, n_failure_cases=constants.N_FAILURE_CASES
)
_FLOW_COMPARED_TO_EXPECTED_FIELD: Final[Callable] = partial(
    pa.Field,
    alias=constants.Columns.FLOW_COMPARED_TO_EXPECTED,
    n_failure_cases=constants.N_FAILURE_CASES,
)
_AIR_TEMP_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.AIR_TEMP, n_failure_cases=constants.N_FAILURE_CASES
)
_WATER_TEMP_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.WATER_TEMP, n_failure_cases=constants.N_FAILURE_CASES
)
_DO_MG_PER_L_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.DO_MG_PER_L, n_failure_cases=constants.N_FAILURE_CASES
)
_SPS_MICRO_S_PER_CM_FIELD: Final[Callable] = partial(
    pa.Field,
    alias=constants.Columns.SPS_MICRO_S_PER_CM,
    n_failure_cases=constants.N_FAILURE_CASES,
)
_SALINITY_PPT_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.SALINITY_PPT, n_failure_cases=constants.N_FAILURE_CASES
)
_PH_FIELD: Final[Callable] = partial(pa.Field, alias=constants.Columns.PH)

# Qualitative site observations: color, odor, visual.
_OBSERVATION_TYPE_FIELD: Final[Callable] = partial(
    pa.Field,
    alias=constants.Columns.OBSERVATION_TYPE,
    n_failure_cases=constants.N_FAILURE_CASES,
)
_RANK_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.RANK, n_failure_cases=constants.N_FAILURE_CASES
)
_DESCRIPTION_FIELD: Final[Callable] = partial(
    pa.Field, alias=constants.Columns.DESCRIPTION, n_failure_cases=constants.N_FAILURE_CASES
)


class FormMetadataExtracted(pa.DataFrameModel):
    """Schema for the form metadata extracted from the datasheets.

    PK: `form_id`.
    """

    # TODO: May need to loosen the typehints.
    #: The form ID, sole primary key.
    form_id: Index[str] = partial(FORM_ID_FIELD)
    #: The form type. Nullable. Unenforced `constants.FormType`.
    form_type: Series[constants.FormType] = partial(_FORM_TYPE_FIELD, **_LAX_KWARGS)
    #: The form version. Nullable.
    form_version: Series[str] = partial(_FORM_VERSION_FIELD, **_LAX_KWARGS)
    #: The date of observations. Nullable.
    date: Series[str] = partial(_DATE_FIELD, **_LAX_KWARGS)
    #: The city of observations. Nullable. Unenforced `constants.City`.
    city: Series[constants.City] = partial(_CITY_FIELD, **_LAX_KWARGS)
    #: The tide height at the time of observations. Nullable.
    tide_height: Series[float] = partial(_TIDE_HEIGHT_FIELD, **_LAX_KWARGS)
    #: The tide time at the time of observations. Nullable.
    tide_time: Series[str] = partial(_TIDE_TIME_FIELD, **_LAX_KWARGS)
    #: The past 24-hour rainfall. Nullable.
    past_24hr_rainfall: Series[float] = partial(_PAST_24HR_RAINFALL_FIELD, **_LAX_KWARGS)
    #: The weather at the time of observations. Nullable. Unenforced `constants.Weather`.
    weather: Series[constants.Weather] = partial(_WEATHER_FIELD, **_LAX_KWARGS)
    #: Investigator notes. Nullable.
    notes: Series[str] = partial(_NOTES_FIELD, **_LAX_KWARGS)

    class Config:
        """The configuration for the schema.

        Not a strict schema at this stage since it's the "raw" extracted data.

        We do enforce the primary key since it's created by the extraction process.
        """

        multiindex_strict = False
        multiindex_unique = False
        strict = False


class InvestigatorsExtracted(pa.DataFrameModel):
    """Schema for the investigators extracted from the datasheets.

    PK: `form_id`, `investigator` (unenforced).
    FK: `FormMetadata.form_id` (unenforced).
    """

    #: The form ID, part of the primary key, foreign key to `FormMetadataExtracted.form_id`.
    form_id: Series[str] = FORM_ID_FIELD()
    #: The investigator, part of the primary key, but nullable at this stage.
    investigator: Series[str] = partial(_INVESTIGATOR_FIELD, **_LAX_KWARGS)
    #: The start time of the investigation. Nullable.
    start_time: Series[str] = partial(_START_TIME_FIELD, **_LAX_KWARGS)
    #: The end time of the investigation. Nullable.
    end_time: Series[str] = partial(_END_TIME_FIELD, **_LAX_KWARGS)

    class Config:
        """The configuration for the schema.

        Not a strict schema at this stage since it's the "raw" extracted data.
        """

        multiindex_strict = False
        multiindex_unique = False
        strict = False


class SiteObservationsExtracted(pa.DataFrameModel):
    """Schema for the observations precleaned.

    PK: `form_id`, `site_id` (unenforced).
    FK: `FormMetadata.form_id` (unenforced).
    FK: ?.`bottle_no` (unenforced).
    """

    # TODO: May need to loosen the typehints.
    #: The form ID, part of the primary key, foreign key to `FormMetadataExtracted.form_id`.
    form_id: Index[str] = FORM_ID_FIELD()
    #: The site ID, part of the primary key, but nullable at this stage.
    site_id: Index[str] = SITE_ID_FIELD_LAX()
    #: The bottle number. Nullable.
    bottle_no: Index[str] = partial(_BOTTLE_NO_FIELD, **_LAX_KWARGS)
    #: Whether the outfall was dry. Nullable.
    dry_outfall: Series[bool] = partial(_DRY_OUTFALL_FIELD, **_LAX_KWARGS)
    #: The arrival time of the investigation. Nullable.
    arrival_time: Series[str] = partial(_ARRIVAL_TIME_FIELD, **_LAX_KWARGS)
    #: The flow. Nullable. Unenforced `constants.Flow`.
    flow: Series[constants.Flow] = partial(_FLOW_FIELD, **_LAX_KWARGS)
    #: The flow compared to expected. Nullable. Unenforced `constants.FlowComparedToExpected`.
    flow_compared_to_expected: Series[constants.FlowComparedToExpected] = partial(
        _FLOW_COMPARED_TO_EXPECTED_FIELD, **_LAX_KWARGS
    )
    #: The air temperature. Nullable.
    air_temp: Series[float] = partial(_AIR_TEMP_FIELD, **_LAX_KWARGS)
    #: The water temperature. Nullable.
    water_temp: Series[float] = partial(_WATER_TEMP_FIELD, **_LAX_KWARGS)
    #: The dissolved oxygen. Nullable.
    DO_mg_per_l: Series[float] = partial(_DO_MG_PER_L_FIELD, **_LAX_KWARGS)
    #: The specific conductance. Nullable.
    SPS_micro_S_per_cm: Series[float] = partial(_SPS_MICRO_S_PER_CM_FIELD, **_LAX_KWARGS)
    #: The salinity. Nullable.
    salinity_ppt: Series[float] = partial(_SALINITY_PPT_FIELD, **_LAX_KWARGS)
    #: The pH. Nullable.
    pH: Series[float] = partial(_PH_FIELD, **_LAX_KWARGS)

    class Config:
        """The configuration for the schema.

        Not a strict schema at this stage since it's the "raw" extracted data.
        """

        multiindex_strict = False
        multiindex_unique = False
        strict = False


class QualitativeSiteObservationsExtracted(pa.DataFrameModel):
    """Schema for the qualitative site observations extracted from the datasheets.

    PK: `form_id`, `site_id`, `observation_type` (unenforced).
    FK: `FormMetadata.form_id` (unenforced).
    """

    # TODO: May need to loosen the typehints.
    #: The form ID, part of the primary key, foreign key to `FormMetadataExtracted.form_id`.
    form_id: Index[str] = FORM_ID_FIELD()
    #: The site ID, part of the primary key, but nullable at this stage.
    site_id: Series[str] = SITE_ID_FIELD_LAX()
    #: The observation type. Nullable. Unenforced `constants.QualitativeSiteObservationTypes`.
    type: Series[constants.QualitativeSiteObservationTypes] = partial(
        _OBSERVATION_TYPE_FIELD, **_LAX_KWARGS
    )
    #: The rank of the observation. Nullable. Unenforced `constants.Rank`.
    rank: Series[constants.Rank] = partial(_RANK_FIELD, **_LAX_KWARGS)
    #: The description of the observation. Nullable.
    description: Series[str] = partial(_DESCRIPTION_FIELD, **_LAX_KWARGS)

    class Config:
        """The configuration for the schema.

        Not a strict schema at this stage since it's the "raw" extracted data.
        """

        multiindex_strict = False
        multiindex_unique = False
        strict = False


class FormMetadataPrecleaned(FormMetadataExtracted):
    """Schema for the form metadata precleaned.

    PK: `form_id`.
    """

    class Config:
        """The configuration for the schema.

        A strict schema, requires all fields to be present.
        """

        add_missing_columns = True
        multiindex_strict = "filter"
        multiindex_unique = True
        strict = "filter"


class InvestigatorsPrecleaned(InvestigatorsExtracted):
    """Schema for the investigators precleaned.

    PK: `form_id`, `investigator` (unenforced).
    FK: `FormMetadata.form_id` (unenforced).
    """

    class Config:
        """The configuration for the schema.

        A strict schema, requires all fields to be present.
        """

        add_missing_columns = True
        multiindex_strict = "filter"
        strict = "filter"


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

        add_missing_columns = True
        multiindex_strict = "filter"
        strict = "filter"


class QualitativeSiteObservationsPrecleaned(QualitativeSiteObservationsExtracted):
    """Schema for the qualitative site observations precleaned.

    PK: `form_id`, `site_id`, `observation_type` (unenforced).
    FK: `FormMetadata.form_id` (unenforced).
    """

    class Config:
        """The configuration for the schema.

        A strict schema, requires all fields to be present.
        """

        add_missing_columns = True
        multiindex_strict = "filter"
        strict = "filter"


class FormMetadataVerified(FormMetadataPrecleaned):
    """Schema for the form metadata verified by the user.

    PK: `form_id`.
    """

    #: The form type.
    form_type: Series[Annotated[pd.CategoricalDtype, list(constants.FormType), False]] = (
        partial(_FORM_TYPE_FIELD, coerce=True)
    )
    #: The form version.
    form_version: Series[str] = partial(_FORM_VERSION_FIELD, coerce=True)
    # TODO: Maybe we might as well cast to datetime at this step.
    # date: Series[pa.DateTime] = partial(
    #: The date of observations (must be "YYYY-MM-DD", on or before today).
    date: Series[str] = partial(
        _DATE_FIELD,
        coerce=True,
        is_valid_date={"format": constants.DATE_FORMAT},
        date_le_today={"flag": True},
    )
    #: The city of observations.
    city: Series[Annotated[pd.CategoricalDtype, list(constants.City), False]] = partial(
        _CITY_FIELD, coerce=True
    )
    #: The tide height at the time of observations.
    tide_height: Series[float] = partial(_TIDE_HEIGHT_FIELD, coerce=True)
    #: The tide time at the time of observations.
    tide_time: Series[str] = partial(
        _TIDE_TIME_FIELD,
        coerce=True,
        is_valid_time={"format": constants.TIME_FORMAT},
        time_le_now={"flag": True},
    )
    #: The past 24-hour rainfall.
    past_24hr_rainfall: Series[float] = partial(
        _PAST_24HR_RAINFALL_FIELD, coerce=True, greater_than_or_equal_to={"min_value": 0}
    )
    #: The weather at the time of observations.
    # TODO: Are we going to make weather ordered?
    weather: Series[Annotated[pd.CategoricalDtype, list(constants.Weather), True]] = partial(
        _WEATHER_FIELD, coerce=True
    )
    #: Investigator notes.
    notes: Series[str] = partial(
        _NOTES_FIELD, **_NULLABLE_KWARGS, str_length={"max": constants.CharLimits.NOTES}
    )

    class Config:
        """The configuration for the schema."""

        add_missing_columns = False
        multiindex_strict = True
        strict = True


class InvestigatorsVerified(InvestigatorsPrecleaned):
    """Schema for the investigators verified by the user.

    PK: `form_id`, `investigator`.
    FK: `FormMetadata.form_id` (unenforced).
    """

    #: The form ID, part of the primary key, foreign key to `FormMetadataExtracted.form_id`.
    form_id: Index[str] = FORM_ID_FIELD()
    #: The investigator, part of the primary key.
    investigator: Index[str] = partial(_INVESTIGATOR_FIELD, coerce=True)
    #: The start time of the investigation.
    start_time: Series[str] = partial(_START_TIME_FIELD, coerce=True)
    #: The end time of the investigation.
    end_time: Series[str] = partial(_END_TIME_FIELD, coerce=True)

    class Config:
        """The configuration for the schema.

        Enforces the primary key.
        """

        add_missing_columns = False
        multiindex_strict = True
        multiindex_unique = True
        strict = True

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
    form_id: Index[str] = FORM_ID_FIELD()
    #: The site ID, part of the primary key.
    site_id: Index[str] = SITE_ID_FIELD()
    #: Whether the outfall was dry.
    dry_outfall: Series[bool] = partial(_DRY_OUTFALL_FIELD, coerce=True)
    #: The bottle number. Nullable, but only if `dry_outfall` is true.
    bottle_no: Series[str] = partial(_BOTTLE_NO_FIELD, **_NULLABLE_KWARGS)
    #: The arrival time of the investigation.
    arrival_time: Series[str] = partial(_ARRIVAL_TIME_FIELD, coerce=True)
    #: The flow. Nullable, but only if `dry_outfall` is false.
    flow: Series[Annotated[pd.CategoricalDtype, list(constants.Flow), True]] = partial(
        _FLOW_FIELD, **_NULLABLE_KWARGS
    )
    #: The flow compared to expected. Nullable, but only if `dry_outfall` is false.
    flow_compared_to_expected: Series[
        Annotated[pd.CategoricalDtype, list(constants.FlowComparedToExpected), True]
    ] = partial(_FLOW_COMPARED_TO_EXPECTED_FIELD, **_NULLABLE_KWARGS)
    #: The air temperature. Nullable, but only if `dry_outfall` is false.
    air_temp: Series[float] = partial(_AIR_TEMP_FIELD, **_NULLABLE_KWARGS)
    #: The water temperature. Nullable, but only if `dry_outfall` is false.
    water_temp: Series[float] = partial(_WATER_TEMP_FIELD, **_NULLABLE_KWARGS)
    #: The dissolved oxygen. Nullable, but only if `dry_outfall` is false.
    DO_mg_per_l: Series[float] = partial(_DO_MG_PER_L_FIELD, **_NULLABLE_KWARGS)
    #: The specific conductance. Nullable, but only if `dry_outfall` is false.
    SPS_micro_S_per_cm: Series[float] = partial(_SPS_MICRO_S_PER_CM_FIELD, **_NULLABLE_KWARGS)
    #: The salinity. Nullable, but only if `dry_outfall` is false.
    salinity_ppt: Series[float] = partial(_SALINITY_PPT_FIELD, **_NULLABLE_KWARGS)
    #: The pH. Nullable, but only if `dry_outfall` is false.
    pH: Series[float] = partial(_PH_FIELD, **_NULLABLE_KWARGS)

    class Config:
        """The configuration for the schema.

        Enforces the primary key.
        """

        add_missing_columns = False
        multiindex_strict = True
        multiindex_unique = True
        strict = True

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

    PK: `form_id`, `site_id`, `observation_type`.
    FK: `FormMetadata.form_id` (unenforced).
    """

    #: The form ID, part of the primary key, foreign key to `FormMetadataExtracted.form_id`.
    form_id: Index[str] = FORM_ID_FIELD()
    #: The site ID, part of the primary key.
    site_id: Index[str] = SITE_ID_FIELD()
    #: The observation type.
    type: Index[
        Annotated[pd.CategoricalDtype, list(constants.QualitativeSiteObservationTypes), False]
    ] = partial(_OBSERVATION_TYPE_FIELD, coerce=True)
    #: The rank of the observation.
    rank: Series[Annotated[pd.CategoricalDtype, list(constants.Rank), True]] = partial(
        _RANK_FIELD, coerce=True
    )
    #: The description of the observation.
    description: Series[str] = partial(
        _DESCRIPTION_FIELD,
        coerce=True,
        str_length={"max_value": constants.CharLimits.DESCRIPTION},
    )

    class Config:
        """The configuration for the schema.

        Enforces the primary key.
        """

        add_missing_columns = False
        multiindex_strict = True
        multiindex_unique = True
        strict = True


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

    PK: `form_id`, `site_id`, `observation_type`.
    FK: `FormMetadata.form_id` (unenforced).
    """
