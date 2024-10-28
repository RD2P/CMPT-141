# anything that can be done with loops can also be done with recursion
'''
base case - smallest possible instance of the problem
branch 1: base case
branch 2: recursive case, slightly smaller version of the problem
'''

# find number of ancestors at nth generation
def num_ancestors(n):
  if n == 1:
    return 1
  else:
    return num_ancestors(n-1) * 2


# add all the squares of nums from 0-N (0^2 + 1^2 + 2^2 + ...)
def sum_squares(n):
  if n <= 0:
    return 0
  else:
    return n**2 + sum_squares(n-1)
  

# sum all number up to n
def sum_n(n):
  if n == 1:
    return 1
  else:
    return n + sum_n(n-1)




print(sum_n(3))