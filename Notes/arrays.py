# lists can have different data types
l = [4, 'a', 5.0]
# lists can change in length
l.append('b')
print(l)


# Arrays
# Can't change size
# Same data type
# Data stored in contigous block of memory
# Good for images, number of data does not change, same data type, need fast operations
# NUMPY library for working with arrays

# numpy has ND array
# pandas is built on top of numpy 


import numpy as np


# create arrays with lists or tuples
A = np.array([1,3,4,5])
print(A) # not separated by commas
B = np.array((6,7,8,9))
print(B)


# 2D arrays (has to be rectangular shape)
AA = np.array([[1,2],[3,4],[5,6]])
print(AA) # separated into rows
BB = np.array(((1,2),(3,4)))
print(BB)


# creating zeros
z = np.zeros(5)
print(z) # default data type is float
# create 2d zeros by giving list or tuple
zz = np.zeros([3,4])
print(zz)
tt = np.zeros((2,2))
print(tt)


# ones
o = np.ones(4)
print(o)