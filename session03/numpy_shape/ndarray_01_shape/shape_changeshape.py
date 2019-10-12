# Shape Manipulation
# change the shape of an array

import numpy as np


a = np.floor(10*np.random.random((3,4)))
print(a)
print()


b = a.ravel()  # returns the array, flattened
print(b)
print()


b = a.reshape(6,2)  # returns the array with a modified shape
print(b)
print()


a.T  # returns the array, transposed
b = a.T.shape
print(b)
print()


print(a.shape)


# If a dimension is given as -1 in a reshaping operation,
# the other dimensions are automatically calculated:
b = a.reshape(3,-1)  # returns the array with a modified shape
print(b)
print()



# The reshape function returns its argument with a modified shape,
# whereas the ndarray.resize method modifies the array itself
a.resize((2,6))
print(a)