# important attributes of an ndarray object

import numpy as np


# create an array

a = np.array([1,2,3,4])  # RIGHT
# a = np.array(1,2,3,4)    # WRONG
print(a,"\n",type(a), a.dtype)


a = np.array([1.4,2.5,3.6,4.7])  # RIGHT
# a = np.array(1,2,3,4)    # WRONG
print(a,"\n",type(a), a.dtype)



a = np.array([(1,2,3,4),(5,6,7,8)])  # RIGHT
print(a,"\n",type(a), a.dtype)


a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)

