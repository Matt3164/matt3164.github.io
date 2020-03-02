## shapes: data generation


```python
from skimage.draw import random_shapes
from matplotlib.pyplot import imshow, show, axis

# Let's start simple and generate a 128x128 image
# with a single grayscale rectangle.
result,_ = random_shapes((128, 128), max_shapes=1, shape='rectangle',
                       multichannel=True)

imshow(result)
axis("off")
show()
```
