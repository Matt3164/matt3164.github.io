# How to compute HOG features

[Doc](https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_hog.html)


```python
from skimage.feature import hog
from skimage.transform import resize
from skimage.color import rgb2gray
from skimage.data import chelsea
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot, imshow , axis
from skimage.exposure import rescale_intensity

im = chelsea()

im = resize(rgb2gray(im), (64,64))

fd, hog_image = hog(im, orientations=8, pixels_per_cell=(8, 8),
                    cells_per_block=(1, 1), visualize=True, multichannel=False)

subplot(1,2,1)
imshow(im, cmap=plt.cm.gray)
axis("off")

# Rescale histogram for better display
hog_image_rescaled = rescale_intensity(hog_image, in_range=(0, 10))
subplot(1,2,2)
imshow(hog_image_rescaled, cmap=plt.cm.gray)
axis("off")


```




    (-0.5, 63.5, 63.5, -0.5)


