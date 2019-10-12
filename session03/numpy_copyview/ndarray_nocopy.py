# not copy at all

import numpy as np

a = np.arange(12)
b = a               # no new object is created
print(b is a)       # a and b are two names for the same ndarray object

b.shape = 3,4       # changes the shape of a
print(a.shape)


#
def f(x):
    print(id(x))

print(id(a))                           # id is a unique identifier of an object
f(a)