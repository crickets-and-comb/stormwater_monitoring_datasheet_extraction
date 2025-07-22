"""Pandera schemas for ETL steps."""

from functools import partial

import pandera as pa
from pandera.typing import Series

from stormwater_monitoring_datasheet_extraction.lib.constants import Columns

# TODO: Validations should be lax for extraction, stricter after cleaning,
# stricter after user verification, and strictest after final cleaning.
# TODO: Index all to form/image name.

_COERCE_FIELD = partial(pa.Field, coerce=True)
_LAX_FIELD = partial(pa.Field, coerce=False, unique=False, nullable=True)
_NULLABLE_FIELD = partial(_COERCE_FIELD, nullable=True)
_UNIQUE_FIELD = partial(_COERCE_FIELD, unique=True)

# NOTE: We can add form_type and form_version when we add other forms.
# May need to add dataframe checks at that point, or create new schema,
# or completely refactor how we handle the data.
FORM_ID_FIELD_LAX = partial(_LAX_FIELD, alias=Columns.FORM_ID)
FORM_ID_FIELD = partial(_COERCE_FIELD, alias=Columns.FORM_ID)
FORM_ID_FIELD_UNQ = partial(_UNIQUE_FIELD, alias=Columns.FORM_ID)

# Form metadata.
CITY_FIELD_LAX = partial(_LAX_FIELD, alias=Columns.CITY)
CITY_FIELD = partial(_COERCE_FIELD, alias=Columns.CITY)
DATE_FIELD_LAX = partial(_LAX_FIELD, alias=Columns.DATE)
DATE_FIELD = partial(_COERCE_FIELD, alias=Columns.DATE)
NOTES_FIELD_LAX = partial(_LAX_FIELD, alias=Columns.NOTES)
NOTES_FIELD = partial(_COERCE_FIELD, alias=Columns.NOTES)

# Investigators.
INVESTIGATOR_FIELD_LAX = partial(_LAX_FIELD, alias=Columns.INVESTIGATOR)
INVESTIGATOR_FIELD = partial(_COERCE_FIELD, alias=Columns.INVESTIGATOR)
START_TIME_FIELD_LAX = partial(_LAX_FIELD, alias=Columns.START_TIME)
START_TIME_FIELD = partial(_COERCE_FIELD, alias=Columns.START_TIME)
END_TIME_FIELD_LAX = partial(_LAX_FIELD, alias=Columns.END_TIME)
END_TIME_FIELD = partial(_COERCE_FIELD, alias=Columns.END_TIME)

# Field observations.
TIDE_HEIGHT_FIELD_LAX = partial(_LAX_FIELD, alias=Columns.TIDE_HEIGHT)
TIDE_HEIGHT_FIELD = partial(_COERCE_FIELD, alias=Columns.TIDE_HEIGHT)
TIDE_TIME_FIELD_LAX = partial(_LAX_FIELD, alias=Columns.TIDE_TIME)
TIDE_TIME_FIELD = partial(_COERCE_FIELD, alias=Columns.TIDE_TIME)
PAST_24HR_RAINFALL_FIELD_LAX = partial(_LAX_FIELD, alias=Columns.PAST_24HR_RAINFALL)
PAST_24HR_RAINFALL_FIELD = partial(_COERCE_FIELD, alias=Columns.PAST_24HR_RAINFALL)
WEATHER_FIELD_LAX = partial(_LAX_FIELD, alias=Columns.WEATHER)
WEATHER_FIELD = partial(_COERCE_FIELD, alias=Columns.WEATHER)


# TODO: Implement this.
class FormMetadataExtracted(pa.DataFrameSchema):
    """Schema for the form metadata extracted from the datasheets."""

    form_id: Series[str] = FORM_ID_FIELD_LAX()
    city: Series[str] = CITY_FIELD_LAX()
    date: Series[str] = DATE_FIELD_LAX()
    notes: Series[str] = NOTES_FIELD_LAX()

    class Config:
        """The configuration for the schema."""

        strict = False


# TODO: Implement this.
class InvestigatorsExtracted(pa.DataFrameSchema):
    """Schema for the investigators extracted from the datasheets."""

    form_id: Series[str] = FORM_ID_FIELD_LAX()
    investigator: Series[str] = INVESTIGATOR_FIELD_LAX()
    start_time: Series[str] = START_TIME_FIELD_LAX()
    end_time: Series[str] = END_TIME_FIELD_LAX()

    class Config:
        """The configuration for the schema."""

        strict = False


# TODO: Implement this.
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


# TODO: Implement this.
class SiteObservationsExtracted(pa.DataFrameSchema):
    """Schema for the observations precleaned."""

    form_id: Series[str] = FORM_ID_FIELD_LAX()

    class Config:
        """The configuration for the schema."""

        strict = False


# TODO: Implement this.
class FormMetadataPrecleaned(pa.DataFrameSchema):
    """Schema for the form metadata precleaned."""

    form_id: Series[str] = FORM_ID_FIELD_UNQ()
    city: Series[str] = CITY_FIELD()
    date: Series[str] = DATE_FIELD()
    notes: Series[str] = NOTES_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


# TODO: Implement this.
class InvestigatorsPrecleaned(pa.DataFrameSchema):
    """Schema for the investigators precleaned."""

    form_id: Series[str] = FORM_ID_FIELD()
    investigator: Series[str] = INVESTIGATOR_FIELD()
    start_time: Series[str] = START_TIME_FIELD()
    end_time: Series[str] = END_TIME_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


# TODO: Implement this.
class FieldObservationsPrecleaned(pa.DataFrameSchema):
    """Schema for the observations extracted from the datasheets."""

    form_id: Series[str] = FORM_ID_FIELD()
    tide_height: Series[float] = TIDE_HEIGHT_FIELD()
    tide_time: Series[str] = TIDE_TIME_FIELD()
    past_24hr_rainfall: Series[float] = PAST_24HR_RAINFALL_FIELD()
    weather: Series[str] = WEATHER_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


class SiteObservationsPrecleaned(pa.DataFrameSchema):
    """Schema for the observations extracted from the datasheets."""

    form_id: Series[str] = FORM_ID_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


# TODO: Implement this.
class FormMetadataVerified(pa.DataFrameSchema):
    """Schema for the form metadata verified by the user."""

    form_id: Series[str] = FORM_ID_FIELD_UNQ()
    city: Series[str] = CITY_FIELD()
    date: Series[str] = DATE_FIELD()
    notes: Series[str] = NOTES_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


# TODO: Implement this.
class InvestigatorsVerified(pa.DataFrameSchema):
    """Schema for the investigators verified by the user."""

    form_id: Series[str] = FORM_ID_FIELD()
    investigator: Series[str] = INVESTIGATOR_FIELD()
    start_time: Series[str] = START_TIME_FIELD()
    end_time: Series[str] = END_TIME_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


# TODO: Implement this.
class FieldObservationsVerified(pa.DataFrameSchema):
    """Schema for the observations verified by the user."""

    form_id: Series[str] = FORM_ID_FIELD()
    tide_height: Series[float] = TIDE_HEIGHT_FIELD()
    tide_time: Series[str] = TIDE_TIME_FIELD()
    past_24hr_rainfall: Series[float] = PAST_24HR_RAINFALL_FIELD()
    weather: Series[str] = WEATHER_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


# TODO: Implement this.
class SiteObservationsVerified(pa.DataFrameSchema):
    """Schema for the observations verified by the user."""

    form_id: Series[str] = FORM_ID_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


# TODO: Implement this.
class FormMetadataCleaned(pa.DataFrameSchema):
    """Schema for the form metadata cleaned."""

    form_id: Series[str] = FORM_ID_FIELD_UNQ()
    city: Series[str] = CITY_FIELD()
    date: Series[str] = DATE_FIELD()
    notes: Series[str] = NOTES_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


# TODO: Implement this.
class InvestigatorsCleaned(pa.DataFrameSchema):
    """Schema for the investigators cleaned."""

    form_id: Series[str] = FORM_ID_FIELD()
    investigator: Series[str] = INVESTIGATOR_FIELD()
    start_time: Series[str] = START_TIME_FIELD()
    end_time: Series[str] = END_TIME_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


# TODO: Implement this.
class FieldObservationsCleaned(pa.DataFrameSchema):
    """Schema for the observations cleaned."""

    form_id: Series[str] = FORM_ID_FIELD()
    tide_height: Series[float] = TIDE_HEIGHT_FIELD()
    tide_time: Series[str] = TIDE_TIME_FIELD()
    past_24hr_rainfall: Series[float] = PAST_24HR_RAINFALL_FIELD()
    weather: Series[str] = WEATHER_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True


# TODO: Implement this.
class SiteObservationsCleaned(pa.DataFrameSchema):
    """Schema for the observations cleaned."""

    form_id: Series[str] = FORM_ID_FIELD()

    class Config:
        """The configuration for the schema."""

        strict = True
