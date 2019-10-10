#

import numpy as np

# a 3D array (two stacked 2D arrays)
c = np.array( [[[  0,  1,  2],
                [ 10, 12, 13]],
              [[100,101,102],
                [110,112,113]]])

print(c.shape)

print(c[1,...])         # same as c[1,:,:] or c[1]

print(c[...,2])         # same as c[:,:,2]
