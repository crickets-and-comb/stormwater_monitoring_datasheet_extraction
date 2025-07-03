"""Top-level module for stormwater monitoring datasheet ETL."""

from pathlib import Path

from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib.constants import DocStrings


# TODO: Set up logging.
# TODO: Set up Pandera schema for each step.
@typechecked
def run_etl(input_dir: Path, output_dir: Path) -> Path:  # noqa: D103
    # TODO, NOTE: This is an estimate outline, not a hard requirement.
    # We may need to adjust the steps based on the actual implementation details.
    # For instance, we may want to add a cleaning step between raw extraction and user
    # verification.
    raw_extraction = extract(input_dir=input_dir)
    user_verified_extraction = verify(raw_extraction=raw_extraction)
    cleaned_extraction = clean(user_verified_extraction=user_verified_extraction)
    final_output_path = load(cleaned_data=cleaned_extraction, output_dir=output_dir)

    return final_output_path


run_etl.__doc__ = DocStrings.RUN_ETL.api_docstring

# TODO: Make return/input types more specific, using Pandera schemas or similar.


# TODO: Implement this.
@typechecked
def extract(input_dir: Path) -> dict:
    """Extracts data from the images in the input directory.

    Using computer vision extracts data from datasheets into JSON schema.

    Args:
        input_dir: Path to the directory containing the datasheet images.

    Returns:
        Raw extraction data in a NoSQL-esque format.
    """
    ...
    return {}


# TODO: Implement this.
@typechecked
def verify(raw_extraction: dict) -> dict:
    """Verifies the raw extraction with the user.

    Prompts user to check each image against each extraction and edit as needed.

    Args:
        raw_extraction: The raw extraction data from the datasheets in NoSQL-esque format..

    Returns:
        User verified extraction data in a NoSQL-esque format.
    """
    ...
    return {}


# TODO: Implement this.
@typechecked
def clean(user_verified_extraction: dict) -> dict:
    """Clean the user verified extraction.

    Clean and validates the user verified extraction data, ensuring it is in a consistent
    format, appropriate data types, within specified ranges, etc., and ready to load.

    Args:
        user_verified_extraction: The user verified extraction data in NoSQL-esque format.

    Returns:
        Cleaned extraction data in a NoSQL-esque format.
    """
    ...
    return {}


# TODO: Implement this.
@typechecked
def load(cleaned_data: dict, output_dir: Path) -> Path:
    """Load the cleaned data into the output directory.

    Saves the cleaned data to the specified output directory in a structured format.
    If the output directory does not exist, it will be created.

    Args:
        cleaned_data: The cleaned extraction data in NoSQL-esque format.
        output_dir: The directory where the cleaned data will be saved.
            If empty path, defaults to a dated directory in the current working directory.

    Returns:
        Path to the saved cleaned data file.
    """
    ...
    return Path("")
