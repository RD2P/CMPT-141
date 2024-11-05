import numpy as np

coffee_shops = [x for x in range(1,100)]


CA = np.array(coffee_shops)

# size
print(CA.size)

# largest element
print(CA[CA.size - 1])

# first 5 elements
for i in range(6):
  print(CA[i])