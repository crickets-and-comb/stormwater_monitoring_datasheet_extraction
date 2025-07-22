"""Top-level module for stormwater monitoring datasheet ETL."""

from pathlib import Path
from typing import Any, Dict, Tuple

import pandera as pa
from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib.constants import DocStrings
from stormwater_monitoring_datasheet_extraction.lib.schema.schema import (
    FieldObservationsCleaned,
    FieldObservationsExtracted,
    FieldObservationsPrecleaned,
    FieldObservationsVerified,
    FormMetadataCleaned,
    FormMetadataExtracted,
    FormMetadataPrecleaned,
    FormMetadataVerified,
    InvestigatorsCleaned,
    InvestigatorsExtracted,
    InvestigatorsPrecleaned,
    InvestigatorsVerified,
    QualitativeSiteObservationsCleaned,
    QualitativeSiteObservationsExtracted,
    QualitativeSiteObservationsPrecleaned,
    QualitativeSiteObservationsVerified,
    SiteObservationsCleaned,
    SiteObservationsExtracted,
    SiteObservationsPrecleaned,
    SiteObservationsVerified,
)


# TODO: Set up logging.
# TODO: Set up Pandera schema for each step.
@typechecked
def run_etl(input_dir: Path, output_dir: Path) -> Path:  # noqa: D103
    # TODO, NOTE: This is an estimate outline, not a hard requirement.
    # We may need to adjust the steps based on the actual implementation details.
    # For instance, we may want to add a cleaning step between raw extraction and user
    # verification.
    (
        raw_metadata,
        raw_investigators,
        raw_field_field_observations,
        raw_site_observations,
        raw_qualitative_site_observations,
    ) = extract(input_dir=input_dir)

    (
        precleaned_metadata,
        precleaned_investigators,
        precleaned_field_observations,
        precleaned_site_observations,
        precleaned_qualitative_site_observations,
    ) = preclean(
        raw_metadata=raw_metadata,
        raw_investigators=raw_investigators,
        raw_field_field_observations=raw_field_field_observations,
        raw_site_observations=raw_site_observations,
        raw_qualitative_site_observations=raw_qualitative_site_observations,
    )

    (
        verified_metadata,
        verified_investigators,
        verified_field_observations,
        verified_site_observations,
        verified_qualitative_site_observations,
    ) = verify(
        precleaned_metadata=precleaned_metadata,
        precleaned_investigators=precleaned_investigators,
        precleaned_field_observations=precleaned_field_observations,
        precleaned_site_observations=precleaned_site_observations,
        precleaned_qualitative_site_observations=precleaned_qualitative_site_observations,
    )

    (
        cleaned_metadata,
        cleaned_investigators,
        cleaned_field_observations,
        cleaned_site_observations,
        cleaned_qualitative_site_observations,
    ) = clean(
        verified_metadata=verified_metadata,
        verified_investigators=verified_investigators,
        verified_field_observations=verified_field_observations,
        verified_site_observations=verified_site_observations,
        verified_qualitative_site_observations=verified_qualitative_site_observations,
    )

    restructured_json = restructure_extraction(
        cleaned_metadata=cleaned_metadata,
        cleaned_investigators=cleaned_investigators,
        cleaned_field_observations=cleaned_field_observations,
        cleaned_site_observations=cleaned_site_observations,
        cleaned_qualitative_site_observations=cleaned_qualitative_site_observations,
    )

    final_output_path = load(restructured_json=restructured_json, output_dir=output_dir)

    return final_output_path


run_etl.__doc__ = DocStrings.RUN_ETL.api_docstring


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def extract(
    input_dir: Path,
) -> Tuple[
    FormMetadataExtracted,
    InvestigatorsExtracted,
    FieldObservationsExtracted,
    SiteObservationsExtracted,
    QualitativeSiteObservationsExtracted,
]:
    """Extracts data from the images in the input directory.

    Using computer vision, extracts data from datasheets.

    Args:
        input_dir: Path to the directory containing the datasheet images.

    Returns:
        Raw extraction split into form metadata, investigators, field observations,
            and site observations.
    """
    # TODO: Index all to form/image name.
    form_metadata = FormMetadataExtracted()
    investigators = InvestigatorsExtracted()
    field_field_observations = FieldObservationsExtracted()
    site_observations = SiteObservationsExtracted()
    qualitative_site_observations = QualitativeSiteObservationsExtracted()
    ...

    return (
        form_metadata,
        investigators,
        field_field_observations,
        site_observations,
        qualitative_site_observations,
    )


def preclean(
    raw_metadata: FormMetadataExtracted,
    raw_investigators: InvestigatorsExtracted,
    raw_field_field_observations: FieldObservationsExtracted,
    raw_site_observations: SiteObservationsExtracted,
    raw_qualitative_site_observations: QualitativeSiteObservationsExtracted,
) -> Tuple[
    FormMetadataPrecleaned,
    InvestigatorsPrecleaned,
    FieldObservationsPrecleaned,
    SiteObservationsPrecleaned,
    QualitativeSiteObservationsPrecleaned,
]:
    """Preclean the raw extraction.

    Ligth cleaning before user verification. E.g., strip whitespace, try to cast to type,
    check for within range, but warn don't fail.

    Args:
        raw_metadata: Metadata extracted from the datasheets.
        raw_investigators: Investigators extracted from the datasheets.
        raw_field_field_observations: Field observations extracted from the datasheets.
        raw_site_observations: Site observations extracted from the datasheets.
        raw_qualitative_site_observations:
            Qualitative site observations extracted from the datasheets.

    Returns:
        Precleaned metadata, investigators, field observations, and site observations.
    """
    precleaned_metadata = FormMetadataPrecleaned()
    precleaned_investigators = InvestigatorsPrecleaned()
    precleaned_field_observations = FieldObservationsPrecleaned()
    precleaned_site_observations = SiteObservationsPrecleaned()
    precleaned_qualitative_site_observations = QualitativeSiteObservationsPrecleaned()
    ...

    return (
        precleaned_metadata,
        precleaned_investigators,
        precleaned_field_observations,
        precleaned_site_observations,
        precleaned_qualitative_site_observations,
    )


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def verify(
    precleaned_metadata: FormMetadataPrecleaned,
    precleaned_investigators: InvestigatorsPrecleaned,
    precleaned_field_observations: FieldObservationsPrecleaned,
    precleaned_site_observations: SiteObservationsPrecleaned,
    precleaned_qualitative_site_observations: QualitativeSiteObservationsPrecleaned,
) -> Tuple[
    FormMetadataVerified,
    InvestigatorsVerified,
    FieldObservationsVerified,
    SiteObservationsVerified,
    QualitativeSiteObservationsVerified,
]:
    """Verifies the raw extraction with the user.

    Prompts user to check each image against each extraction and edit as needed.

    Args:
        precleaned_metadata: The precleaned metadata.
        precleaned_investigators: The precleaned investigators.
        precleaned_field_observations: The precleaned field observations.
        precleaned_site_observations: The precleaned site observations.
        precleaned_qualitative_site_observations:
            The precleaned qualitative site observations.

    Returns:
        User-verified metadata, investigators, field observations, and site observations.
    """
    verified_metadata = FormMetadataVerified()
    verified_investigators = InvestigatorsVerified()
    verified_field_observations = FieldObservationsVerified()
    verified_site_observations = SiteObservationsVerified()
    verified_qualitative_site_observations = QualitativeSiteObservationsVerified()
    ...

    return (
        verified_metadata,
        verified_investigators,
        verified_field_observations,
        verified_site_observations,
        verified_qualitative_site_observations,
    )


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def clean(
    verified_metadata: FormMetadataVerified,
    verified_investigators: InvestigatorsVerified,
    verified_field_observations: FieldObservationsVerified,
    verified_site_observations: SiteObservationsVerified,
    verified_qualitative_site_observations: QualitativeSiteObservationsVerified,
) -> Tuple[
    FormMetadataCleaned,
    InvestigatorsCleaned,
    FieldObservationsCleaned,
    SiteObservationsCleaned,
    QualitativeSiteObservationsCleaned,
]:
    """Clean the user-verified extraction.

    Clean and validates the user-verified extraction data, ensuring it is in a consistent
    format, appropriate data types, within specified ranges, etc., and ready to load.

    Args:
        verified_metadata: The user-verified metadata.
        verified_investigators: The user-verified investigators.
        verified_field_observations: The user-verified field observations.
        verified_site_observations: The user-verified site observations.
        verified_qualitative_site_observations:
            The user-verified qualitative site observations.

    Returns:
        Cleaned metadata, investigators, field observations, and site observations.
    """
    cleaned_metadata = FormMetadataCleaned()
    cleaned_investigators = InvestigatorsCleaned()
    cleaned_field_observations = FieldObservationsCleaned()
    cleaned_site_observations = SiteObservationsCleaned()
    cleaned_qualitative_site_observations = QualitativeSiteObservationsCleaned()
    ...

    return (
        cleaned_metadata,
        cleaned_investigators,
        cleaned_field_observations,
        cleaned_site_observations,
        cleaned_qualitative_site_observations,
    )


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def restructure_extraction(
    cleaned_metadata: FormMetadataCleaned,
    cleaned_investigators: InvestigatorsCleaned,
    cleaned_field_observations: FieldObservationsCleaned,
    cleaned_site_observations: SiteObservationsCleaned,
    cleaned_qualitative_site_observations: QualitativeSiteObservationsCleaned,
) -> Dict[str, Any]:
    """Restructure the cleaned extraction into a JSON schema.

    Args:
        cleaned_metadata: The cleaned metadata.
        cleaned_investigators: The cleaned investigators.
        cleaned_field_observations: The cleaned field observations.
        cleaned_site_observations: The cleaned site observations.
        cleaned_qualitative_site_observations: The cleaned qualitative site observations.

    Returns:
        Restructured JSON schema.
    """
    restructured_json = {}

    ...
    return restructured_json


# TODO: Implement this.
@typechecked
def load(restructured_json: Dict[str, Any], output_dir: Path) -> Path:
    """Load the cleaned data into the output directory.

    Saves the cleaned data to the specified output directory in a structured format.
    If the output directory does not exist, it will be created.

    Args:
        restructured_json: The restructured JSON schema.
        output_dir: The directory where the cleaned data will be saved.
            If empty path, defaults to a dated directory in the current working directory.

    Returns:
        Path to the saved cleaned data file.
    """
    final_output_path = Path()

    ...

    return final_output_path
