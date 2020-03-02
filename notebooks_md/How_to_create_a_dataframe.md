# How to create a dataframe


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
    0  0.779976  0.115767
    1  0.156384  0.438307
    2  0.795218  0.256210
    3  0.689936  0.790331
    4  0.763893  0.390188
           col1      col2
    0  0.779976  0.115767
    1  0.156384  0.438307
    2  0.795218  0.256210
    3  0.689936  0.790331
    4  0.763893  0.390188
           col1      col2
    0  0.779976  0.115767
    1  0.156384  0.438307
    2  0.795218  0.256210
    3  0.689936  0.790331
    4  0.763893  0.390188

