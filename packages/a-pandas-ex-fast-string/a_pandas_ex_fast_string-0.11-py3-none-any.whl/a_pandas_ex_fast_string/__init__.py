import numexpr
import pandas as pd
import ujson
from pandas.core.frame import DataFrame, Series


def update_string_df(
    df,
    ensure_ascii=True,
    encode_html_chars=True,
    escape_forward_slashes=False,
    allow_nan=True,
):
    return load_df_and_add_string(
        df,
        ensure_ascii=ensure_ascii,
        encode_html_chars=encode_html_chars,
        escape_forward_slashes=escape_forward_slashes,
        allow_nan=allow_nan,
    )


def update_string_series(
    df,
    ensure_ascii=True,
    encode_html_chars=True,
    escape_forward_slashes=False,
    allow_nan=True,
):
    df._stringser = (
        df.fillna("")
        .astype("string")
        .apply(
            lambda x: encode_ujson(
                x,
                ensure_ascii,
                encode_html_chars,
                escape_forward_slashes,
                allow_nan,
            )
        )
        .__array__()
        .astype("a")
    )


def encode_ujson(
    x,
    ensure_ascii=True,
    encode_html_chars=True,
    escape_forward_slashes=False,
    allow_nan=True,
):
    return ujson.encode(
        x,
        ensure_ascii=ensure_ascii,
        encode_html_chars=encode_html_chars,
        escape_forward_slashes=escape_forward_slashes,
        allow_nan=allow_nan,
    )[1:-1].encode()


def load_df_and_add_string(
    df,
    ensure_ascii=True,
    encode_html_chars=True,
    escape_forward_slashes=False,
    allow_nan=True,
):
    dfstri = df.fillna("").astype("string")
    dfstri = dfstri.applymap(
        lambda x: encode_ujson(
            x,
            ensure_ascii,
            encode_html_chars,
            escape_forward_slashes,
            allow_nan,
        )
    )

    for col in dfstri:
        df[col]._stringser = dfstri[col].__array__().astype("a")
    return df


def _get_col_word(
    series,
    wanted_string,
    ensure_ascii=True,
    encode_html_chars=True,
    escape_forward_slashes=False,
    allow_nan=True,
):
    wordtosearchbin = ujson.encode(
        wanted_string,
        ensure_ascii=ensure_ascii,
        encode_html_chars=encode_html_chars,
        escape_forward_slashes=escape_forward_slashes,
        allow_nan=allow_nan,
    )[1:-1].encode()
    return wordtosearchbin, series._stringser.__array__()


def search_exact_string(
    series,
    wanted_string,
    ensure_ascii=True,
    encode_html_chars=True,
    escape_forward_slashes=False,
    allow_nan=True,
):
    wordtosearchbin, columntosearch = _get_col_word(
        series,
        wanted_string,
        ensure_ascii=ensure_ascii,
        encode_html_chars=encode_html_chars,
        escape_forward_slashes=escape_forward_slashes,
        allow_nan=allow_nan,
    )
    return numexpr.evaluate("wordtosearchbin == columntosearch")


def search_contains(
    series,
    wanted_string,
    ensure_ascii=True,
    encode_html_chars=True,
    escape_forward_slashes=False,
    allow_nan=True,
):
    wordtosearchbin, columntosearch = _get_col_word(
        series,
        wanted_string,
        ensure_ascii=ensure_ascii,
        encode_html_chars=encode_html_chars,
        escape_forward_slashes=escape_forward_slashes,
        allow_nan=allow_nan,
    )
    return numexpr.evaluate("contains(columntosearch, wordtosearchbin)")


def pd_add_fast_string():
    Series._stringser = None
    pd.Q_convert_to_fast_string = load_df_and_add_string
    DataFrame.ds_update_fast_string = update_string_df
    Series.ds_update_fast_string = update_string_series
    Series.s_string_contains = search_contains
    Series.s_string_is = search_exact_string
