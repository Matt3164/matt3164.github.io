# How to interpolate using scipy


```python
import numpy as np
from scipy import interpolate
from matplotlib.pyplot import plot
%matplotlib inline
```


```python
x = np.linspace(0, 4, 12)

y = np.cos(x**2/3+4)

f1 = interpolate.interp1d(x, y,kind = 'linear')
f2 = interpolate.interp1d(x, y, kind = 'cubic')

xnew = np.linspace(0, 4,30)

new_values1 = f1(xnew)
```


```python
import matplotlib.pyplot as plt
%matplotlib inline

plt.plot(x, y, "o")
plt.plot(xnew, new_values1, "+--")
```




    [<matplotlib.lines.Line2D at 0x7f9b784055f8>]




![png](output_3_1.png)

