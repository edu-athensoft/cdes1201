# deep copy

import numpy as np

a = np.arange(12).reshape(4,3)

d = a.copy()                          # a new array object with new data is created
print(d is a)
print()

print(d.base is a)
print()


d[0,0] = 9999
print(d)

print(a)

# copy after slicing
a = np.arange(int(1e8))
b = a[:100].copy()
print(b)
del a  # the memory of ``a`` can be released.
print(b)