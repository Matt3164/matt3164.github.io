# How to get unique array elements

Title is pretty self explanatory. A common operation consists of getting unqiue elements from an array.


```python
import numpy as np
np.unique(np.random.randint(0,255,size=(10,)))
```




    array([ 32,  72,  74,  83, 101, 167, 180, 199, 236, 254])



With counts for each values:


```python
np.unique(np.random.randint(0,255,size=(10,)), return_counts=True)
```




    (array([ 10,  42,  43,  77, 113, 124, 187, 195, 205, 214]),
     array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))



## Bonus : using pandas


```python
import pandas
df = pandas.DataFrame(np.random.randint(0,255,size=(10,)) , columns=["test"])
print(pandas.unique(df.test))
```

    [ 39 125 197 105 188 196 113 177 130 228]

