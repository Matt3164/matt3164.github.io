## Patches

Especially, in remote sensing, a common operation consists of splitting an image into smaller parts


```python
from skimage.util import view_as_windows
from skimage.data import chelsea
out = view_as_windows(chelsea(), window_shape=(32,32,3), step=(16,16,3))

print(f"Out shape : {out.shape}")
print("Out shape : (windows_on_i, windows_on_j, 1, window_width, window_height, 3)")
```

    Out shape : (17, 27, 1, 32, 32, 3)
    Out shape : (windows_on_i, windows_on_j, 1, window_width, window_height, 3)

