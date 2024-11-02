import numpy as np

# add, subtract, divide, multiply, power
# must have the same shape
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(a - b)
print(b ** a)
print(b % a)
print()


# do operations with a number
print(a * 2)
print(10 - b)