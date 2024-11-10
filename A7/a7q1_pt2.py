# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #

import numpy as np

# System of equations:
# 2x + y + 3z = 9
# 5x + 3y + z = 15
# x + 7y + 12z = 0

# array of coefficients
A = np.array([[2, 1, 3], 
              [5, 3, 1], 
              [1, 7, 12]])

# array of constants
B = np.array([9, 15, 0])

# solve system
print(np.linalg.solve(A, B))

# Output:
# [ 4.16842105 -2.27368421  0.97894737]

# Hand Solution:
# x = 4.1685
# y = -2.2737
# z = 0.9789