"""Pandera schemas for ETL steps."""

import pandera as pa

# TODO: Validations should be lax for extraction, stricter after cleaning,
# stricter after user verification, and strictest after final cleaning.
# TODO: Index all to form/image name.


# TODO: Implement this.
class FormMetadataExtracted(pa.DataFrameSchema):
    """Schema for the form metadata extracted from the datasheets."""

    pass


# TODO: Implement this.
class InvestigatorsExtracted(pa.DataFrameSchema):
    """Schema for the investigators extracted from the datasheets."""

    pass


# TODO: Implement this.
class FieldObservationsExtracted(pa.DataFrameSchema):
    """Schema for the observations precleaned."""

    pass


# TODO: Implement this.
class SiteObservationsExtracted(pa.DataFrameSchema):
    """Schema for the observations precleaned."""

    pass


# TODO: Implement this.
class FormMetadataPrecleaned(pa.DataFrameSchema):
    """Schema for the form metadata precleaned."""

    pass


# TODO: Implement this.
class InvestigatorsPrecleaned(pa.DataFrameSchema):
    """Schema for the investigators precleaned."""

    pass


# TODO: Implement this.
class FieldObservationsPrecleaned(pa.DataFrameSchema):
    """Schema for the observations extracted from the datasheets."""

    pass


class SiteObservationsPrecleaned(pa.DataFrameSchema):
    """Schema for the observations extracted from the datasheets."""

    pass


# TODO: Implement this.
class FormMetadataVerified(pa.DataFrameSchema):
    """Schema for the form metadata verified by the user."""

    pass


# TODO: Implement this.
class InvestigatorsVerified(pa.DataFrameSchema):
    """Schema for the investigators verified by the user."""

    pass


# TODO: Implement this.
class FieldObservationsVerified(pa.DataFrameSchema):
    """Schema for the observations verified by the user."""

    pass


# TODO: Implement this.
class SiteObservationsVerified(pa.DataFrameSchema):
    """Schema for the observations verified by the user."""

    pass


# TODO: Implement this.
class FormMetadataCleaned(pa.DataFrameSchema):
    """Schema for the form metadata cleaned."""

    pass


# TODO: Implement this.
class InvestigatorsCleaned(pa.DataFrameSchema):
    """Schema for the investigators cleaned."""

    pass


# TODO: Implement this.
class FieldObservationsCleaned(pa.DataFrameSchema):
    """Schema for the observations cleaned."""

    pass


# TODO: Implement this.
class SiteObservationsCleaned(pa.DataFrameSchema):
    """Schema for the observations cleaned."""

    pass
