# pandas

## Creating a DataFrame


```python
import numpy as np
import pandas

col1 = np.random.rand(100)
col2 = np.random.rand(100)

# From dict of numpy arrays

print( pandas.DataFrame.from_dict({"col1":col1,"col2":col2}).head() ) 

# From numpy array and list of column names

print(pandas.DataFrame.from_records(np.hstack([col1.reshape(-1,1), col2.reshape(-1,1)]), columns=["col1", "col2"]).head())

# From list of row dict

row_dict = list( map(lambda x: {"col1": x[0], "col2": x[1]} , zip(col1, col2)) )

print(pandas.DataFrame.from_records(row_dict).head())

```

           col1      col2
    0  0.739740  0.795301
    1  0.777264  0.957833
    2  0.705391  0.144569
    3  0.074463  0.299167
    4  0.977063  0.170670
           col1      col2
    0  0.739740  0.795301
    1  0.777264  0.957833
    2  0.705391  0.144569
    3  0.074463  0.299167
    4  0.977063  0.170670
           col1      col2
    0  0.739740  0.795301
    1  0.777264  0.957833
    2  0.705391  0.144569
    3  0.074463  0.299167
    4  0.977063  0.170670


## Loading/Unloading from CSV


```python
import numpy as np
import pandas
col1 = np.random.rand(100)
col2 = np.random.rand(100)

df = pandas.DataFrame.from_dict({"col1":col1,"col2":col2})

df.to_csv("/tmp/data.csv")

loaded_df = pandas.read_csv("/tmp/data.csv", index_col=0)

```
