# Indexing, Slicing and Iterating
# nd

# understanding fromfunction()

import numpy as np

def f(x,y):
    return 10 * x + y

b = np.fromfunction(f,(5,4),dtype=int)
print(b)
print()


print(b[2,3])
print()

print(b[0:5, 1])    # each row in the second column of b
print()

print(b[ : ,1])     # equivalent to the previous example
print()

print(b[1:3, : ])   # each column in the second and third row of b
print()

# fewer indices
print(b[-1])        # b[-1, :]
