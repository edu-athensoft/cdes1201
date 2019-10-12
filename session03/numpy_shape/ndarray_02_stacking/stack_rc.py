# np.r_
# np.c_

import numpy as np

# row stack
c = np.r_[1:4,0,4]
print(c)
print()

c = np.r_[np.array([1,2,3]), np.array([4,5,6])]
print(c)
print()

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.vstack((a,b))
print(c)
print()


# column stack
# 1d array should be taken as a column vector
c = np.c_[np.array([1,2,3]), np.array([4,5,6])]
print(c)
print()

c = np.c_[np.array([[1,2,3]]), np.array([[4,5,6]])]
print(c)
print()

c = np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]
print(c)
print()
