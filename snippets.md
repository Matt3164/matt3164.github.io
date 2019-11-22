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

Useful API to chain operations on dataset.

```python

from sklearn.datasets import make_classification
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression

data = make_classification(1000)

pipe = make_pipeline(
    StandardScaler(),
    PCA(),
    LogisticRegression()
)

pipe.fit(*data)

```

## Feature aggregation



```python

from sklearn.datasets import make_classification
from sklearn.pipeline import make_pipeline, make_union
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.neural_network import MLPClassifier

data = make_classification(1000)

pipe = make_pipeline(
    StandardScaler(),
    make_union( 
                PCA(n_components=2),
                TruncatedSVD(n_components=2),
                KBinsDiscretizer()
                ),
    MLPClassifier()
)

pipe.fit(*data)

```

## Column Transformer

```python

from sklearn.datasets import make_classification
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier

data = make_classification(1000)

pipe = make_pipeline(
    ColumnTransformer(
        [
            ("scaled", StandardScaler(), slice(0, 10)),
            ("disc", KBinsDiscretizer(n_bins=10), slice(10,12)),
            ("rest", "passthrough", slice(12,20))
    ]), 
    PCA(n_components=2),
    MLPClassifier()
)

pipe.fit(*data)

```

# tensorflow

## TF records

# pytorch

## Simple CNN

## Sequential

# toolz

Amazing library to do functionnal programming in Python.

## compose
```python
from toolz import compose

def func1(i: int)->int:     
    return i+2

def func2(i: int)->int:
    return i - 1

func3 = compose(func2, func1)

print(func3(3)) # ->4

```

## pipe

Apply successive functions on value

```python
from toolz import pipe

print( pipe( 3,
    lambda x: x+1,
    lambda x: x-2,
    lambda _: 4,
    float
)) # -> 4.0
    

```

## Magic combo

```python

from toolz import pipe, compose
from toolz.curried import map, filter


print(pipe( range(100),
    filter(lambda x : x%2),
    map(compose(lambda x : 2*x, lambda x: x+1)),
    filter(lambda x : x<20),
    list
)) # -> 4,8,12,16


```

# hyperopt

[Source](https://docs.azuredatabricks.net/_static/notebooks/hyperopt-sklearn-model-selection.html)

```python

from sklearn.datasets import make_classification
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from hyperopt import tpe, hp, fmin

x, y = make_classification(1000)

def objective(params):
    global x, y
    pipe = make_pipeline(
        ColumnTransformer(
            [
                ("scaled", StandardScaler(), slice(0, 10)),
                ("disc", KBinsDiscretizer(n_bins=10), slice(10,12)),
                ("rest", "passthrough", slice(12,20))
        ]), 
        PCA(n_components=2),
        params["model"](**params["kwargs"])
    )
    
    pipe.fit(x, y)

    accuracy =accuracy_score(pipe.predict(x), y)
    
    return {'loss': -accuracy}

search_space = hp.choice("classifier",[
        {'model': KNeighborsClassifier,
        'kwargs': {'n_neighbors': hp.choice('n_neighbors',range(3,11))}
        },
        {'model': MLPCLassifier,
        'kwargs': {'hidden_layer_sizes':hp.choice('layers',[(10,10), (100,100), (256,256)])}
        ])


best_result = fmin(
    fn=objective, 
    space=search_space,
    algo=tpe.suggest,
    max_evals=16,
    )

```

# mlflow

[Source](https://www.mlflow.org/docs/latest/tutorial.html)

```python
import mlflow

with mlflow.start_run():
        
        # ... Fit model   

        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)

        mlflow.sklearn.log_model(lr, "model")

```

# joblib
