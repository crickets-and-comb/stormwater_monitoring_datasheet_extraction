"""Schema field checks."""

import pandas as pd
from pandera import extensions


@extensions.register_check_method(statistics=["format"])
def is_valid_date(series: pd.Series, format: str) -> bool:
    """Every value parses with the given format."""
    parsed = pd.to_datetime(series, format=format)
    return parsed.notna().all()


@extensions.register_check_method(statistics=["flag"])
def date_le_today(series: pd.Series, flag: bool) -> bool:
    """Every date is on or before today."""
    parsed = pd.to_datetime(series)
    return parsed.notna().all() and (parsed <= pd.Timestamp.today()).all() if flag else True
