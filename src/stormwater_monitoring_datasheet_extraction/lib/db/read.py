"""Database read utilities and queries."""

import pandera as pa
import pandera.typing as pt

from stormwater_monitoring_datasheet_extraction.lib import schema
from stormwater_monitoring_datasheet_extraction.lib.db import tables


# NOTE: At some point, these will return tables from a database that we don't manage.
# So, we'll continue to use the pandera schema here.
# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def get_site_type_map() -> pt.DataFrame[schema.Site]:
    """Reads in the site type map."""
    site_type_map = tables.SITES

    return site_type_map


# TODO: Implement this.
@pa.check_types(with_pydantic=True, lazy=True)
def get_creek_type_map() -> pt.DataFrame[schema.Creek]:
    """Reads in the creek type map."""
    creek_type_map = tables.CREEKS
    return creek_type_map
