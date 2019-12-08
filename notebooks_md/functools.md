# Functools

## partial


is used to freeze some arguments of a function. Useful for functionnal programming


```python
from functools import partial

def add(i1: int, i2: int)->int:
    return i1+i2

add2 = partial(add, i2=2)

print(add2(2))
```

    4

