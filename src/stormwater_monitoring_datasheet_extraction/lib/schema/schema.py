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
FORM_ID_FIELD_LAX = partial(_LAX_FIELD, alias=Columns.FORM_ID)
FORM_ID_FIELD = partial(_COERCE_FIELD, alias=Columns.FORM_ID)
FORM_ID_FIELD_UNQ = partial(_UNIQUE_FIELD, alias=Columns.FORM_ID)


# TODO: Implement this.
class FormMetadataExtracted(pa.DataFrameSchema):
    """Schema for the form metadata extracted from the datasheets."""

    form_id: Series[str] = FORM_ID_FIELD_LAX()


# TODO: Implement this.
class InvestigatorsExtracted(pa.DataFrameSchema):
    """Schema for the investigators extracted from the datasheets."""

    form_id: Series[str] = FORM_ID_FIELD_LAX()


# TODO: Implement this.
class FieldObservationsExtracted(pa.DataFrameSchema):
    """Schema for the observations precleaned."""

    form_id: Series[str] = FORM_ID_FIELD_LAX()


# TODO: Implement this.
class SiteObservationsExtracted(pa.DataFrameSchema):
    """Schema for the observations precleaned."""

    form_id: Series[str] = FORM_ID_FIELD_LAX()


# TODO: Implement this.
class FormMetadataPrecleaned(pa.DataFrameSchema):
    """Schema for the form metadata precleaned."""

    form_id: Series[str] = FORM_ID_FIELD_UNQ()


# TODO: Implement this.
class InvestigatorsPrecleaned(pa.DataFrameSchema):
    """Schema for the investigators precleaned."""

    form_id: Series[str] = FORM_ID_FIELD()


# TODO: Implement this.
class FieldObservationsPrecleaned(pa.DataFrameSchema):
    """Schema for the observations extracted from the datasheets."""

    form_id: Series[str] = FORM_ID_FIELD()


class SiteObservationsPrecleaned(pa.DataFrameSchema):
    """Schema for the observations extracted from the datasheets."""

    form_id: Series[str] = FORM_ID_FIELD()


# TODO: Implement this.
class FormMetadataVerified(pa.DataFrameSchema):
    """Schema for the form metadata verified by the user."""

    form_id: Series[str] = FORM_ID_FIELD_UNQ()


# TODO: Implement this.
class InvestigatorsVerified(pa.DataFrameSchema):
    """Schema for the investigators verified by the user."""

    form_id: Series[str] = FORM_ID_FIELD()


# TODO: Implement this.
class FieldObservationsVerified(pa.DataFrameSchema):
    """Schema for the observations verified by the user."""

    form_id: Series[str] = FORM_ID_FIELD()


# TODO: Implement this.
class SiteObservationsVerified(pa.DataFrameSchema):
    """Schema for the observations verified by the user."""

    form_id: Series[str] = FORM_ID_FIELD()


# TODO: Implement this.
class FormMetadataCleaned(pa.DataFrameSchema):
    """Schema for the form metadata cleaned."""

    form_id: Series[str] = FORM_ID_FIELD_UNQ()


# TODO: Implement this.
class InvestigatorsCleaned(pa.DataFrameSchema):
    """Schema for the investigators cleaned."""

    form_id: Series[str] = FORM_ID_FIELD()


# TODO: Implement this.
class FieldObservationsCleaned(pa.DataFrameSchema):
    """Schema for the observations cleaned."""

    form_id: Series[str] = FORM_ID_FIELD()


# TODO: Implement this.
class SiteObservationsCleaned(pa.DataFrameSchema):
    """Schema for the observations cleaned."""

    form_id: Series[str] = FORM_ID_FIELD()
