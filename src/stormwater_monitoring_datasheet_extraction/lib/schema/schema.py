"""Pandera schemas for the stormwater monitoring datasheet extraction."""

import pandera as pa

# TODO: Validations should be lax for extraction,
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
class ObservationsExtracted(pa.DataFrameSchema):
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
class ObservationsVerified(pa.DataFrameSchema):
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
class ObservationsCleaned(pa.DataFrameSchema):
    """Schema for the observations cleaned."""

    pass
