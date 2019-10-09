# printing large arrays

import numpy as np
import sys

# 1d array
# without any config
a = np.arange(2000)
print(a)
print()


# 2d array
# without any config
a = np.arange(10000).reshape(100,100)
print(a)
print()


# To force NumPy to print the entire array
np.set_printoptions(threshold=sys.maxsize)
a = np.arange(2000)
print(a)
print()