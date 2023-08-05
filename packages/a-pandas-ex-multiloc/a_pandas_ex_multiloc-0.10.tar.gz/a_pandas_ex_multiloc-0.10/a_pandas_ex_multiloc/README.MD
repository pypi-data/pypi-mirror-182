# Search for multiple values in multiple columns of a Pandas DataFrame

```python
pip install a-pandas-ex-multiloc
```

```python

from random import randrange
from a_pandas_ex_multiloc import pd_add_multiloc
import pandas as pd

pd_add_multiloc()
df = pd.DataFrame(
    [(randrange(0, 256), randrange(0, 256), randrange(0, 256)) for k in range(100000)],
    columns=["r", "g", "b"],
)



df.d_multiloc(
    column_and_values=[
        (
            "==",
            ("r", "g", "b"),
            ((166, 16, 169), (1, 0, 0), (18, 38, 64), (11, 14, 45), (11, 14, pd.NA)),
        )
    ],
)

# the same as:
# df.loc[((df['r'] == 166)&(df['g'] == 16)&(df['b'] == 169))|((df['r'] == 1)&(df['g'] == 0)&(df['b'] == 0))|((df['r'] == 18)&(df['g'] == 38)&(df['b'] == 64))|((df['r'] == 11)&(df['g'] == 14)&(df['b'] == 45))|((df['r'] == 11)&(df['g'] == 14)&(df['b'] == pd.NA))]

# NaN has to be passed as: pd.NA

df.d_multiloc(
    column_and_values=[("==", ("r", "g", "b"), ((11, 14, 45), (11, 14, pd.NA)))],
)
# the same as: df.loc[((df['r'] == 11)&(df['g'] == 14)&(df['b'] == 45))|((df['r'] == 11)&(df['g'] == 14)&(df['b'] == pd.NA))]

# not all values need to be inside each tuple
df.d_multiloc(
    column_and_values=[("==", ("r", "g", "b"), ((11, 14, 45), (11,), (16, 100)))],
)
# the same as: df.loc[((df['r'] == 11)&(df['g'] == 14)&(df['b'] == 45))|((df['r'] == 11))|((df['r'] == 16)&(df['g'] == 100))]


```
