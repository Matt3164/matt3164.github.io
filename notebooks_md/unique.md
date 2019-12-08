Useful to compute uniaue elements in an array.

For instance, useful in case you want to known the composition in terms of labels of a dataset.


```python
import numpy as np

random_ints = np.random.randint(0,16, size=(100,))
# Print unique elements
print(f"Unique elements in the list : {np.unique(random_ints)}")
# Print unique elements and counts
print(f"Unique elements in the list with counts : {np.unique(random_ints, return_counts=True)}")
print()

```

    Unique elements in the list : [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
    Unique elements in the list with counts : (array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15]), array([6, 7, 5, 9, 7, 9, 3, 6, 5, 3, 5, 8, 6, 7, 6, 8]))
    

