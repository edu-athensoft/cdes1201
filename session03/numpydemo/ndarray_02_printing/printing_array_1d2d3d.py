# printing arrays

import numpy as np

# 1d array
a = np.arange(6)
print(a)
print()


# 1d array
a = np.arange(12).reshape(4,3)
print(a)
print()


# 2d array
a = np.arange(24).reshape(4,3,2)
print(a)
print()

# the last axis or dimension is 2
# the second-to-last axis or dimension is 3
# the rest axis or dimension is 4
