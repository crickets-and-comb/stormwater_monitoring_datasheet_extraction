"""Database tables as constants."""

from typing import Final

import pandas as pd
import pandera.typing as pt

from stormwater_monitoring_datasheet_extraction.lib.constants import (
    Columns,
    CreekType,
    OutfallType,
)
from stormwater_monitoring_datasheet_extraction.lib.schema import schema

_sites = pd.DataFrame(
    columns=[Columns.SITE_ID, Columns.OUTFALL_TYPE],
    data=[
        ("Little Squalicum Creek", OutfallType.CREEK),
        ("Squalicum Creek", OutfallType.CREEK),
        ("Whatcom Creek", OutfallType.CREEK),
        ("Broadway", OutfallType.OUTFALL),
        ("C Street", OutfallType.OUTFALL),
        ("Cornwall", OutfallType.OUTFALL),
        ("Cedar", OutfallType.OUTFALL),
        ("Oliver", OutfallType.OUTFALL),
        ("Bennett", OutfallType.OUTFALL),
        ("Padden", OutfallType.CREEK),
    ],
)
_sites[Columns.CREEK_SITE_ID] = _sites.apply(
    lambda row: (
        row[Columns.SITE_ID] if row[Columns.OUTFALL_TYPE] == OutfallType.CREEK else pd.NA
    ),
    axis=1,
)
_sites.set_index(Columns.SITE_ID, inplace=True)

SITES: Final[pt.DataFrame[schema.Site]] = pt.DataFrame[schema.Site](_sites)

_creeks = _sites[_sites[Columns.OUTFALL_TYPE] == OutfallType.CREEK].copy()
_creeks[Columns.CREEK_TYPE] = CreekType.SPAWN
CREEKS: Final[pt.DataFrame[schema.Creek]] = pt.DataFrame[schema.Creek](
    _creeks[[Columns.CREEK_TYPE]]
)

del _sites, _creeks
