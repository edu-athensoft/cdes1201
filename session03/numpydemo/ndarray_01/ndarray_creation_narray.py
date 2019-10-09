# frequent error when creation

import numpy as np


# transform from sequence of sequence
# 2-d array
a = np.array([(1.5, 2, 3), (4, 5, 6)])
print(a,"\n",type(a), "and the dimension is ",a.ndim)
print()


# transform from sequence of sequence of sequence
# 3-d array
a = np.array([((3,5), (3,5), (3,5)), ((3,5), (3,5), (3,5))])
print(a,"\n",type(a), "and the dimension is ", a.ndim)
print()
