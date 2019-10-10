# creating array with dtype

import numpy as np


# creating array without dtype
# 2-d array
a = np.array([(1.5, 2, 3), (4, 5, 6)])
print(a,"\n",type(a))
print()

# creating array with dtype
# 2-d array
a = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=int)
print(a,"\n",type(a), "and the data type is ",a.dtype)
print()

a = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=np.int16)
print(a,"\n",type(a), "and the data type is ",a.dtype)
print()

a = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=np.int8)
print(a,"\n",type(a), "and the data type is ",a.dtype)
print()

# creating array with dtype
# 2-d array
a = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)
print(a,"\n",type(a), "and the data type is ",a.dtype)
print()

a = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=np.float32)
print(a,"\n",type(a), "and the data type is ",a.dtype)
print()

# creating array with dtype
# 2-d array
a = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=complex)
print(a,"\n",type(a), "and the data type is ",a.dtype)
print()