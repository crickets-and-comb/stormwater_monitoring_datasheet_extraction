"""Pandera schemas for ETL steps."""

from functools import partial
from typing import Callable, Final

import pandera as pa
from pandera.typing import Series

from stormwater_monitoring_datasheet_extraction.lib.constants import Columns

# TODO: Set field restrictions.
# See/use field_datasheet_data_definition.json metadata.
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
# with default that uses generally useful DataFrameSchema error features.

_COERCE_FIELD: Final[Callable] = partial(pa.Field, coerce=True)
_LAX_FIELD: Final[Callable] = partial(pa.Field, coerce=False, unique=False, nullable=True)
_NULLABLE_FIELD: Final[Callable] = partial(_COERCE_FIELD, nullable=True)
_UNIQUE_FIELD: Final[Callable] = partial(_COERCE_FIELD, unique=True)


# Form metadata.
# NOTE: form_id is typically going to be image file name, e.g. "2025-07-22_14-41-00.jpg".
# If all files are from the same directory in a single extraction, then it will be unique.
# But, that doesn't guarantee uniqueness across multiple extractions to the same DB.
FORM_ID_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.FORM_ID)
FORM_ID_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.FORM_ID)
FORM_ID_FIELD_UNQ: Final[Callable] = partial(_UNIQUE_FIELD, alias=Columns.FORM_ID)
# NOTE: We can add form_type and form_version when we add other forms.
# May need to add dataframe checks at that point, or create new schema,
# or completely refactor how we handle the data.
CITY_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.CITY)
CITY_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.CITY)
DATE_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.DATE)
DATE_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.DATE)
NOTES_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.NOTES)
NOTES_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.NOTES)

# Investigators.
INVESTIGATOR_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.INVESTIGATOR)
INVESTIGATOR_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.INVESTIGATOR)
START_TIME_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.START_TIME)
START_TIME_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.START_TIME)
END_TIME_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.END_TIME)
END_TIME_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.END_TIME)

# Field observations.
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

# Site observations.
SITE_ID_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.SITE_ID)
SITE_ID_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.SITE_ID)
BOTTLE_NO_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.BACTERIA_BOTTLE_NO)
BOTTLE_NO_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.BACTERIA_BOTTLE_NO)
DRY_OUTFALL_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.DRY_OUTFALL)
DRY_OUTFALL_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.DRY_OUTFALL)
ARRIVAL_TIME_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.ARRIVAL_TIME)
ARRIVAL_TIME_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.ARRIVAL_TIME)
FLOW_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.FLOW)
FLOW_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.FLOW)
FLOW_COMPARED_TO_EXPECTED_FIELD_LAX: Final[Callable] = partial(
    _LAX_FIELD, alias=Columns.FLOW_COMPARED_TO_EXPECTED
)
FLOW_COMPARED_TO_EXPECTED_FIELD: Final[Callable] = partial(
    _COERCE_FIELD, alias=Columns.FLOW_COMPARED_TO_EXPECTED
)
AIR_TEMP_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.AIR_TEMP)
AIR_TEMP_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.AIR_TEMP)
WATER_TEMP_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.WATER_TEMP)
WATER_TEMP_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.WATER_TEMP)
DO_MG_PER_L_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.DO_MG_PER_L)
DO_MG_PER_L_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.DO_MG_PER_L)
SPS_MICRO_S_PER_CM_FIELD_LAX: Final[Callable] = partial(
    _LAX_FIELD, alias=Columns.SPS_MICRO_S_PER_CM
)
SPS_MICRO_S_PER_CM_FIELD: Final[Callable] = partial(
    _COERCE_FIELD, alias=Columns.SPS_MICRO_S_PER_CM
)
SALINITY_PPT_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.SALINITY_PPT)
SALINITY_PPT_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.SALINITY_PPT)
PH_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.PH)
PH_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.PH)

# Qualitative site observations: color, odor, visual.
TYPE_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.OBSERVATION_TYPE)
TYPE_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.OBSERVATION_TYPE)
RANK_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.RANK)
RANK_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.RANK)
DESCRIPTION_FIELD_LAX: Final[Callable] = partial(_LAX_FIELD, alias=Columns.DESCRIPTION)
DESCRIPTION_FIELD: Final[Callable] = partial(_COERCE_FIELD, alias=Columns.DESCRIPTION)


class FormMetadataExtracted(pa.DataFrameSchema):
    """Schema for the form metadata extracted from the datasheets."""

    form_id: Series[str] = FORM_ID_FIELD_LAX()
    city: Series[str] = CITY_FIELD_LAX()
    date: Series[str] = DATE_FIELD_LAX()
    notes: Series[str] = NOTES_FIELD_LAX()

    class Config:
        """The configuration for the schema."""

        strict = False


class InvestigatorsExtracted(pa.DataFrameSchema):
    """Schema for the investigators extracted from the datasheets."""

    form_id: Series[str] = FORM_ID_FIELD_LAX()
    investigator: Series[str] = INVESTIGATOR_FIELD_LAX()
    start_time: Series[str] = START_TIME_FIELD_LAX()
    end_time: Series[str] = END_TIME_FIELD_LAX()

    class Config:
        """The configuration for the schema."""

        strict = False


class FieldObservationsExtracted(pa.DataFrameSchema):
    """Schema for the observations precleaned."""

    form_id: Series[str] = FORM_ID_FIELD_LAX()
    tide_height: Series[float] = TIDE_HEIGHT_FIELD_LAX()
    tide_time: Series[str] = TIDE_TIME_FIELD_LAX()
    past_24hr_rainfall: Series[float] = PAST_24HR_RAINFALL_FIELD_LAX()
    weather: Series[str] = WEATHER_FIELD_LAX()

    class Config:
        """The configuration for the schema."""

        strict = False


class SiteObservationsExtracted(pa.DataFrameSchema):
    """Schema for the observations precleaned."""

    form_id: Series[str] = FORM_ID_FIELD_LAX()
    bottle_no: Series[str] = BOTTLE_NO_FIELD_LAX()
    dry_outfall: Series[bool] = DRY_OUTFALL_FIELD_LAX()
    arrival_time: Series[str] = ARRIVAL_TIME_FIELD_LAX()
    flow: Series[str] = FLOW_FIELD_LAX()
    flow_compared_to_expected: Series[str] = FLOW_COMPARED_TO_EXPECTED_FIELD_LAX()
    air_temp: Series[float] = AIR_TEMP_FIELD_LAX()
    water_temp: Series[float] = WATER_TEMP_FIELD_LAX()
    DO_mg_per_l: Series[float] = DO_MG_PER_L_FIELD_LAX()
    SPS_micro_S_per_cm: Series[float] = SPS_MICRO_S_PER_CM_FIELD_LAX()
    salinity_ppt: Series[float] = SALINITY_PPT_FIELD_LAX()
    pH: Series[float] = PH_FIELD_LAX()

    class Config:
        """The configuration for the schema."""

        strict = False


class QualitativeSiteObservationsExtracted(pa.DataFrameSchema):
    """Schema for the qualitative site observations extracted from the datasheets."""

    form_id: Series[str] = FORM_ID_FIELD_LAX()
    bottle_no: Series[str] = BOTTLE_NO_FIELD_LAX()
    color: Series[str] = TYPE_FIELD_LAX()
    odor: Series[str] = TYPE_FIELD_LAX()
    visual: Series[str] = TYPE_FIELD_LAX()

    class Config:
        """The configuration for the schema."""

        strict = False


class FormMetadataPrecleaned(FormMetadataExtracted):
    """Schema for the form metadata precleaned."""

    form_id: Series[str] = FORM_ID_FIELD_UNQ()
    city: Series[str] = CITY_FIELD()
    date: Series[str] = DATE_FIELD()
    notes: Series[str] = NOTES_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


class InvestigatorsPrecleaned(InvestigatorsExtracted):
    """Schema for the investigators precleaned."""

    form_id: Series[str] = FORM_ID_FIELD()
    investigator: Series[str] = INVESTIGATOR_FIELD()
    start_time: Series[str] = START_TIME_FIELD()
    end_time: Series[str] = END_TIME_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


class FieldObservationsPrecleaned(FieldObservationsExtracted):
    """Schema for the observations extracted from the datasheets."""

    form_id: Series[str] = FORM_ID_FIELD()
    tide_height: Series[float] = TIDE_HEIGHT_FIELD()
    tide_time: Series[str] = TIDE_TIME_FIELD()
    past_24hr_rainfall: Series[float] = PAST_24HR_RAINFALL_FIELD()
    weather: Series[str] = WEATHER_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


class SiteObservationsPrecleaned(SiteObservationsExtracted):
    """Schema for the observations extracted from the datasheets."""

    form_id: Series[str] = FORM_ID_FIELD()
    bottle_no: Series[str] = BOTTLE_NO_FIELD()
    dry_outfall: Series[bool] = DRY_OUTFALL_FIELD()
    arrival_time: Series[str] = ARRIVAL_TIME_FIELD()
    flow: Series[str] = FLOW_FIELD()
    flow_compared_to_expected: Series[str] = FLOW_COMPARED_TO_EXPECTED_FIELD()
    air_temp: Series[float] = AIR_TEMP_FIELD()
    water_temp: Series[float] = WATER_TEMP_FIELD()
    DO_mg_per_l: Series[float] = DO_MG_PER_L_FIELD()
    SPS_micro_S_per_cm: Series[float] = SPS_MICRO_S_PER_CM_FIELD()
    salinity_ppt: Series[float] = SALINITY_PPT_FIELD()
    pH: Series[float] = PH_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


class QualitativeSiteObservationsPrecleaned(QualitativeSiteObservationsExtracted):
    """Schema for the qualitative site observations precleaned."""

    form_id: Series[str] = FORM_ID_FIELD()
    bottle_no: Series[str] = BOTTLE_NO_FIELD()
    color: Series[str] = TYPE_FIELD()
    odor: Series[str] = TYPE_FIELD()
    visual: Series[str] = TYPE_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


class FormMetadataVerified(FormMetadataPrecleaned):
    """Schema for the form metadata verified by the user."""


class InvestigatorsVerified(InvestigatorsPrecleaned):
    """Schema for the investigators verified by the user."""


class FieldObservationsVerified(FieldObservationsPrecleaned):
    """Schema for the observations verified by the user."""


class SiteObservationsVerified(SiteObservationsPrecleaned):
    """Schema for the observations verified by the user."""


class QualitativeSiteObservationsVerified(QualitativeSiteObservationsPrecleaned):
    """Schema for the qualitative site observations verified by the user."""


class FormMetadataCleaned(FormMetadataVerified):
    """Schema for the form metadata cleaned."""


class InvestigatorsCleaned(InvestigatorsVerified):
    """Schema for the investigators cleaned."""


class FieldObservationsCleaned(FieldObservationsVerified):
    """Schema for the observations cleaned."""


class SiteObservationsCleaned(SiteObservationsVerified):
    """Schema for the observations cleaned."""


class QualitativeSiteObservationsCleaned(QualitativeSiteObservationsVerified):
    """Schema for the qualitative site observations cleaned."""
