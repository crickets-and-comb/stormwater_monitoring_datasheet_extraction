"""Schema field checks."""

import pandas as pd
from pandera import extensions


@extensions.register_check_method(statistics=["format"])
def is_valid_date(series: pd.Series, format: str) -> bool:
    """Every value parses with the given strptime format."""
    parsed = pd.to_datetime(series, format=format)
    return parsed.notna().all()
