# How to use pipe


```python
from toolz import pipe

print( pipe( 3,
    lambda x: x+1,
    lambda x: x-2,
    lambda _: 4,
    float
)) # -> 4.0
```

    4.0



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

    [4, 8, 12, 16]

