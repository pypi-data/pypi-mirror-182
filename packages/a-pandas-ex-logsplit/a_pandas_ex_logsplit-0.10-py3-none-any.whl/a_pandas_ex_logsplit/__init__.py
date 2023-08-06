import itertools
import pandas as pd
from pandas.core.frame import DataFrame, Series


from typing import Union


def series_to_dataframe(
    df: Union[pd.Series, pd.DataFrame]
) -> (Union[pd.Series, pd.DataFrame], bool):
    dataf = df.copy()
    isseries = False
    if isinstance(dataf, pd.Series):
        columnname = dataf.name
        dataf = dataf.to_frame()

        try:
            dataf.columns = [columnname]
        except Exception:
            dataf.index = [columnname]
            dataf = dataf.T
        isseries = True

    return dataf, isseries


def log_split(*args):
    def logsplit(lst):
        # https://stackoverflow.com/a/35756376/15096247
        iterator = iter(lst)
        for n, e in enumerate(iterator):
            yield itertools.chain([e], itertools.islice(iterator, n))

    if len(args) > 1:
        for x in logsplit(zip(*args)):
            yield list(x)
    else:
        for x in logsplit(args[0]):
            yield list(x)


def pd_log_split(
    df: Union[pd.Series, pd.DataFrame],
    columns: Union[list, str,None] = None,
    includeindex: bool = False,
) -> list:
    if not isinstance(columns, list):
        columns = [columns]
    if not includeindex and isinstance(df, pd.DataFrame):
        return [
            list(l) if len(columns) > 1 else list([f[0] for f in l])
            for l in (list(log_split(zip(*[df[q].to_list() for q in df[columns]]))))
        ]
    else:
        dframe, _ = series_to_dataframe(df)
        columns = [dframe.columns[0]]
        dframe["___tmp___idx____"] = dframe.index.copy()
        columns.insert(0, "___tmp___idx____")

        return [
            list(l)
            for l in (
                list(log_split(zip(*[dframe[q].to_list() for q in dframe[columns]])))
            )
        ]


def pd_add_logsplit():
    DataFrame.ds_logsplit = pd_log_split
    Series.ds_logsplit = pd_log_split

