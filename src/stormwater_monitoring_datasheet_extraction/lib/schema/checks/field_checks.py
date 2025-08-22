"""Schema field checks."""

from typing import cast

import pandas as pd
from pandera.typing import Series
from typeguard import typechecked

# TODO: An alternative approach would be to create custom classes for the field types,
# handle validation in the class constructor, and then coerce the field to the class.
# This may allow us to generate better error messages, and may be more flexible
# for future changes.
# Consider doing this.
# On the other hand, would also be vulnerable to changes in nullability. If we find out a
# field can be null, and we've made a custom class to carry out our validations, we'd need
# to then coerce the null into the class, which in itself could be tricky, and which would
# also mean we'd end up with a non-null value, even if empty. (In other words, we'd get too
# "Pythonic" for real data integrity.)
# Also, we'd end up having field validations in multiple places unless we chose one approach
# or the other.


@typechecked
def is_valid_date(series: Series, date_format: str) -> Series[bool]:
    """Every date parses with the given format."""
    parsed = pd.to_datetime(series, format=date_format, errors="coerce")
    is_valid = parsed.notna()
    is_valid = cast("Series[bool]", is_valid)
    return is_valid


@typechecked
def date_le_today(series: Series) -> Series[bool]:
    """Every date is on or before today."""
    parsed = pd.to_datetime(series, errors="coerce")
    is_valid = parsed.notna() and parsed <= pd.Timestamp.today()
    is_valid = cast("Series[bool]", is_valid)
    return is_valid


@typechecked
def is_valid_time(series: Series, format: str) -> Series[bool]:
    """Every time parses with the given format."""
    parsed = pd.to_datetime(series, format=format, errors="coerce").dt.time
    is_valid = parsed.notna()
    is_valid = cast("Series[bool]", is_valid)
    return is_valid
