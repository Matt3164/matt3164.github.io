# How to read and write images using opencv


```python
import cv2
from skimage.data import chelsea
from matplotlib.pyplot import imshow, axis
%matplotlib inline

im = chelsea()

im_path = "/tmp/chelsea.jpg"

cv2.imwrite(im_path, im)

loaded_im = cv2.imread(im_path)

imshow(loaded_im)
axis("off")
```




    (-0.5, 450.5, 299.5, -0.5)




![png](output_1_1.png)

