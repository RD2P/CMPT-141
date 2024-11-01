# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #


# import function from file named a6q3, which is in the same directory
from a6q3 import closest_to_zero


# Assume 3 arguments (num1, num2, num3) are passed to the function and they're all integers


# num1 is closest to zero
# Test when the first if statement in the for loop is never satisfied
num1, num2, num3 = 1,2,3 
expected = 1
result = closest_to_zero(num1, num2, num3)
if result != expected:
  print("Testing closest_to_zero() with", num1, num2, num3, "   Expected:", expected, " Got: ", result)


# num2 is closest to zero
# Test when first if statement is satisfied on the first iteration of the loop
num1, num2, num3 = 2, 0, 3 
expected = 0
result = closest_to_zero(num1, num2, num3)
if result != expected:
  print("Testing closest_to_zero() with", num1, num2, num3, "   Expected:", expected, " Got: ", result)


# num3 is closest to zero
# Test when first if statement is satisfied on the second and last iteration of the loop
num1, num2, num3 = 3, 2, 0
expected = 0
result = closest_to_zero(num1, num2, num3)


# Two arguments are closest - first and third, and both positive
# Test when the elif is satisfied on the second iteration of the loop, but the nested if statement is not hit
num1, num2, num3 = 1, 2, 1
expected = 1
result = closest_to_zero(num1, num2, num3)
if result != expected:
  print("Testing closest_to_zero() with", num1, num2, num3, "   Expected:", expected, " Got: ", result)


# Two arguments are closest - second and third, and both are positive
# Test when the if statement is hit on the first iteration, and the elif on the second iteration of the loop is hit
num1, num2, num3 = 2, 1, 1
expected = 1
result = closest_to_zero(num1, num2, num3)
if result != expected:
  print("Testing closest_to_zero() with", num1, num2, num3, "   Expected:", expected, " Got: ", result)


# Two arguments are closest, both negative
# Test when the elif is hit but the nested if statement is not hit
num1, num2, num3 = -1, 2, -1
expected = -1
result = closest_to_zero(num1, num2, num3)
if result != expected:
  print("Testing closest_to_zero() with", num1, num2, num3, "   Expected:", expected, " Got: ", result)


# Two arguments are closest, one negative, one positive
# Test when the elif is hit and the nested if statement is hit
num1, num2, num3 = -1, 2, 1
expected = 1
result = closest_to_zero(num1, num2, num3)
if result != expected:
  print("Testing closest_to_zero() with", num1, num2, num3, "   Expected:", expected, " Got: ", result)


print("\nAll tests done.")