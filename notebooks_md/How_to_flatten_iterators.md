# How to flatten iterators

How to create a longer iterator from a list of iterators or an iterator of iterators.


```python
from itertools import chain

new_iter = chain.from_iterable([range(10), range(10)])

for elmt in new_iter:
    print(f"Value : {elmt}")
    
```

    Value : 0
    Value : 1
    Value : 2
    Value : 3
    Value : 4
    Value : 5
    Value : 6
    Value : 7
    Value : 8
    Value : 9
    Value : 0
    Value : 1
    Value : 2
    Value : 3
    Value : 4
    Value : 5
    Value : 6
    Value : 7
    Value : 8
    Value : 9

