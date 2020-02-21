# How to get unique array elements


```python
import numpy as np
np.unique(np.random.randint(0,255,size=(10,)))
```




    array([ 24,  27,  52,  64,  72,  74, 115, 152, 187, 199])



With counts for each values:


```python
np.unique(np.random.randint(0,255,size=(10,)), return_counts=True)
```




    (array([ 61,  67,  96, 116, 120, 121, 152, 193, 203, 236]),
     array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))



## Bonus : using pandas


```python
import pandas
df = pandas.DataFrame(np.random.randint(0,255,size=(10,)) , columns=["test"])
print(pandas.unique(df.test))
```

    [157   5 148 121  75 152  47 235  36 176]

