# Snippets

# Python

## Type hints

### Raw
````python
def add_th(i1: int, i2: int)->int:
    ...
````

### Generic

## itertools

[Reference doc](https://docs.python.org/fr/3/library/itertools.html)

### tee

Create a copy of an iterator.

````python
from itertools import tee

init_iter = range(100)

# Create 2 synchronized iterators
sync1, sync2 = tee(init_iter)
# Apply one function to one iterator and print to see synchronization
for val, valplusone in zip(sync1, map(lambda x: x+1, sync2)):
    print(val, valplusone)

````

### islice

Modify an iterator : start index, stop index or event step

```python
from itertools import islice
# New iterator starting at 2 ending at 50 jumping 2 to 2
new_iter = islice(range(100),2, 50, 2)
```

### chain.from_iterable

flat_map function : return an iterator from a list of iterators...

```python
from itertools import chain

new_iter = chain.from_iterable([range(10), range(10)])

```

## functools

### partial

```python
from functools import partial

def add(i1: int, i2: int)->int:
    return i1+i2

add2 = partial(add, i2=2)

print(add2(2))

```

# Numpy

## unique

Compute unique elements from an array. 

```python

import numpy as np

random_ints = np.random.randint(0,255, size=(100,))
# Print unique elements
print(np.unique(random_ints))
# Print unique elements and counts
print(np.unique(random_ints, return_counts=True))

```

# Scipy

## interpolate

Create a new function from X and Y arrays.

```python
import numpy as np
from scipy import interpolate
x = np.linspace(0, 4, 12)
y = np.cos(x**2/3+4)

f1 = interpolate.interp1d(x, y,kind = 'linear')
f2 = interpolate.interp1d(x, y, kind = 'cubic')

xnew = np.linspace(0, 4,30)

new_values1 = f1(xnew)

```

# pandas

## Creating a DataFrame

```python

import numpy as np
import pandas

# From numpy arrays
col1 = np.random.rand(100)
col2 = np.random.rand(100)

print( pandas.DataFrame.from_dict({"col1":col1,"col2":col2}) ) 

# From dict iterator

print(pandas.DataFrame.from_records(np.hstack([col1.reshape(-1,1), col2.reshape(-1,1)]), columns=["col1", "col2"]))

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

## Indexing

# sklearn

## Pipeline

## Feature aggregation

## Column Transformer

# tensorflow

## TF records

# pytorch

## Simple CNN

## Sequential

# toolz

## compose

## pipe

# hyperopt

# mlflow

# joblib
