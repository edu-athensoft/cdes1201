# create sequences of numbers and return arrays instead of lists
# linspace()

import numpy as np
from numpy import pi


# generating a sequence accepting int
a = np.linspace(10, 30, 5)
print(a)
print()


# generating a sequence accepting float
a = np.linspace(0, 2, 9)    # 9 numbers from 0 to 2
print(a)
print()


# generating a sequence
x = np.linspace( 0, 2*pi, 10 )        # useful to evaluate function at lots of points
f = np.sin(x)
print(f)
print()

x = np.linspace( 0, 2*pi, 100 )        # useful to evaluate function at lots of points
f = np.sin(x)
print(f)
print()

