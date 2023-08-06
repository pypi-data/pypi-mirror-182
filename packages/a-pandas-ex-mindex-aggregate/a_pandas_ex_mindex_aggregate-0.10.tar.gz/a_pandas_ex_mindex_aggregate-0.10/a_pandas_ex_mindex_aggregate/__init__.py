import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame


def aggra_pandas(df, col_names):
    # based on: https://stackoverflow.com/a/66018377/15096247
    if not isinstance(col_names, list):
        col_names = [col_names]
    values = df.sort_values(col_names).values.T
    col_idcs = tuple(df.columns.get_loc(cn) for cn in col_names)
    other_col_names = tuple(
        name for idx, name in enumerate(df.columns) if idx not in col_idcs
    )
    other_col_idcs = tuple(df.columns.get_loc(cn) for cn in other_col_names)
    keys = values[col_idcs, :]
    vals = values[other_col_idcs, :]
    multikeys = tuple(zip(*keys))
    ukeys, index = np.unique(multikeys, return_index=True, axis=0)
    return pd.DataFrame(
        data={
            tup[-1]: tup[:-1]
            for tup in zip(*np.split(vals, index[1:], axis=1), other_col_names)
        },
        index=pd.MultiIndex.from_arrays(ukeys.T, names=col_names),
    )


def pd_add_mindex_aggregate():
    DataFrame.d_multiindex_aggregate = aggra_pandas
