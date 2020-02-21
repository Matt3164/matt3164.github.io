# How to compute Haar features

Compute haar features as in the famous viola jones paper

[Link](https://scikit-image.org/docs/dev/auto_examples/applications/plot_haar_extraction_selection_classification.html#sphx-glr-auto-examples-applications-plot-haar-extraction-selection-classification-py)


```python
from skimage.feature import haar_like_feature_coord, haar_like_feature
from skimage.transform import integral_image, resize
from skimage.color import rgb2gray
from skimage.data import chelsea

feature_types = ['type-2-x', 'type-2-y',
                 'type-3-x', 'type-3-y',
                 'type-4']

im = resize(rgb2gray(chelsea()), (32, 32))

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

