"""Database read utilities and queries."""

import pandera as pa
import pandera.typing as pt

from stormwater_monitoring_datasheet_extraction.lib import constants, schema


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def get_site_type_map() -> pt.DataFrame[schema.Site]:
    """Reads in the site type map."""
    site_type_map = constants.SITES

    return site_type_map


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def get_creek_type_map() -> pt.DataFrame[schema.Creek]:
    """Reads in the creek type map."""
    creek_type_map = constants.CREEKS
    return creek_type_map
