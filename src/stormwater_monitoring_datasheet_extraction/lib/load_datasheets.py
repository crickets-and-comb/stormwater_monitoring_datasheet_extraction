"""Top-level module for stormwater monitoring datasheet ETL."""

from pathlib import Path
from typing import Any, Dict, Tuple

import pandera as pa
from pandera.typing import DataFrame
from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib import schema
from stormwater_monitoring_datasheet_extraction.lib.constants import DocStrings


# TODO: Set up logging.
@typechecked
def run_etl(input_dir: Path, output_dir: Path) -> Path:  # noqa: D103
    # TODO, NOTE: This is an estimated outline, not a hard requirement.
    # We may need to adjust the steps based on the actual implementation details.
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
    DataFrame[schema.FormMetadataExtracted],
    DataFrame[schema.InvestigatorsExtracted],
    DataFrame[schema.FieldObservationsExtracted],
    DataFrame[schema.SiteObservationsExtracted],
    DataFrame[schema.QualitativeSiteObservationsExtracted],
]:
    """Extracts data from the images in the input directory.

    Using computer vision, extracts data from datasheets.

    Args:
        input_dir: Path to the directory containing the datasheet images.

    Returns:
        Raw extraction split into form metadata, investigators, field observations,
            and site observations.
    """
    form_metadata = DataFrame[schema.FormMetadataExtracted]()
    investigators = DataFrame[schema.InvestigatorsExtracted]()
    field_field_observations = DataFrame[schema.FieldObservationsExtracted]()
    site_observations = DataFrame[schema.SiteObservationsExtracted]()
    qualitative_site_observations = DataFrame[schema.QualitativeSiteObservationsExtracted]()
    ...

    return (
        form_metadata,
        investigators,
        field_field_observations,
        site_observations,
        qualitative_site_observations,
    )


def preclean(
    raw_metadata: DataFrame[schema.FormMetadataExtracted],
    raw_investigators: DataFrame[schema.InvestigatorsExtracted],
    raw_field_field_observations: DataFrame[schema.FieldObservationsExtracted],
    raw_site_observations: DataFrame[schema.SiteObservationsExtracted],
    raw_qualitative_site_observations: DataFrame[schema.QualitativeSiteObservationsExtracted],
) -> Tuple[
    DataFrame[schema.FormMetadataPrecleaned],
    DataFrame[schema.InvestigatorsPrecleaned],
    DataFrame[schema.FieldObservationsPrecleaned],
    DataFrame[schema.SiteObservationsPrecleaned],
    DataFrame[schema.QualitativeSiteObservationsPrecleaned],
]:
    """Preclean the raw extraction.

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
    # TODO: Light cleaning before user verification.
    # E.g., strip whitespace, try to cast, check range, but warn don't fail.
    precleaned_metadata = DataFrame[schema.FormMetadataPrecleaned]()
    precleaned_investigators = DataFrame[schema.InvestigatorsPrecleaned]()
    precleaned_field_observations = DataFrame[schema.FieldObservationsPrecleaned]()
    precleaned_site_observations = DataFrame[schema.SiteObservationsPrecleaned]()
    precleaned_qualitative_site_observations = DataFrame[
        schema.QualitativeSiteObservationsPrecleaned
    ]()
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
    precleaned_metadata: DataFrame[schema.FormMetadataPrecleaned],
    precleaned_investigators: DataFrame[schema.InvestigatorsPrecleaned],
    precleaned_field_observations: DataFrame[schema.FieldObservationsPrecleaned],
    precleaned_site_observations: DataFrame[schema.SiteObservationsPrecleaned],
    precleaned_qualitative_site_observations: DataFrame[
        schema.QualitativeSiteObservationsPrecleaned
    ],
) -> Tuple[
    DataFrame[schema.FormMetadataVerified],
    DataFrame[schema.InvestigatorsVerified],
    DataFrame[schema.FieldObservationsVerified],
    DataFrame[schema.SiteObservationsVerified],
    DataFrame[schema.QualitativeSiteObservationsVerified],
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
    verified_metadata = DataFrame[schema.FormMetadataVerified]()
    verified_investigators = DataFrame[schema.InvestigatorsVerified]()
    verified_field_observations = DataFrame[schema.FieldObservationsVerified]()
    verified_site_observations = DataFrame[schema.SiteObservationsVerified]()
    verified_qualitative_site_observations = DataFrame[
        schema.QualitativeSiteObservationsVerified
    ]()
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
    verified_metadata: DataFrame[schema.FormMetadataVerified],
    verified_investigators: DataFrame[schema.InvestigatorsVerified],
    verified_field_observations: DataFrame[schema.FieldObservationsVerified],
    verified_site_observations: DataFrame[schema.SiteObservationsVerified],
    verified_qualitative_site_observations: DataFrame[
        schema.QualitativeSiteObservationsVerified
    ],
) -> Tuple[
    DataFrame[schema.FormMetadataCleaned],
    DataFrame[schema.InvestigatorsCleaned],
    DataFrame[schema.FieldObservationsCleaned],
    DataFrame[schema.SiteObservationsCleaned],
    DataFrame[schema.QualitativeSiteObservationsCleaned],
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
    cleaned_metadata = DataFrame[schema.FormMetadataCleaned]()
    cleaned_investigators = DataFrame[schema.InvestigatorsCleaned]()
    cleaned_field_observations = DataFrame[schema.FieldObservationsCleaned]()
    cleaned_site_observations = DataFrame[schema.SiteObservationsCleaned]()
    cleaned_qualitative_site_observations = DataFrame[
        schema.QualitativeSiteObservationsCleaned
    ]()
    ...
    # TODO: Validate referential integrity. (Among other things to do here.)

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
    cleaned_metadata: DataFrame[schema.FormMetadataCleaned],
    cleaned_investigators: DataFrame[schema.InvestigatorsCleaned],
    cleaned_field_observations: DataFrame[schema.FieldObservationsCleaned],
    cleaned_site_observations: DataFrame[schema.SiteObservationsCleaned],
    cleaned_qualitative_site_observations: DataFrame[
        schema.QualitativeSiteObservationsCleaned
    ],
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
