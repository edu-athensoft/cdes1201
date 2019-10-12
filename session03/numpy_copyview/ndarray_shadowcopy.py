# view or shadow copy

import numpy as np

a = np.arange(12)

c = a.view()
print(c is a)
print()

print(c.base is a)                        # c is a view of the data owned by a
print()

print(c.flags.owndata)
c.shape = 2,6                      # a's shape doesn't change
print(a.shape)

c[0,4] = 1234                      # a's data changes
print(a)
print()

a = np.arange(24)
a = a.reshape(4,6)
print(a)
s = a[ : , 1:3]
# s[:] = 10
print(s)
print(a)
