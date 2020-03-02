## rescale_intensity


```python
from skimage.exposure import rescale_intensity
import numpy as np
from skimage.data import chelsea
from matplotlib.pyplot import subplot, imshow, axis
loaded_im = chelsea()
subplot(1,2,1)
imshow(rescale_intensity(loaded_im, in_range="image", out_range=np.uint8))
axis("off")
subplot(1,2,2)
imshow(rescale_intensity(loaded_im, in_range=(0,128), out_range=np.uint8))
axis("off")
```




    (-0.5, 450.5, 299.5, -0.5)


