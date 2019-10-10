# Iterating

import numpy as np


def f(x,y):
    return 10 * x + y

b = np.fromfunction(f,(5,4),dtype=int)
print(b)
print()

# iterate
for row in b:
    print(row)

# iterate over all element
for element in b.flat:
    print(element)

