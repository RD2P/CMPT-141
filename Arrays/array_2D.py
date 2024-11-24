import numpy as np

turbines = [ 
  [ 2.5, 2.2, 3.4],
  [ 3.5, 2.9, 4.4],
  [ 9.1, 3.4, 6.5]]

# 2d array

A = np.array(turbines)
print(A, '\n')

# dimensions of wind farm
print('dimension: ', A.ndim)
print('shape', A.shape)

# 3rd row, 1st col  
print(A[2,0]) # or
print(A[2][0])

# average
print('ave', A.mean()) # average of all items
print()

# average of subset first 2 of first 2 rows
subset = A[:2,:2]
print(subset)
print(np.sum(subset)/subset.size)
print(np.average(subset))

# sum everything
print(np.sum(A), '\n')

for i in turbines:
  print(i) # print each row

for i in turbines: # print each item
  for j in i:
    print(j)