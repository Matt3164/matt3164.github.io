## Convolutions (Random kernels)


```python
import cv2
from skimage.morphology import disk
from skimage.transform import resize
from skimage.color import rgb2gray
from skimage.data import chelsea
from matplotlib.pyplot import imshow, show, subplot, axis
import matplotlib.pyplot as plt

gray = resize(rgb2gray(chelsea()), (256, 256))

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

    /home/mlegoff/anaconda3/envs/juicy/lib/python3.7/site-packages/ipykernel_launcher.py:7: MatplotlibDeprecationWarning: Adding an axes using the same arguments as a previous axes currently reuses the earlier instance.  In a future version, a new instance will always be created and returned.  Meanwhile, this warning can be suppressed, and the future behavior ensured, by passing a unique label to each axes instance.
      import sys
    /home/mlegoff/anaconda3/envs/juicy/lib/python3.7/site-packages/ipykernel_launcher.py:10: MatplotlibDeprecationWarning: Adding an axes using the same arguments as a previous axes currently reuses the earlier instance.  In a future version, a new instance will always be created and returned.  Meanwhile, this warning can be suppressed, and the future behavior ensured, by passing a unique label to each axes instance.
      # Remove the CWD from sys.path while we load stuff.





    (-0.5, 255.5, 255.5, -0.5)


