"""Schema dataframe checks."""

from typing import cast

import pandas as pd
from pandera.typing import Series


def datetime_le_now(
    df: pd.DataFrame,
    date_col: str,
    time_col: str,
    date_format: str,
    time_format: str,
) -> Series[bool]:
    """Checks if each date:time is on or before now.

    Arguments:
        df: The DataFrame containing the date and time columns.
        date_col: The name of the date column.
        time_col: The name of the time column.
        date_format: The format string for parsing the date.
        time_format: The format string for parsing the time.

    Return:
        A boolean Series indicating whether each date:time is on or before now.
    """
    dt_df = df[[date_col, time_col]].copy()
    dt_df[date_col] = pd.to_datetime(dt_df[date_col], format=date_format, errors="coerce")
    dt_df[time_col] = pd.to_datetime(dt_df[time_col], format=time_format, errors="coerce")
    dt_df["date_time_series"] = dt_df[date_col] + dt_df[time_col].dt.time
    now = pd.Timestamp.now()

    is_valid = dt_df["date_time_series"] <= now
    is_valid = cast("Series[bool]", is_valid)

    return is_valid
