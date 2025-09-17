"""Checks across the whole schema, between tables, e.g. referential integrity."""

import pandera as pa
import pandera.typing as pt

from stormwater_monitoring_datasheet_extraction.lib import constants, schema


@pa.check_types(with_pydantic=True, lazy=True)
def validate_site_creek_map(
    site_type_map: pt.DataFrame[schema.Site],
    creek_type_map: pt.DataFrame[schema.Creek],
) -> None:
    """Validate the site and creek type maps.

    Checks mutual referential integrity.

    Args:
        site_type_map: A DataFrame mapping site IDs to their outfall types.
        creek_type_map: A DataFrame mapping creek site IDs to their creek types.
    """
    invalid_creeks = creek_type_map[
        ~creek_type_map.index.isin(site_type_map[constants.Columns.CREEK_SITE_ID])
    ]

    creek_sites = site_type_map[constants.Columns.OUTFALL_TYPE] == constants.OutfallType.CREEK
    invalid_creek_sites = site_type_map[
        ~(
            (
                creek_sites
                & site_type_map[constants.Columns.CREEK_SITE_ID].isin(creek_type_map.index)
            )
            | ~creek_sites
        )
    ]

    if not invalid_creeks.empty or not invalid_creek_sites.empty:
        error_messages = []
        if not invalid_creeks.empty:
            error_messages.append(
                f"Creek site IDs in creek_type_map not found in site_type_map: "
                f"{invalid_creeks.index.tolist()}"
            )
        if not invalid_creek_sites.empty:
            error_messages.append(
                f"Creek site IDs in site_type_map not in creek_type_map: "
                f"{invalid_creek_sites.index.tolist()}"
            )
        raise ValueError(" ; ".join(error_messages))
