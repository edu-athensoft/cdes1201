# matrix product


import numpy as np

A = np.array([[1,1],
              [0,1]])

B = np.array([[2,0],
              [3,4]])


# elementwise multiply
c = A * B
print(c)
print()

# matrix product
C = A @ B
print(C)
print()

# matrix product in other way
C = A.dot(B)
print(C)
print()



