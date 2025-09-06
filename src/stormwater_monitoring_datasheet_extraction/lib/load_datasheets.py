"""Top-level module for stormwater monitoring datasheet ETL."""

import logging
from pathlib import Path
from typing import Any, cast

import pandas as pd
import pandera as pa
import pandera.typing as pt
from typeguard import typechecked

# from stormwater_monitoring_datasheet_extraction.lib import schema
from stormwater_monitoring_datasheet_extraction.lib.constants import DocStrings

# TODO: To check observations threshholds, need a site-type map:
# creek or outfall, and if creek:
# habitat, spawn, rear, or migrate.

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_etl(input_dir: Path, output_dir: Path) -> Path:  # noqa: D103
    return Path()
# @typechecked
# def run_etl(input_dir: Path, output_dir: Path) -> Path:  # noqa: D103
    # logger.info("Starting ETL process...")

#     # TODO, NOTE: This is an estimated outline, not a hard requirement.
#     # We may need to adjust the steps based on the actual implementation details.
#     (
#         raw_form_metadata,
#         raw_investigators,
#         raw_site_visits,
#         raw_quantitative_observations,
#         raw_qualitative_observations,
#     ) = extract(input_dir=input_dir)

#     (
#         precleaned_form_metadata,
#         precleaned_investigators,
#         precleaned_site_visits,
#         precleaned_quantitative_observations,
#         precleaned_qualitative_observations,
#     ) = preclean(
#         raw_form_metadata=raw_form_metadata,
#         raw_investigators=raw_investigators,
#         raw_site_visits=raw_site_visits,
#         raw_quantitative_observations=raw_quantitative_observations,
#         raw_qualitative_observations=raw_qualitative_observations,
#     )

#     (
#         verified_form_metadata,
#         verified_investigators,
#         verified_site_visits,
#         verified_quantitative_observations,
#         verified_qualitative_observations,
#     ) = verify(
#         precleaned_form_metadata=precleaned_form_metadata,
#         precleaned_investigators=precleaned_investigators,
#         precleaned_site_visits=precleaned_site_visits,
#         precleaned_quantitative_observations=precleaned_quantitative_observations,
#         precleaned_qualitative_observations=precleaned_qualitative_observations,
#     )

#     (
#         cleaned_form_metadata,
#         cleaned_investigators,
#         cleaned_site_visits,
#         cleaned_quantitative_observations,
#         cleaned_qualitative_observations,
#     ) = clean(
#         verified_form_metadata=verified_form_metadata,
#         verified_investigators=verified_investigators,
#         verified_site_visits=verified_site_visits,
#         verified_quantitative_observations=verified_quantitative_observations,
#         verified_qualitative_observations=verified_qualitative_observations,
#     )

#     restructured_json = restructure_extraction(
#         cleaned_form_metadata=cleaned_form_metadata,
#         cleaned_investigators=cleaned_investigators,
#         cleaned_site_visits=cleaned_site_visits,
#         cleaned_quantitative_observations=cleaned_quantitative_observations,
#         cleaned_qualitative_observations=cleaned_qualitative_observations,
#     )

#     final_output_path = load(restructured_json=restructured_json, output_dir=output_dir)

#     return final_output_path


# run_etl.__doc__ = DocStrings.RUN_ETL.api_docstring


# # TODO: Implement this.
# @pa.check_types(with_pydantic=True, lazy=True)
# def extract(
#     input_dir: Path,
# ):
#     # def extract(
#     #     input_dir: Path,
#     # ) -> tuple[
#     #     pt.DataFrame[schema.FormExtracted],
#     #     pt.DataFrame[schema.FormInvestigatorExtracted],
#     #     pt.DataFrame[schema.SiteVisitExtracted],
#     #     pt.DataFrame[schema.QuantitativeObservationsExtracted],
#     #     pt.DataFrame[schema.QualitativeObservationsExtracted],
#     # ]:
#     """Extracts data from the images in the input directory.

#     Using computer vision, extracts data from datasheets.

#     Args:
#         input_dir: Path to the directory containing the datasheet images.

#     Returns:
#         Raw extraction split into normalized relational tables, with no enforcement.
#     """
#     logger.info(f"Extracting data from images in {input_dir} ...")

#     # TODO: When implementing, you can just make a pandas.DataFrame. No need to cast.
#     # It will cast and validate on return.
#     raw_form_metadata = cast("pt.DataFrame[schema.FormExtracted]", pd.DataFrame())
#     raw_investigators = cast("pt.DataFrame[schema.FormInvestigatorExtracted]", pd.DataFrame())
#     raw_site_visits = cast("pt.DataFrame[schema.SiteVisitExtracted]", pd.DataFrame())
#     raw_quantitative_observations = cast(
#         "pt.DataFrame[schema.QuantitativeObservationsExtracted]", pd.DataFrame()
#     )
#     raw_qualitative_observations = cast(
#         "pt.DataFrame[schema.QualitativeObservationsExtracted]", pd.DataFrame()
#     )
#     # TODO: Use data definition as source of truth rather than schema.
#     ...

#     return (
#         raw_form_metadata,
#         raw_investigators,
#         raw_site_visits,
#         raw_quantitative_observations,
#         raw_qualitative_observations,
#     )


# # TODO: Implement this.
# def preclean(
#     raw_form_metadata,
#     raw_investigators,
#     raw_site_visits,
#     raw_quantitative_observations,
#     raw_qualitative_observations,
# ):
#     # def preclean(
#     #     raw_form_metadata: pt.DataFrame[schema.FormExtracted],
#     #     raw_investigators: pt.DataFrame[schema.FormInvestigatorExtracted],
#     #     raw_site_visits: pt.DataFrame[schema.SiteVisitExtracted],
#     #     raw_quantitative_observations: pt.DataFrame[schema.QuantitativeObservationsExtracted],
#     #     raw_qualitative_observations: pt.DataFrame[schema.QualitativeObservationsExtracted],
#     # ) -> tuple[
#     #     pt.DataFrame[schema.FormPrecleaned],
#     #     pt.DataFrame[schema.FormInvestigatorPrecleaned],
#     #     pt.DataFrame[schema.SiteVisitPrecleaned],
#     #     pt.DataFrame[schema.QuantitativeObservationsPrecleaned],
#     #     pt.DataFrame[schema.QualitativeObservationsPrecleaned],
#     # ]:
#     """Preclean the raw extraction.

#     Args:
#         raw_form_metadata: Metadata extracted from the datasheets.
#         raw_investigators: FormInvestigator extracted from the datasheets.
#         raw_site_visits: Site observations extracted from the datasheets.
#         raw_quantitative_observations:
#             Quantitative site observations extracted from the datasheets.
#         raw_qualitative_observations:
#             Qualitative site observations extracted from the datasheets.

#     Returns:
#         Precleaned relational tables, with no enforcement.
#     """
#     logger.info("Precleaning raw extraction data...")

#     # TODO: Light cleaning before user verification.
#     # E.g., strip whitespace, try to cast/format, check range, but warn don't fail.
#     # Much of this might be done by creating a custom class for each field
#     # that cleans and warns on construction,
#     # define __str__/__repr__/__int__ etc. as needed,
#     # and use the class as a type in the schema to coerce the data.
#     # Use data definition as source of truth rather than schema.
#     # TODO: When implementing, you can just make a pandas.DataFrame. No need to cast.
#     # It will cast and validate on return.
#     precleaned_form_metadata = cast("pt.DataFrame[schema.FormPrecleaned]", raw_form_metadata)
#     precleaned_investigators = cast(
#         "pt.DataFrame[schema.FormInvestigatorPrecleaned]", raw_investigators
#     )
#     precleaned_site_visits = cast("pt.DataFrame[schema.SiteVisitPrecleaned]", raw_site_visits)
#     precleaned_quantitative_observations = cast(
#         "pt.DataFrame[schema.QuantitativeObservationsPrecleaned]",
#         raw_quantitative_observations,
#     )
#     precleaned_qualitative_observations = cast(
#         "pt.DataFrame[schema.QualitativeObservationsPrecleaned]",
#         raw_qualitative_observations,
#     )
#     ...

#     return (
#         precleaned_form_metadata,
#         precleaned_investigators,
#         precleaned_site_visits,
#         precleaned_quantitative_observations,
#         precleaned_qualitative_observations,
#     )


# # TODO: Implement this.
# @pa.check_types(with_pydantic=True, lazy=True)
# def verify(
#     precleaned_form_metadata,
#     precleaned_investigators,
#     precleaned_site_visits,
#     precleaned_quantitative_observations,
#     precleaned_qualitative_observations,
# ):
#     # def verify(
#     #     precleaned_form_metadata: pt.DataFrame[schema.FormPrecleaned],
#     #     precleaned_investigators: pt.DataFrame[schema.FormInvestigatorPrecleaned],
#     #     precleaned_site_visits: pt.DataFrame[schema.SiteVisitPrecleaned],
#     #     precleaned_quantitative_observations: pt.DataFrame[
#     #         schema.QuantitativeObservationsPrecleaned
#     #     ],
#     #     precleaned_qualitative_observations: pt.DataFrame[
#     #         schema.QualitativeObservationsPrecleaned
#     #     ],
#     # ) -> tuple[
#     #     pt.DataFrame[schema.FormVerified],
#     #     pt.DataFrame[schema.FormInvestigatorVerified],
#     #     pt.DataFrame[schema.SiteVisitVerified],
#     #     pt.DataFrame[schema.QuantitativeObservationsVerified],
#     #     pt.DataFrame[schema.QualitativeObservationsVerified],
#     # ]:
#     """Verifies the raw extraction with the user.

#     Prompts user to check each image against each extraction and edit as needed.

#     Args:
#         precleaned_form_metadata: The precleaned metadata.
#         precleaned_investigators: The precleaned investigators.
#         precleaned_site_visits: The precleaned site observations.
#         precleaned_quantitative_observations:
#             The precleaned quantitative site observations.
#         precleaned_qualitative_observations:
#             The precleaned qualitative site observations.

#     Returns:
#         User-verified relational tables, with some enforcement.
#     """
#     logger.info("Verifying precleaned data with user...")

#     # TODO: When implementing, you can just make a pandas.DataFrame. No need to cast.
#     # It will cast and validate on return.
#     verified_form_metadata = cast(
#         "pt.DataFrame[schema.FormVerified]", precleaned_form_metadata
#     )
#     verified_investigators = cast(
#         "pt.DataFrame[schema.FormInvestigatorVerified]", precleaned_investigators
#     )
#     verified_site_visits = cast(
#         "pt.DataFrame[schema.SiteVisitVerified]", precleaned_site_visits
#     )
#     verified_quantitative_observations = cast(
#         "pt.DataFrame[schema.QuantitativeObservationsVerified]",
#         precleaned_quantitative_observations,
#     )
#     verified_qualitative_observations = cast(
#         "pt.DataFrame[schema.QualitativeObservationsVerified]",
#         precleaned_qualitative_observations,
#     )
#     ...
#     # TODO: Offer some immediate feedback:
#     # Offer enumerated options for categorical data.
#     # Highlight invalid extracted fields as they come to user's focus.
#     # Ask for reentry if entered/verified can't be typed correctly or is out of range.
#     # Warn and offer to re-enter if out of expected range but within valid range.
#     # Use data definition as source of truth rather than schema.

#     return (
#         verified_form_metadata,
#         verified_investigators,
#         verified_site_visits,
#         verified_quantitative_observations,
#         verified_qualitative_observations,
#     )


# # TODO: Implement this.
# @pa.check_types(with_pydantic=True, lazy=True)
# def clean(
#     verified_form_metadata,
#     verified_investigators,
#     verified_site_visits,
#     verified_quantitative_observations,
#     verified_qualitative_observations,
# ):
#     # def clean(
#     #     verified_form_metadata: pt.DataFrame[schema.FormVerified],
#     #     verified_investigators: pt.DataFrame[schema.FormInvestigatorVerified],
#     #     verified_site_visits: pt.DataFrame[schema.SiteVisitVerified],
#     #     verified_quantitative_observations: pt.DataFrame[schema.QuantitativeObservationsVerified],
#     #     verified_qualitative_observations: pt.DataFrame[schema.QualitativeObservationsVerified],
#     # ) -> tuple[
#     #     pt.DataFrame[schema.FormCleaned],
#     #     pt.DataFrame[schema.FormInvestigatorCleaned],
#     #     pt.DataFrame[schema.SiteVisitCleaned],
#     #     pt.DataFrame[schema.QuantitativeObservationsCleaned],
#     #     pt.DataFrame[schema.QualitativeObservationsCleaned],
#     # ]:
#     """Clean the user-verified extraction.

#     Clean and validates the user-verified extraction data, ensuring it is in a consistent
#     format, appropriate data types, within specified ranges, etc., and ready to load.

#     Args:
#         verified_form_metadata: The user-verified metadata.
#         verified_investigators: The user-verified investigators.
#         verified_site_visits: The user-verified site observations.
#         verified_quantitative_observations: The user-verified quantitative site observations.
#         verified_qualitative_observations: The user-verified qualitative site observations.

#     Returns:
#         Cleaned relational tables, with full enforcement.
#     """
#     logger.info("Cleaning verified data...")

#     # TODO: When implementing, you can just make a pandas.DataFrame. No need to cast.
#     # It will cast and validate on return.
#     cleaned_form_metadata = cast("pt.DataFrame[schema.FormCleaned]", verified_form_metadata)
#     cleaned_investigators = cast(
#         "pt.DataFrame[schema.FormInvestigatorCleaned]", verified_investigators
#     )
#     cleaned_site_visits = cast("pt.DataFrame[schema.SiteVisitCleaned]", verified_site_visits)
#     cleaned_quantitative_observations = cast(
#         "pt.DataFrame[schema.QuantitativeObservationsCleaned]",
#         verified_quantitative_observations,
#     )
#     cleaned_qualitative_observations = cast(
#         "pt.DataFrame[schema.QualitativeObservationsCleaned]",
#         verified_qualitative_observations,
#     )
#     ...
#     # TODO: Inferred/courtesy imputations? (nulls/empties, don't overstep)

#     # TODO: Validations schema can't accomplish:
#     # - Referential integrity.
#     # - Ideally, we would verify that site arrival times are within
#     #   the investigator's start and end times, but we can't 100% do that
#     #   because forms don't assign observations to investigators.
#     # - FormInvestigator start/end datetimes < now.
#     # - SiteMetadata arrival datetime < now.
#     # - No dry outfalls in observations tables.

#     # TODO: If still invalid, alert to the problem, and re-call `verify()`.
#     # Use data definition as source of truth rather than schema.

#     return (
#         cleaned_form_metadata,
#         cleaned_investigators,
#         cleaned_site_visits,
#         cleaned_quantitative_observations,
#         cleaned_qualitative_observations,
#     )


# # TODO: Implement this.
# @pa.check_types(with_pydantic=True, lazy=True)
# def restructure_extraction(
#     cleaned_form_metadata,
#     cleaned_investigators,
#     cleaned_site_visits,
#     cleaned_quantitative_observations,
#     cleaned_qualitative_observations,
# ):
#     # def restructure_extraction(
#     #     cleaned_form_metadata: pt.DataFrame[schema.FormCleaned],
#     #     cleaned_investigators: pt.DataFrame[schema.FormInvestigatorCleaned],
#     #     cleaned_site_visits: pt.DataFrame[schema.SiteVisitCleaned],
#     #     cleaned_quantitative_observations: pt.DataFrame[schema.QuantitativeObservationsCleaned],
#     #     cleaned_qualitative_observations: pt.DataFrame[schema.QualitativeObservationsCleaned],
#     # ) -> dict[str, Any]:
#     """Restructure the cleaned extraction into a JSON schema.

#     Args:
#         cleaned_form_metadata: The cleaned metadata.
#         cleaned_investigators: The cleaned investigators.
#         cleaned_site_visits: The cleaned site observations.
#         cleaned_quantitative_observations: The cleaned quantitative site observations.
#         cleaned_qualitative_observations: The cleaned qualitative site observations.

#     Returns:
#         Cleaned relational tables restructured into JSON schema.
#     """
#     logger.info("Restructuring cleaned data into JSON schema...")

#     restructured_json = {}

#     ...
#     return restructured_json


# # TODO: Implement this.
# @typechecked
# def load(restructured_json: dict[str, Any], output_dir: Path) -> Path:
#     """Load the cleaned data into the output directory.

#     Saves the cleaned data to the specified output directory in a structured format.
#     If the output directory does not exist, it will be created.

#     Args:
#         restructured_json: The restructured JSON schema.
#         output_dir: The directory where the cleaned data will be saved.
#             If empty path, defaults to a dated directory in the current working directory.

#     Returns:
#         Path to the saved cleaned data file.
#     """
#     logger.info(f"Loading cleaned data to {output_dir} ...")

#     final_output_path = Path()

#     ...

#     return final_output_path
