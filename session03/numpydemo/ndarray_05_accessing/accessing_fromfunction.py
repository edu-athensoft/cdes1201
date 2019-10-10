#

import numpy as np

a = np.fromfunction(lambda i: i, (4,))
print(a)

b = np.fromfunction(lambda i, j: i + j, (2, 3))
print(b)


