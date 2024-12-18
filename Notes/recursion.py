'''
anything that can be done with loops can also be done with recursion
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


# bottles of beer on the wall
def bottles_of_beer(n):
  if n <= 0:
    print("All gone!")
  else:
    print(n, "bottles of beer on the wall.")
    print(n, "bottles of beer.")
    print("Take one down, pass it around.")
    print(n-1, "bottles of beer on the wall.\n")
    bottles_of_beer(n-1)


# determine if n is even (maximum recursion depth is 1000)
def is_even(n):
  if n == 2:
    return True
  elif n == 1:
    return False
  else:
    return is_even(n-2)


# print 1 to n
def print_nums(n, current=0):
  if current < n:
    print(current)
    print_nums(n, current+1)

print_nums(4)

def isPalindrome(s):
  if len(s) <= 1:
    return True
  if s[0] != s[-1]:
    return False
  return isPalindrome(s[1:-1])

print(isPalindrome("eevee"))


# recursion limit helps guard against stack overflows
# import sys
# print(sys.getrecursionlimit()) # 1000

