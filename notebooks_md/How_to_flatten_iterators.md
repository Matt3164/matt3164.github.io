# How to flatten iterators

Whoever often use iterators may encounter the problem of creating a longer iterator from a list of iterators or an iterator of iterators.

The function `chain.from_iterable` from the `itertools` library is here to save the day and allow the creation of a single iterator from an iterator of iterators


```python
from itertools import chain

new_iter = chain.from_iterable([range(10), range(10)])

for elmt in new_iter:
    print(elmt)
    
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

