# skimage

## imread/imwrite


```python
from skimage.data import chelsea
from skimage.io import imread, imsave
from matplotlib.pyplot import imshow, axis, subplot
import matplotlib.pyplot as plt
%matplotlib inline

im = chelsea()

im_path = "/tmp/chelsea.jpg"

imsave(im_path, im)

loaded_im = imread(im_path)

imshow(loaded_im)
axis("off")
```




    (-0.5, 450.5, 299.5, -0.5)




![png](output_1_1.png)


## rescale_intensity


```python
from skimage.exposure import rescale_intensity
import numpy as np
im = chelsea()
subplot(1,2,1)
imshow(rescale_intensity(loaded_im, in_range="image", out_range=np.uint8))
axis("off")
subplot(1,2,2)
imshow(rescale_intensity(loaded_im, in_range=(0,128), out_range=np.uint8))
axis("off")
```




    (-0.5, 450.5, 299.5, -0.5)




![png](output_3_1.png)


## HOG

Histogram of oriented gradients

[Link](https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_hog.html)


```python
from skimage.feature import hog
from skimage.transform import resize
from skimage.color import rgb2gray

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




![png](output_5_1.png)


TODO: Visualisation for all cell size

## Daisy

An another type daisy shipped with the skimage library

[Link](https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_daisy.html)


```python
from skimage.feature import daisy

im = resize(rgb2gray(loaded_im), (256,256))

descs, descs_img = daisy(im, step=64, radius=58, rings=2, histograms=6,
                         orientations=8, visualize=True)


imshow(descs_img)
```




    <matplotlib.image.AxesImage at 0x7ff4946b4da0>




![png](output_8_1.png)


# Haar

Compute haar features as in the famous viola jones paper

[Link](https://scikit-image.org/docs/dev/auto_examples/applications/plot_haar_extraction_selection_classification.html#sphx-glr-auto-examples-applications-plot-haar-extraction-selection-classification-py)


```python
from skimage.feature import haar_like_feature_coord, haar_like_feature
from skimage.transform import integral_image

feature_types = ['type-2-x', 'type-2-y',
                 'type-3-x', 'type-3-y',
                 'type-4']

im = resize(rgb2gray(loaded_im), (32, 32))

img_ii = integral_image(im)

# Extract all possible features
feature_coord, feature_type = haar_like_feature_coord(width=im.shape[0], height=im.shape[1],
                            feature_type=feature_types)

print(f"Number of haar feature : {feature_coord.shape[0]}")

# Limiting feature for convenience reasons
# This example should run fast :smile:
feature_coord = feature_coord[:256]
feature_type = feature_type[:256]

feats = haar_like_feature(img_ii, 0, 0, img_ii.shape[0], img_ii.shape[1], feature_type=feature_type, feature_coord=feature_coord)

print(f"Extracted features: {feats.shape}")
```

    Number of haar feature : 509270
    Extracted features: (256,)


## LBP

[Link](https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_local_binary_pattern.html)


```python
from skimage.feature import local_binary_pattern

# settings for LBP
radius = 3
n_points = 8 * radius

image = resize(rgb2gray(loaded_im), (32, 32))
lbp = local_binary_pattern(image, n_points, radius, "uniform")

subplot(1,2,1)
imshow(image, cmap=plt.cm.gray)
axis("off")
subplot(1,2,2)
imshow(lbp, cmap=plt.cm.gray)
axis("off")
```




    (-0.5, 31.5, 31.5, -0.5)




![png](output_12_1.png)


## Haralick features

## Convolutions (Random kernels)


```python
import cv2
from skimage.morphology import disk
gray = resize(rgb2gray(loaded_im), (256, 256))

kernel = disk(10)

out = cv2.filter2D(gray, -1, kernel)

subplot(1,2,1)
imshow(gray, cmap=plt.cm.gray)
axis("off")
subplot(1,2,2)
imshow(out, cmap=plt.cm.gray)
axis("off")
```




    (-0.5, 255.5, 255.5, -0.5)




![png](output_15_1.png)



```python
import numpy as np

kernel = 0.2* np.random.randn(10,10)

out = cv2.filter2D(gray, -1, kernel)

subplot(1,2,1)
imshow(gray, cmap=plt.cm.gray)
axis("off")
subplot(1,2,2)
imshow(out, cmap=plt.cm.gray)
axis("off")
```




    (-0.5, 255.5, 255.5, -0.5)




![png](output_16_1.png)


## Convolutions (Gabor kernels)


```python
import numpy as np
from skimage.filters import gabor_kernel


theta = np.random.choice(
    np.arange(0, 4)/ 4. * np.pi
)

sigma = np.random.choice(
    np.arange(0,4)
) 

freq = np.random.choice(
    np.arange(0.05,0.25, 0.05)
) 
    
        
kernel = np.real(gabor_kernel(freq, theta=theta,
                              sigma_x=sigma, sigma_y=sigma))

out = cv2.filter2D(gray, -1, kernel)

subplot(1,2,1)
imshow(gray, cmap=plt.cm.gray)
axis("off")
subplot(1,2,2)
imshow(out, cmap=plt.cm.gray)
axis("off")
```




    (-0.5, 255.5, 255.5, -0.5)




![png](output_18_1.png)


## Image collection


## Patches

Especially, in remote sensing, a common operation consists of splitting an image into smaller parts


```python
from skimage.util import view_as_windows

out = view_as_windows(chelsea(), window_shape=(32,32,3), step=(16,16,3))

print(f"Out shape : {out.shape}")
print("Out shape : (windows_on_i, windows_on_j, 1, window_width, window_height, 3)")
```

    Out shape : (17, 27, 1, 32, 32, 3)
    Out shape : (windows_on_i, windows_on_j, 1, window_width, window_height, 3)


## shapes: data generation


```python
from skimage.draw import random_shapes

# Let's start simple and generate a 128x128 image
# with a single grayscale rectangle.
result,_ = random_shapes((128, 128), max_shapes=1, shape='rectangle',
                       multichannel=True)

imshow(result)
```




    <matplotlib.image.AxesImage at 0x7ff4698f9240>




![png](output_23_1.png)

