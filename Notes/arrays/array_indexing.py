import numpy as np

# indexing 2d arrays
dd = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dd)
print(dd[1,2]) # 6
print(dd[:,2]) # [3 6 9]
print(dd[1,:]) # [4 5 6]
print(dd[0,1:]) # [2 3]
print(dd[1:, 1:]) # [[5 6] [8 9]]