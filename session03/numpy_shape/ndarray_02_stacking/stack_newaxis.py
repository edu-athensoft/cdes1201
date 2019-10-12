# stacking
# newaxis

import numpy as np
from numpy import newaxis


a = np.array([4.,2.])
b = np.array([3.,8.])
c = np.column_stack((a,b))     # returns a 2D array
print("column_stack\n",c)
print()



# newaxis
# to increase a dimension
c = a[:,newaxis]               # this allows to have a 2D columns vector
print(c)
print()


c = np.column_stack((a[:,newaxis],b[:,newaxis]))
print(c)
print()


c = np.hstack((a[:,newaxis],b[:,newaxis]))   # the result is the same
print(c)
print()