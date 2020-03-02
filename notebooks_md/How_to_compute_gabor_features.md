## Convolutions (Gabor kernels)


```python
import numpy as np
from skimage.filters import gabor_kernel
import cv2
from skimage.color import rgb2gray
from skimage.data import chelsea

from matplotlib.pyplot import imshow, show, subplot, axis
import matplotlib.pyplot as plt

gray = rgb2gray(chelsea())


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

    /home/mlegoff/anaconda3/envs/juicy/lib/python3.7/site-packages/skimage/filters/_gabor.py:90: RuntimeWarning: divide by zero encountered in true_divide
      g[:] = np.exp(-0.5 * (rotx ** 2 / sigma_x ** 2 + roty ** 2 / sigma_y ** 2))
    /home/mlegoff/anaconda3/envs/juicy/lib/python3.7/site-packages/skimage/filters/_gabor.py:90: RuntimeWarning: invalid value encountered in true_divide
      g[:] = np.exp(-0.5 * (rotx ** 2 / sigma_x ** 2 + roty ** 2 / sigma_y ** 2))
    /home/mlegoff/anaconda3/envs/juicy/lib/python3.7/site-packages/skimage/filters/_gabor.py:91: RuntimeWarning: invalid value encountered in true_divide
      g /= 2 * np.pi * sigma_x * sigma_y





    (-0.5, 450.5, 299.5, -0.5)


