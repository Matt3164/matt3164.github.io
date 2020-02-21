# How to create synchronized iterators

[Reference doc](https://docs.python.org/fr/3/library/itertools.html)

How to create 2 iterators with synchronised values


```python
from itertools import tee

init_iter = range(10)

# Create 2 synchronized iterators
sync1, sync2 = tee(init_iter)
# Apply one function to one iterator and print to see synchronization
for val, valplusone in zip(sync1, map(lambda x: x+1, sync2)):
    print(f"Values: 1st iter {val}, 2nd iter {valplusone}")

```

    Values: 1st iter 0, 2nd iter 1
    Values: 1st iter 1, 2nd iter 2
    Values: 1st iter 2, 2nd iter 3
    Values: 1st iter 3, 2nd iter 4
    Values: 1st iter 4, 2nd iter 5
    Values: 1st iter 5, 2nd iter 6
    Values: 1st iter 6, 2nd iter 7
    Values: 1st iter 7, 2nd iter 8
    Values: 1st iter 8, 2nd iter 9
    Values: 1st iter 9, 2nd iter 10

