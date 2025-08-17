"""Schema dataframe checks."""

import pandas as pd
from pandera import extensions


# TODO: Abstract to `comb_utils`.
@extensions.register_check_method(statistics=["pk_cols"])
def pk_check(df: pd.DataFrame, pk_cols: list[str]) -> bool:
    """Assert that a DataFrame is unique on the primary key columns."""
    return not df[pk_cols].duplicated().any()
