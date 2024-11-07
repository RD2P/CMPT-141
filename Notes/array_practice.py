import numpy as np

# coffee_shops = [x for x in range(1,100)]

# CA = np.array(coffee_shops)

# # size
# print(CA.size)

# # largest element
# print(CA[CA.size - 1]) # just do CA[-1]

# # first 5 elements
# for i in range(6):
#   print(CA[i])

# # len on arrays gets only length of first dimension
# A = np.array([[10,9],[3,4],[8,1]])
# print(len(A))

# print()

# # sorting on arrays, sorts the last dimension
# A.sort()
# print(A)

# print("B")
# B = np.array([[[4,2],[10,3]],[[4,2],[10,3]]])
# B.sort()
# print(B)


# # np operations on scalars
# print(np.sum([2,3,4]))

# A = np.array([[10,9],[3,4],[8,1]])
# print()
# print(A)
# for i in A:
#   for j in i:
#     print(j)

# create array from a range
# A = np.array(range(1,11,2))
# print(A + 1)

# boolean mask indexing
A = np.array([
  [1,2,5],
  [7,3,4],
  [8,2,7]])

# all rows, first 2 cols
# print(A[:,:2])

# first 2 rows, last 2 cols
# print(A[:2, 1:])

B = np.array([
  [1.2, 2.3, 5.6],
  [1.2, 2.3, 5.6],
  [1.2, 2.3, 5.6],
])

# print(A + B)
# print(type(A))
# print(type(A) == int)

# iterating over arrays 
# for x in np.nditer(A):
#   print(x)

# logical indexing
a = np.array([True, True, False])
print(B[a])