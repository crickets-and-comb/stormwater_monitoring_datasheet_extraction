"""Top-level module for stormwater monitoring datasheet ETL."""

from pathlib import Path
from typing import Any, cast

import pandas as pd
import pandera as pa
import pandera.typing as pt
from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib import schema
from stormwater_monitoring_datasheet_extraction.lib.constants import DocStrings

# TODO: To check observations threshholds, need a site-type map:
# creek or outfall, and if creek:
# habitat, spawn, rear, or migrate.


# TODO: Set up logging.
@typechecked
def run_etl(input_dir: Path, output_dir: Path) -> Path:  # noqa: D103
    # TODO, NOTE: This is an estimated outline, not a hard requirement.
    # We may need to adjust the steps based on the actual implementation details.
    (
        raw_metadata,
        raw_investigators,
        raw_site_observations,
        raw_qualitative_site_observations,
    ) = extract(input_dir=input_dir)

    (
        precleaned_metadata,
        precleaned_investigators,
        precleaned_site_observations,
        precleaned_qualitative_site_observations,
    ) = preclean(
        raw_metadata=raw_metadata,
        raw_investigators=raw_investigators,
        raw_site_observations=raw_site_observations,
        raw_qualitative_site_observations=raw_qualitative_site_observations,
    )

    (
        verified_metadata,
        verified_investigators,
        verified_site_observations,
        verified_qualitative_site_observations,
    ) = verify(
        precleaned_metadata=precleaned_metadata,
        precleaned_investigators=precleaned_investigators,
        precleaned_site_observations=precleaned_site_observations,
        precleaned_qualitative_site_observations=precleaned_qualitative_site_observations,
    )

    (
        cleaned_metadata,
        cleaned_investigators,
        cleaned_site_observations,
        cleaned_qualitative_site_observations,
    ) = clean(
        verified_metadata=verified_metadata,
        verified_investigators=verified_investigators,
        verified_site_observations=verified_site_observations,
        verified_qualitative_site_observations=verified_qualitative_site_observations,
    )

    restructured_json = restructure_extraction(
        cleaned_metadata=cleaned_metadata,
        cleaned_investigators=cleaned_investigators,
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
) -> tuple[
    pt.DataFrame[schema.FormMetadataExtracted],
    pt.DataFrame[schema.InvestigatorsExtracted],
    pt.DataFrame[schema.SiteObservationsExtracted],
    pt.DataFrame[schema.QualitativeSiteObservationsExtracted],
]:
    """Extracts data from the images in the input directory.

    Using computer vision, extracts data from datasheets.

    Args:
        input_dir: Path to the directory containing the datasheet images.

    Returns:
        Raw extraction split into form metadata, investigators,
            and site observations.
    """
    # TODO: When implementing, you can just make a pandas.DataFrame. No need to cast.
    # It will cast and validate on return.
    form_metadata = cast("pt.DataFrame[schema.FormMetadataExtracted]", pd.DataFrame())
    investigators = cast("pt.DataFrame[schema.InvestigatorsExtracted]", pd.DataFrame())
    site_observations = cast("pt.DataFrame[schema.SiteObservationsExtracted]", pd.DataFrame())
    qualitative_site_observations = cast(
        "pt.DataFrame[schema.QualitativeSiteObservationsExtracted]", pd.DataFrame()
    )
    # TODO: Use data definition as source of truth rather than schema.
    ...

    return (
        form_metadata,
        investigators,
        site_observations,
        qualitative_site_observations,
    )


# TODO: Implement this.
def preclean(
    raw_metadata: pt.DataFrame[schema.FormMetadataExtracted],
    raw_investigators: pt.DataFrame[schema.InvestigatorsExtracted],
    raw_site_observations: pt.DataFrame[schema.SiteObservationsExtracted],
    raw_qualitative_site_observations: pt.DataFrame[
        schema.QualitativeSiteObservationsExtracted
    ],
) -> tuple[
    pt.DataFrame[schema.FormMetadataPrecleaned],
    pt.DataFrame[schema.InvestigatorsPrecleaned],
    pt.DataFrame[schema.SiteObservationsPrecleaned],
    pt.DataFrame[schema.QualitativeSiteObservationsPrecleaned],
]:
    """Preclean the raw extraction.

    Args:
        raw_metadata: Metadata extracted from the datasheets.
        raw_investigators: Investigators extracted from the datasheets.
        raw_site_observations: Site observations extracted from the datasheets.
        raw_qualitative_site_observations:
            Qualitative site observations extracted from the datasheets.

    Returns:
        Precleaned metadata, investigators, and site observations.
    """
    # TODO: Light cleaning before user verification.
    # E.g., strip whitespace, try to cast, check range, but warn don't fail.
    # Much of this might be done by creating a custom class for each field
    # that cleans and warns on construction,
    # define __str__/__repr__/__int__ etc. as needed,
    # and use the class as a type in the schema to coerce the data.
    # Use data definition as source of truth rather than schema.
    # TODO: When implementing, you can just make a pandas.DataFrame. No need to cast.
    # It will cast and validate on return.
    precleaned_metadata = cast("pt.DataFrame[schema.FormMetadataPrecleaned]", raw_metadata)
    precleaned_investigators = cast(
        "pt.DataFrame[schema.InvestigatorsPrecleaned]", raw_investigators
    )
    precleaned_site_observations = cast(
        "pt.DataFrame[schema.SiteObservationsPrecleaned]", raw_site_observations
    )
    precleaned_qualitative_site_observations = cast(
        "pt.DataFrame[schema.QualitativeSiteObservationsPrecleaned]",
        raw_qualitative_site_observations,
    )
    ...

    return (
        precleaned_metadata,
        precleaned_investigators,
        precleaned_site_observations,
        precleaned_qualitative_site_observations,
    )


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def verify(
    precleaned_metadata: pt.DataFrame[schema.FormMetadataPrecleaned],
    precleaned_investigators: pt.DataFrame[schema.InvestigatorsPrecleaned],
    precleaned_site_observations: pt.DataFrame[schema.SiteObservationsPrecleaned],
    precleaned_qualitative_site_observations: pt.DataFrame[
        schema.QualitativeSiteObservationsPrecleaned
    ],
) -> tuple[
    pt.DataFrame[schema.FormMetadataVerified],
    pt.DataFrame[schema.InvestigatorsVerified],
    pt.DataFrame[schema.SiteObservationsVerified],
    pt.DataFrame[schema.QualitativeSiteObservationsVerified],
]:
    """Verifies the raw extraction with the user.

    Prompts user to check each image against each extraction and edit as needed.

    Args:
        precleaned_metadata: The precleaned metadata.
        precleaned_investigators: The precleaned investigators.
        precleaned_site_observations: The precleaned site observations.
        precleaned_qualitative_site_observations:
            The precleaned qualitative site observations.

    Returns:
        User-verified metadata, investigators, and site observations.
    """
    # TODO: When implementing, you can just make a pandas.DataFrame. No need to cast.
    # It will cast and validate on return.
    verified_metadata = cast("pt.DataFrame[schema.FormMetadataVerified]", precleaned_metadata)
    verified_investigators = cast(
        "pt.DataFrame[schema.InvestigatorsVerified]", precleaned_investigators
    )
    verified_site_observations = cast(
        "pt.DataFrame[schema.SiteObservationsVerified]", precleaned_site_observations
    )
    verified_qualitative_site_observations = cast(
        "pt.DataFrame[schema.QualitativeSiteObservationsVerified]",
        precleaned_qualitative_site_observations,
    )
    ...
    # TODO: Offer some immediate feedback:
    # Offer enumerated options for categorical data.
    # Highlight invalid extracted fields as they come to user's focus.
    # Ask for reentry if entered/verified can't be typed correctly or is out of range.
    # Warn and offer to re-enter if out of expected range but within valid range.
    # Use data definition as source of truth rather than schema.

    return (
        verified_metadata,
        verified_investigators,
        verified_site_observations,
        verified_qualitative_site_observations,
    )


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def clean(
    verified_metadata: pt.DataFrame[schema.FormMetadataVerified],
    verified_investigators: pt.DataFrame[schema.InvestigatorsVerified],
    verified_site_observations: pt.DataFrame[schema.SiteObservationsVerified],
    verified_qualitative_site_observations: pt.DataFrame[
        schema.QualitativeSiteObservationsVerified
    ],
) -> tuple[
    pt.DataFrame[schema.FormMetadataCleaned],
    pt.DataFrame[schema.InvestigatorsCleaned],
    pt.DataFrame[schema.SiteObservationsCleaned],
    pt.DataFrame[schema.QualitativeSiteObservationsCleaned],
]:
    """Clean the user-verified extraction.

    Clean and validates the user-verified extraction data, ensuring it is in a consistent
    format, appropriate data types, within specified ranges, etc., and ready to load.

    Args:
        verified_metadata: The user-verified metadata.
        verified_investigators: The user-verified investigators.
        verified_site_observations: The user-verified site observations.
        verified_qualitative_site_observations:
            The user-verified qualitative site observations.

    Returns:
        Cleaned metadata, investigators, and site observations.
    """
    # TODO: When implementing, you can just make a pandas.DataFrame. No need to cast.
    # It will cast and validate on return.
    cleaned_metadata = cast("pt.DataFrame[schema.FormMetadataCleaned]", verified_metadata)
    cleaned_investigators = cast(
        "pt.DataFrame[schema.InvestigatorsCleaned]", verified_investigators
    )
    cleaned_site_observations = cast(
        "pt.DataFrame[schema.SiteObservationsCleaned]", verified_site_observations
    )
    cleaned_qualitative_site_observations = cast(
        "pt.DataFrame[schema.QualitativeSiteObservationsCleaned]",
        verified_qualitative_site_observations,
    )
    ...
    # TODO: Inferred/courtesy imputations? (nulls/empties, don't overstep)

    # TODO: Validations schema can't accomplish:
    # - Referential integrity.
    # - Date is on or before today.
    # - Ideally, we would verify that site arrival times are within
    #   the investigator's start and end times, but we can't 100% do that
    #   because forms don't assign observations to investigators.
    # - Qualitative observations for non-dry outfalls exist, but none for dry outfalls.

    # TODO: If still invalid, alert to the problem, and re-call `verify()`.
    # Use data definition as source of truth rather than schema.

    return (
        cleaned_metadata,
        cleaned_investigators,
        cleaned_site_observations,
        cleaned_qualitative_site_observations,
    )


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def restructure_extraction(
    cleaned_metadata: pt.DataFrame[schema.FormMetadataCleaned],
    cleaned_investigators: pt.DataFrame[schema.InvestigatorsCleaned],
    cleaned_site_observations: pt.DataFrame[schema.SiteObservationsCleaned],
    cleaned_qualitative_site_observations: pt.DataFrame[
        schema.QualitativeSiteObservationsCleaned
    ],
) -> dict[str, Any]:
    """Restructure the cleaned extraction into a JSON schema.

    Args:
        cleaned_metadata: The cleaned metadata.
        cleaned_investigators: The cleaned investigators.
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
def load(restructured_json: dict[str, Any], output_dir: Path) -> Path:
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
