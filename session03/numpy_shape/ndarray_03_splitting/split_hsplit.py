# splitting
# horizontal splitting

import numpy as np

a = np.floor(10*np.random.random((2,12)))
print(a)

b = np.hsplit(a,3)   # Split a into 3
print(b)
print()
print(b[0])
print()
print(b[1])
print()
print(b[2])
print()

b = np.hsplit(a,(3,4))   # Split a after the third and the fourth column
print(b)
