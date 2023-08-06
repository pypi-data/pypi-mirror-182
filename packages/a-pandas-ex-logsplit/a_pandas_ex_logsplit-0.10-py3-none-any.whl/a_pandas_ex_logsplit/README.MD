# Splits a DataFrame/Series logarithmically 

```python
pip install a-pandas-ex-logsplit
```

```python
from a_pandas_ex_logsplit import pd_add_logsplit
pd_add_logsplit()
import pandas as pd
df = pd.read_csv("https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv")
df = df[:50]
for h in df.ds_logsplit(columns=["Cabin", "Fare"], includeindex=False):
    print(h)
for h in df.ds_logsplit(columns="Cabin", includeindex=True):
    print(h)
for h in df.ds_logsplit(columns="Cabin", includeindex=False):
    print(h)
for h in df.Cabin.ds_logsplit(includeindex=True):
    print(h)
	
	
[(nan, 7.25)]
[('C85', 71.2833), (nan, 7.925)]
[('C123', 53.1), (nan, 8.05), (nan, 8.4583)]
[('E46', 51.8625), (nan, 21.075), (nan, 11.1333), (nan, 30.0708)]
[('G6', 16.7), ('C103', 26.55), (nan, 8.05), (nan, 31.275), (nan, 7.8542)]
[(nan, 16.0), (nan, 29.125), (nan, 13.0), (nan, 18.0), (nan, 7.225), (nan, 26.0)]
[('D56', 13.0), (nan, 8.0292), ('A6', 35.5), (nan, 21.075), (nan, 31.3875), (nan, 7.225), ('C23 C25 C27', 263.0)]
[(nan, 7.8792), (nan, 7.8958), (nan, 27.7208), ('B78', 146.5208), (nan, 7.75), (nan, 10.5), (nan, 82.1708), (nan, 52.0)]
[(nan, 7.2292), (nan, 8.05), (nan, 18.0), (nan, 11.2417), (nan, 9.475), (nan, 21.0), (nan, 7.8958), (nan, 41.5792), (nan, 7.8792)]
[(nan, 8.05), (nan, 15.5), (nan, 7.75), (nan, 21.6792), (nan, 17.8)]


[(0, 1)]
[(1, 2), (2, 3)]
[(3, 4), (4, 5), (5, 6)]
[(6, 7), (7, 8), (8, 9), (9, 10)]
[(10, 11), (11, 12), (12, 13), (13, 14), (14, 15)]
[(15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21)]
[(21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 27), (27, 28)]
[(28, 29), (29, 30), (30, 31), (31, 32), (32, 33), (33, 34), (34, 35), (35, 36)]
[(36, 37), (37, 38), (38, 39), (39, 40), (40, 41), (41, 42), (42, 43), (43, 44), (44, 45)]
[(45, 46), (46, 47), (47, 48), (48, 49), (49, 50)]


[nan]
['C85', nan]
['C123', nan, nan]
['E46', nan, nan, nan]
['G6', 'C103', nan, nan, nan]
[nan, nan, nan, nan, nan, nan]
['D56', nan, 'A6', nan, nan, nan, 'C23 C25 C27']
[nan, nan, nan, 'B78', nan, nan, nan, nan]
[nan, nan, nan, nan, nan, nan, nan, nan, nan]
[nan, nan, nan, nan, nan]


[(0, nan)]
[(1, 'C85'), (2, nan)]
[(3, 'C123'), (4, nan), (5, nan)]
[(6, 'E46'), (7, nan), (8, nan), (9, nan)]
[(10, 'G6'), (11, 'C103'), (12, nan), (13, nan), (14, nan)]
[(15, nan), (16, nan), (17, nan), (18, nan), (19, nan), (20, nan)]
[(21, 'D56'), (22, nan), (23, 'A6'), (24, nan), (25, nan), (26, nan), (27, 'C23 C25 C27')]
[(28, nan), (29, nan), (30, nan), (31, 'B78'), (32, nan), (33, nan), (34, nan), (35, nan)]
[(36, nan), (37, nan), (38, nan), (39, nan), (40, nan), (41, nan), (42, nan), (43, nan), (44, nan)]
[(45, nan), (46, nan), (47, nan), (48, nan), (49, nan)]

```
