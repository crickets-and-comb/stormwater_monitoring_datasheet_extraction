"""Field checks."""

import pandas as pd
import pandera.extensions as extensions


# TODO: An alternative approach would be to create a custom class for the field type,
# handle validation in the class constructor, and then coerce the field to the class.
# This would allow us to generate better error messages, and would be more flexible
# for future changes.
# Consider doing this.
@extensions.register_check_method(statistics=["char_limit"])
def limit_char(pandas_obj: pd.Series, char_limit: int) -> bool:
    """Check that a string has at most `char_limit` characters."""
    return all(len(val) <= char_limit for val in pandas_obj)
