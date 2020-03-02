# How to compute daisy features

[Link](https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_daisy.html)


```python
from skimage.feature import daisy
from skimage.transform import resize
from skimage.color import rgb2gray
from skimage.data import chelsea
from matplotlib.pyplot import imshow
%matplotlib inline

im = resize(rgb2gray(chelsea()), (256,256))

descs, descs_img = daisy(im, step=64, radius=58, rings=2, histograms=6,
                         orientations=8, visualize=True)


imshow(descs_img)
```




    <matplotlib.image.AxesImage at 0x7fe8ac1d1d68>




![png](output_1_1.png)

