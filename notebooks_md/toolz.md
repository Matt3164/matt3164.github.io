# Toolz

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

    4


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

    4.0


Full example


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

    4.0


Full example


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

