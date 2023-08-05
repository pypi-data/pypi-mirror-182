import operator
from itertools import accumulate
from typing import Union
from pandas.core.frame import DataFrame, Series

import pandas as pd
import numpy as np


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


def iloc_split(
    dframe: Union[pd.DataFrame, pd.Series], splitindex: list
) -> Union[pd.Series, pd.DataFrame]:
    if not splitindex:
        return [dframe]
    df, isseries = series_to_dataframe(dframe)

    splitindex_final = [0] + splitindex + [len(df)]
    va1 = [
        df.iloc[splitindex_final[n] : splitindex_final[n + 1]]
        for n in range(len(splitindex_final) - 1)
    ]
    if isseries:
        va1 = [x[x.columns[0]] for x in va1]
    return va1


def loc_split(
    dframe: Union[pd.DataFrame, pd.Series], splitindex: list
) -> Union[pd.Series, pd.DataFrame]:

    if not splitindex:
        return [dframe]
    df, isseries = series_to_dataframe(dframe)

    indilist = df.index.to_list()
    splitindex_final = [indilist[0]] + splitindex + [indilist[-1]]
    va1 = [
        df.loc[splitindex_final[n] : splitindex_final[n + 1]]
        for n in range(len(splitindex_final) - 1)
    ]
    if isseries:
        va1 = [x[x.columns[0]] for x in va1]
    return va1


def iloc_split_pairs(
    dframe: Union[pd.DataFrame, pd.Series],
    splitindex: list[tuple],
    include_last: bool = True,
) -> Union[pd.Series, pd.DataFrame]:
    if not splitindex:
        return [dframe]
    df, isseries = series_to_dataframe(dframe)

    if not include_last:
        va1 = [df.iloc[n[0] : n[1]] for n in splitindex]
    else:
        va1 = [df.iloc[n[0] : n[1] + 1] for n in splitindex]
    if isseries:
        va1 = [x[x.columns[0]] for x in va1]
    return va1


def split_df_in_n_parts(df, n):
    return np.array_split(df, n)


def split_df_in_n_parts_of_length(
    dframe: Union[pd.DataFrame, pd.Series], size_of_each: int, exact_split: bool = True
) -> Union[pd.Series, pd.DataFrame]:
    if not exact_split:
        return np.array_split(dframe, np.floor(len(dframe) / size_of_each))
    else:
        df, isseries = series_to_dataframe(dframe)

        vari = len(df)
        howmany = size_of_each
        divmod_ = divmod(vari, howmany)
        splitlist = list(accumulate([howmany] * divmod_[0], operator.add))
        splitlist = [0] + splitlist + [len(df)]
        va1 = [
            df.iloc[splitlist[n] : splitlist[n + 1]] for n in range(len(splitlist) - 1)
        ]
        if isseries:
            va1 = [x[x.columns[0]] for x in va1]
        return va1


def pd_add_df_split():
    DataFrame.ds_split_in_n_parts_of_length = split_df_in_n_parts_of_length
    Series.ds_split_in_n_parts_of_length = split_df_in_n_parts_of_length
    DataFrame.ds_split_in_n_parts = split_df_in_n_parts
    Series.ds_split_in_n_parts = split_df_in_n_parts
    DataFrame.ds_iloc_split_pairwise = iloc_split_pairs
    Series.ds_iloc_split_pairwise = iloc_split_pairs
    DataFrame.ds_loc_split = loc_split
    Series.ds_loc_split = loc_split
    DataFrame.ds_iloc_split = iloc_split
    Series.ds_iloc_split = iloc_split
