# important attributes of an ndarray object

import numpy as np


# create an array from Python list
# 1-d array
a = np.array([1,2,3,4])             # RIGHT
# a = np.array(1,2,3,4)             # WRONG
print(a,"\n",type(a), "the datatype is ", a.dtype)
print()

# 1-d array
a = np.array([1.4,2.5,3.6,4.7])     # RIGHT
# a = np.array(1,2,3,4)             # WRONG
print(a,"\n",type(a), "the datatype is ", a.dtype)
print()

# create an array from Python tuple
# 1-d array
a = np.array((1,2,3,4))             # RIGHT
print(a,"\n",type(a), "the datatype is ", a.dtype)
print()

# create an array
# 2-d array
a = np.array([(1,2,3,4),(5,6,7,8)]) # RIGHT
print(a,"\n",type(a), "the datatype is ", a.dtype)
print()


