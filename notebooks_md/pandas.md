# pandas

## Creating a DataFrame


```python
import numpy as np
import pandas

# From numpy arrays
col1 = np.random.rand(100)
col2 = np.random.rand(100)

print( pandas.DataFrame.from_dict({"col1":col1,"col2":col2}).head() ) 

# From dict iterator

print(pandas.DataFrame.from_records(np.hstack([col1.reshape(-1,1), col2.reshape(-1,1)]), columns=["col1", "col2"]).head())

# From list of row dict

row_dict = list( map(lambda x: {"col1": x[0], "col2": x[1]} , zip(col1, col2)) )

print(pandas.DataFrame.from_records(row_dict).head())

```

           col1      col2
    0  0.114465  0.259129
    1  0.368231  0.132901
    2  0.893511  0.205036
    3  0.636088  0.856989
    4  0.497390  0.834272
           col1      col2
    0  0.114465  0.259129
    1  0.368231  0.132901
    2  0.893511  0.205036
    3  0.636088  0.856989
    4  0.497390  0.834272
           col1      col2
    0  0.114465  0.259129
    1  0.368231  0.132901
    2  0.893511  0.205036
    3  0.636088  0.856989
    4  0.497390  0.834272


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


```python
import numpy as np
import pandas
col1 = np.random.rand(100)
col2 = np.random.rand(100)

df = pandas.DataFrame.from_dict({"col1":col1,"col2":col2})

df.to_csv("/tmp/data.csv")

loaded_df = pandas.read_csv("/tmp/data.csv", index_col=0)

```

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
