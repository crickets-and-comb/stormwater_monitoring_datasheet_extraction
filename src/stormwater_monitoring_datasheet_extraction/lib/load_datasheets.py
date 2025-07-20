"""Top-level module for stormwater monitoring datasheet ETL."""

from pathlib import Path
from typing import Any, Dict, Tuple

import pandera as pa
from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib.constants import DocStrings
from stormwater_monitoring_datasheet_extraction.lib.schema.schema import (
    FormMetadataCleaned,
    FormMetadataExtracted,
    FormMetadataVerified,
    InvestigatorsCleaned,
    InvestigatorsExtracted,
    InvestigatorsVerified,
    ObservationsCleaned,
    ObservationsExtracted,
    ObservationsVerified,
)


# TODO: Set up logging.
# TODO: Set up Pandera schema for each step.
@typechecked
def run_etl(input_dir: Path, output_dir: Path) -> Path:  # noqa: D103
    # TODO, NOTE: This is an estimate outline, not a hard requirement.
    # We may need to adjust the steps based on the actual implementation details.
    # For instance, we may want to add a cleaning step between raw extraction and user
    # verification.
    raw_metadata, raw_investigators, raw_observations = extract(input_dir=input_dir)

    verified_metadata, verified_investigators, verified_observations = verify(
        raw_metadata=raw_metadata,
        raw_investigators=raw_investigators,
        raw_observations=raw_observations,
    )

    cleaned_metadata, cleaned_investigators, cleaned_observations = clean(
        verified_metadata=verified_metadata,
        verified_investigators=verified_investigators,
        verified_observations=verified_observations,
    )

    restructured_json = restructure_extraction(
        cleaned_metadata=cleaned_metadata,
        cleaned_investigators=cleaned_investigators,
        cleaned_observations=cleaned_observations,
    )

    final_output_path = load(restructured_json=restructured_json, output_dir=output_dir)

    return final_output_path


run_etl.__doc__ = DocStrings.RUN_ETL.api_docstring


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def extract(
    input_dir: Path,
) -> Tuple[FormMetadataExtracted, InvestigatorsExtracted, ObservationsExtracted]:
    """Extracts data from the images in the input directory.

    Using computer vision extracts data from datasheets into JSON schema.

    Args:
        input_dir: Path to the directory containing the datasheet images.

    Returns:
        Raw extraction split into form metadata, investigators, and observations.
    """
    # TODO: Index all to form/image name.
    form_metadata = FormMetadataExtracted()
    investigators = InvestigatorsExtracted()
    observations = ObservationsExtracted()

    ...

    return form_metadata, investigators, observations


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def verify(
    raw_metadata: FormMetadataExtracted,
    raw_investigators: InvestigatorsExtracted,
    raw_observations: ObservationsExtracted,
) -> Tuple[FormMetadataVerified, InvestigatorsVerified, ObservationsVerified]:
    """Verifies the raw extraction with the user.

    Prompts user to check each image against each extraction and edit as needed.

    Args:
        raw_metadata: The raw metadata extracted from the datasheets.
        raw_investigators: The raw investigators extracted from the datasheets.
        raw_observations: The raw observations extracted from the datasheets.

    Returns:
        User-verified metadata, investigators, and observations.
    """
    verified_metadata = FormMetadataVerified()
    verified_investigators = InvestigatorsVerified()
    verified_observations = ObservationsVerified()

    ...

    return verified_metadata, verified_investigators, verified_observations


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def clean(
    verified_metadata: FormMetadataVerified,
    verified_investigators: InvestigatorsVerified,
    verified_observations: ObservationsVerified,
) -> Tuple[FormMetadataCleaned, InvestigatorsCleaned, ObservationsCleaned]:
    """Clean the user verified extraction.

    Clean and validates the user verified extraction data, ensuring it is in a consistent
    format, appropriate data types, within specified ranges, etc., and ready to load.

    Args:
        verified_metadata: The user verified metadata.
        verified_investigators: The user verified investigators.
        verified_observations: The user verified observations.

    Returns:
        Cleaned metadata, investigators, and observations.
    """
    cleaned_metadata = FormMetadataCleaned()
    cleaned_investigators = InvestigatorsCleaned()
    cleaned_observations = ObservationsCleaned()

    ...

    return cleaned_metadata, cleaned_investigators, cleaned_observations


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def restructure_extraction(
    cleaned_metadata: FormMetadataCleaned,
    cleaned_investigators: InvestigatorsCleaned,
    cleaned_observations: ObservationsCleaned,
) -> Dict[str, Any]:
    """Restructure the cleaned extraction into a JSON schema.

    Args:
        cleaned_metadata: The cleaned metadata.
        cleaned_investigators: The cleaned investigators.
        cleaned_observations: The cleaned observations.

    Returns:
        Restructured JSON schema.
    """
    restructured_json = {}

    ...
    return restructured_json


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
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
