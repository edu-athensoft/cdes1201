# Shape Manipulation
# vstack and hstack

import numpy as np

a = np.floor(10*np.random.random((2,2)))
print(a)
print()

b = np.floor(10*np.random.random((2,2)))
print(b)
print()

c = np.vstack((a,b))
print(c)
print()

c = np.hstack((a,b))
print(c)
print()