# How to compute local binary patterns features

[Link](https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_local_binary_pattern.html)


```python
from skimage.feature import local_binary_pattern
from skimage.data import chelsea
from skimage.transform import resize
from skimage.color import rgb2gray
from matplotlib.pyplot import imshow, axis, subplot
import matplotlib.pyplot as plt
%matplotlib inline

# settings for LBP
radius = 3
n_points = 8 * radius

image = resize(rgb2gray(chelsea()), (32, 32))
lbp = local_binary_pattern(image, n_points, radius, "uniform")

subplot(1,2,1)
imshow(image, cmap=plt.cm.gray)
axis("off")
subplot(1,2,2)
imshow(lbp, cmap=plt.cm.gray)
axis("off")
```




    (-0.5, 31.5, 31.5, -0.5)




![png](output_1_1.png)

