"""DataFrame checks."""

import pandas as pd
import pandera.extensions as extensions


# TODO: Abstract to `comb_utils`.
@extensions.register_check_method(statistics=["pk_cols"])
def pk_check(df: pd.DataFrame, pk_cols: list[str]) -> bool:
    """Assert that a DataFrame is unique on the primary key columns."""
    return df[pk_cols].drop_duplicates().shape[0] == df.shape[0]
