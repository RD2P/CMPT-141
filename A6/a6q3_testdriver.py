# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #


# import function from file named a6q3, which is in the same directory
from a6q3 import closest_to_zero


# num1 is closest
num1, num2, num3 = 1,2,3 
expected = 1
result = closest_to_zero(num1, num2, num3)
if result != expected:
  print("Testing closest_to_zero() with", num1, num2, num3, "   Expected:", expected, " Got: ", result)


# num2 is closest
num1, num2, num3 = 2, 0, 3 
expected = 0
result = closest_to_zero(num1, num2, num3)
if result != expected:
  print("Testing closest_to_zero() with", num1, num2, num3, "   Expected:", expected, " Got: ", result)


# num3 is closest
num1, num2, num3 = 3, 2, 0
expected = 0
result = closest_to_zero(num1, num2, num3)
if result != expected:
  print("Testing closest_to_zero() with", num1, num2, num3, "   Expected:", expected, " Got: ", result)


# Two arguments are closest, both positive
num1, num2, num3 = 1, 2, 1
expected = 1
result = closest_to_zero(num1, num2, num3)
if result != expected:
  print("Testing closest_to_zero() with", num1, num2, num3, "   Expected:", expected, " Got: ", result)


# Two arguments are closest, both negative
num1, num2, num3 = -1, 2, -1
expected = -1
result = closest_to_zero(num1, num2, num3)
if result != expected:
  print("Testing closest_to_zero() with", num1, num2, num3, "   Expected:", expected, " Got: ", result)


# Two arguments are closest, one negative, one positive
num1, num2, num3 = -1, 2, 1
expected = 1
result = closest_to_zero(num1, num2, num3)
if result != expected:
  print("Testing closest_to_zero() with", num1, num2, num3, "   Expected:", expected, " Got: ", result)


print("\nAll tests done.")