## Image collection


Generating fake data


```python
from skimage.data import lfw_subset
from pathlib import Path
from skimage.io import imsave
from skimage.exposure import rescale_intensity
import numpy as np


data = lfw_subset()

p = Path("/tmp/skimage_data")

p.mkdir(exist_ok=True)

for idx, d in enumerate(data):
    imsave(p/f"im_{idx}.png", rescale_intensity(d, out_range=np.uint8).astype(np.uint8))
```

Image Collection creation


```python
from skimage.io import ImageCollection, imread
ic = ImageCollection(str(p/"*.png"), load_func=imread)
```


```python
from matplotlib.pyplot import imshow, show, axis
imshow(ic[0], cmap="gray")
axis("off")
show()

```
