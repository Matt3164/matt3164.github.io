# How to freeze function arguments using partial


`partial` is used to freeze some arguments of a function. It is extremely useful for functionnal programming


```python
from functools import partial

def add(i1: int, i2: int)->int:
    return i1+i2

add2 = partial(add, i2=2)

print(add2(2))
```

    4


Here, the initial `add` function takes 2 inputs. Using `partial`, you can generate a new function called `add2` which is the `add` function where the `i2` argument is freezed (equals to a constants here 2). In fact, the syntax equivalent would be the following:


```python
def add2(i1: int)->int:
    return add(i1, i2=2)
```
