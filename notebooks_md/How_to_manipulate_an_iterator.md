# How to manipulate an iterator

Example on how to use `islice` to modify start index, stop index and even step.


```python
from itertools import islice
# New iterator starting at 2 ending at 50 jumping 2 to 2
new_iter = islice(range(100),2, 50, 2)
```
