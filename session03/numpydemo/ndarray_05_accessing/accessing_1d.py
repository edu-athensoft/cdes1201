# Indexing, Slicing and Iterating
# 1d

import numpy as np

a = np.arange(10)**3
print(a)

# slicing
print(a[2:5])

# equivalent to a[0:6:2] = -1000
# from start to position 6, exclusive, set every 2nd element to -1000
a[:6:2] = -1000
print(a)

# reversed a
print(a[ : :-1])

# Iterating
for i in a:
    print(i**(1/3.))

