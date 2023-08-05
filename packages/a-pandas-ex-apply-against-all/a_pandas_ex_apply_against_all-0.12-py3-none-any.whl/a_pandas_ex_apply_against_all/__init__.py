from typing import Union, Any

import pandas as pd
from pandas.core.frame import Series


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


def apply_each_value_to_whole_column(
    df: pd.Series,
    expression: str,
    func=None,
    exception_value: Any = pd.NA,
    diagonal_value: Any = pd.NA,
    print_exception: bool = True,
    ignore_exceptions=True,
) -> pd.DataFrame:
    def execute_function(
        colname,
        ini_,
        df,
        expression,
        xx,
        diagonal_value,
        func,
        exception_value=pd.NA,
        ignore_exceptions=True,
    ):
        result = []
        for ini, y in zip(df.index, df):
            try:
                x = xx[colname]
                val = eval(expression) if ini != ini_ else diagonal_value
                result.append(val)
            except Exception as fe:
                if not ignore_exceptions:
                    raise fe
                if print_exception:
                    print(fe)
                result.append(exception_value)
        return pd.Series(result)

    dfapp, isseries = series_to_dataframe(df)
    colname = dfapp.columns[0]
    df4 = dfapp.apply(
        lambda xx: execute_function(
            colname,
            xx.name,
            df,
            expression,
            xx,
            diagonal_value,
            func,
            exception_value=exception_value,
            ignore_exceptions=ignore_exceptions,
        ),
        axis=1,
    )
    df4.columns = df.index.__array__().copy()
    return df4


def pd_add_apply_each():
    Series.s_apply_each = apply_each_value_to_whole_column