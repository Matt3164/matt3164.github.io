# How to load/unload from a CSV


```python
import numpy as np
import pandas
col1 = np.random.rand(100)
col2 = np.random.rand(100)

df = pandas.DataFrame.from_dict({"col1":col1,"col2":col2})

df.to_csv("/tmp/data.csv")

loaded_df = pandas.read_csv("/tmp/data.csv", index_col=0)

```
