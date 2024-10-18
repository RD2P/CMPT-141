# Raphael De Los Reyes
# 11189672
# gld141

import random as rand
import math as m

rnum = rand.randint(1, 10000) # random integer between 1 and 10000 inclusive
root = int(m.sqrt(rnum)) # get integer square root of random number

print("Your random number is:", rnum)

# if rnum is a perfect square, sqrt of rnum should have no digits after decimal
if root * root == rnum:
  print(rnum, "is a perfect square.")