# Up to 4x faster than Series.str.contains / Series.eq - can handle Unicode!

```python
pip install a-pandas-ex-fast-string
```

```python
from a_pandas_ex_fast_string import pd_add_fast_string
import pandas as pd

pd_add_fast_string()

df2 = pd.read_csv(
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv",
    dtype="string",
)

# To check if it can handle unicode strings
df2.Name.iloc[0] += "ö"
df2.Name.iloc[10] += "ä"
df2.Name.iloc[20] += "ü"

# converts the whole dataframe
df900 = pd.Q_convert_to_fast_string(df2.copy())


dfone = df2.copy()
# converts one column
dfone.Cabin.ds_update_fast_string()

# Let's create some DataFrames of different sizes
df9000 = pd.Q_convert_to_fast_string(
    pd.concat([df2.copy() for _ in range(10)], ignore_index=True)
)
df90000 = pd.Q_convert_to_fast_string(
    pd.concat([df2.copy() for _ in range(100)], ignore_index=True)
)
df900000 = pd.Q_convert_to_fast_string(
    pd.concat([df2.copy() for _ in range(1000)], ignore_index=True)
)
df9000000 = pd.Q_convert_to_fast_string(
    pd.concat([df2.copy() for _ in range(10000)], ignore_index=True)
)



%timeit df900.loc[df900.Name.s_string_contains('y') | df900.Name.s_string_is('Montvila, Rev. Juozas')]
%timeit df900.loc[df900.Name.str.contains('y',regex=False) | (df900.Name == 'Montvila, Rev. Juozas')]
604 µs ± 9.09 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
997 µs ± 13.2 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)


%timeit df9000.loc[df9000.Name.s_string_contains('y') | df9000.Name.s_string_is('Montvila, Rev. Juozas')]
%timeit df9000.loc[df9000.Name.str.contains('y',regex=False) | (df9000.Name == 'Montvila, Rev. Juozas')]
1.15 ms ± 15.2 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
2.77 ms ± 11.2 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)


%timeit df90000.loc[df90000.Name.s_string_contains('y') | df90000.Name.s_string_is('Montvila, Rev. Juozas')]
%timeit df90000.loc[df90000.Name.str.contains('y',regex=False) | (df90000.Name == 'Montvila, Rev. Juozas')]
6.45 ms ± 77.4 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
20.7 ms ± 166 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)


%timeit df900000.loc[df900000.Name.s_string_contains('y') | df900000.Name.s_string_is('Montvila, Rev. Juozas')]
%timeit df900000.loc[df900000.Name.str.contains('y',regex=False) | (df900000.Name == 'Montvila, Rev. Juozas')]
60.5 ms ± 853 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
206 ms ± 840 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)


%timeit df9000000.loc[df9000000.Name.s_string_contains('y') | df9000000.Name.s_string_is('Montvila, Rev. Juozas')]
%timeit df9000000.loc[df9000000.Name.str.contains('y',regex=False) | (df9000000.Name == 'Montvila, Rev. Juozas')]
596 ms ± 11.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
2.06 s ± 2.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)


# Good news: it can handle unicode characters! 
df9000.loc[df9000.Name.s_string_contains('ö')].Name
Out[14]: 
0       Braund, Mr. Owen Harrisö
891     Braund, Mr. Owen Harrisö
1782    Braund, Mr. Owen Harrisö
2673    Braund, Mr. Owen Harrisö
3564    Braund, Mr. Owen Harrisö
4455    Braund, Mr. Owen Harrisö
5346    Braund, Mr. Owen Harrisö
6237    Braund, Mr. Owen Harrisö
7128    Braund, Mr. Owen Harrisö
8019    Braund, Mr. Owen Harrisö
Name: Name, dtype: string


# Bad news: every time you modify a Series, you have to update it: 

df9000.loc[df9000.Name.s_string_contains('ö')].Name
0       Braund, Mr. Owen Harrisö
891     Braund, Mr. Owen Harrisö
1782    Braund, Mr. Owen Harrisö
2673    Braund, Mr. Owen Harrisö
3564    Braund, Mr. Owen Harrisö


df9000.loc[df9000.Name.s_string_contains('ö'), "Name"] = df9000.loc[df9000.Name.s_string_contains('ö'), "Name"] + 'Ä' # updating 

df9000.Name
0                               Braund, Mr. Owen HarrisöÄ
1       Cumings, Mrs. John Bradley (Florence Briggs Th...
2                                  Heikkinen, Miss. Laina

df9000.loc[df9000.Name.s_string_contains('ö'), "Name"]  # Exception because ds_update_fast_string was not called

Traceback (most recent call last):
  File "C:\Users\Gamer\anaconda3\envs\dfdir\lib\site-packages\IPython\core\interactiveshell.py", line 3398, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-7-2b0dfaf8b41c>", line 1, in <cell line: 1>
    df9000.loc[df9000.Name.s_string_contains('ö'), "Name"]
  File "C:/Users/Gamer/anaconda3/envs/dfdir/a_pandas_string_search.py", line 133, in search_contains
    wordtosearchbin, columntosearch = _get_col_word(
  File "C:/Users/Gamer/anaconda3/envs/dfdir/a_pandas_string_search.py", line 103, in _get_col_word
    return wordtosearchbin, series._stringser.__array__()
AttributeError: 'NoneType' object has no attribute '__array__'

df9000.Name.ds_update_fast_string() # Necessary after changing a Series
# you can also update the whole DataFrame: df9000 = df9000.ds_update_fast_string()
# Be careful: df9000.Name.ds_update_fast_string() returns None (inplace) 
# df9000.ds_update_fast_string() returns a DataFrame

df9000.loc[df9000.Name.s_string_contains('ö'), "Name"]  # Now it is working!

0       Braund, Mr. Owen HarrisöÄ
891     Braund, Mr. Owen HarrisöÄ
1782    Braund, Mr. Owen HarrisöÄ
2673    Braund, Mr. Owen HarrisöÄ
```
