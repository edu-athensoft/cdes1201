# stacking
#

import numpy as np
from numpy import newaxis


a = np.floor(10*np.random.random((2,2)))
print("a\n",a)
print()

b = np.floor(10*np.random.random((2,2)))
print("b\n",b)
print()

# It is equivalent to hstack only for 2D arrays
b = np.column_stack((a,b))     # with 2D arrays
print("column_stack\n",b)
print()


a = np.array([4.,2.])
b = np.array([3.,8.])
c = np.column_stack((a,b))     # returns a 2D array
print("column_stack\n",c)
print()


