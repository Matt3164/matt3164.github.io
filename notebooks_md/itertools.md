# itertools

[Reference doc](https://docs.python.org/fr/3/library/itertools.html)


## tee
Create a copy of an iterator.

from itertools import tee

init_iter = range(10)

# Create 2 synchronized iterators
sync1, sync2 = tee(init_iter)
# Apply one function to one iterator and print to see synchronization
for val, valplusone in zip(sync1, map(lambda x: x+1, sync2)):
    print(val, valplusone)



```python
from itertools import islice
# New iterator starting at 2 ending at 50 jumping 2 to 2
new_iter = islice(range(100),2, 50, 2)
```

# chain.from_iterable


```python
from itertools import chain

new_iter = chain.from_iterable([range(10), range(10)])
```
