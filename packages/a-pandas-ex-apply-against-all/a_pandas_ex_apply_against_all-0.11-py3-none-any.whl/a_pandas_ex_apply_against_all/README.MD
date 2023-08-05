# Apply each value in a column against the whole column

```python
pip install a-pandas-ex-apply-against-all
```

```python

from a_pandas_ex_apply_against_all import pd_add_apply_each
import pandas as pd
pd_add_apply_each()
df = pd.read_csv(
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
)
df1 = df.PassengerId.s_apply_each(
    expression="str(x) + str(y)", # use always x/y in your expression
    exception_value=pd.NA,
    diagonal_value=pd.NA,
    print_exception=True,
)
print(df1)
      0     1     2     3     4    ...     886     887     888     889     890
0    <NA>    12    13    14    15  ...    1887    1888    1889    1890    1891
1      21  <NA>    23    24    25  ...    2887    2888    2889    2890    2891
2      31    32  <NA>    34    35  ...    3887    3888    3889    3890    3891
3      41    42    43  <NA>    45  ...    4887    4888    4889    4890    4891
4      51    52    53    54  <NA>  ...    5887    5888    5889    5890    5891
..    ...   ...   ...   ...   ...  ...     ...     ...     ...     ...     ...
886  8871  8872  8873  8874  8875  ...    <NA>  887888  887889  887890  887891
887  8881  8882  8883  8884  8885  ...  888887    <NA>  888889  888890  888891
888  8891  8892  8893  8894  8895  ...  889887  889888    <NA>  889890  889891
889  8901  8902  8903  8904  8905  ...  890887  890888  890889    <NA>  890891
890  8911  8912  8913  8914  8915  ...  891887  891888  891889  891890    <NA>
[891 rows x 891 columns]

# If you use a non-built-in function, you have to pass it as an argument, and use it as "func" in your expression
# An example using shapely (merging different polygons)

from shapely.ops import unary_union
import shapely
polyshape = []
for k in range(10):
    xmin = k * 10 + 5
    ymin = k * 10 + 5
    xmax = k * 20 + 10
    ymax = k * 20 + 10
    coordsalls = [[xmin, ymin], [xmax, ymin], [xmax, ymax], [xmin, ymax], [xmin, ymin]]
    po = shapely.geometry.Polygon(coordsalls)
    polyshape.append(po)
df2 = pd.DataFrame(polyshape)
df1 = df2[0].s_apply_each(
    expression="func([x,y]) if x.intersects(y) else x", # use always x/y in your expression
    func=unary_union,
    exception_value=pd.NA,
    diagonal_value=pd.NA,
    print_exception=True,
    ignore_exceptions=True
)

```
