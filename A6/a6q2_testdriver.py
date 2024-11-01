# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #


from testing_blackbox_improvedAverage import improvedAverage
# i.e. the improvedAverage() function is sitting in a file called "testing_blackbox_improvedAverage.py"


# The empty list is a special case
test = []
# None, since the list is empty
expected = None
result = improvedAverage(test)
if result != expected:
  print("Testing improvedAverage() with", test, "   Expected:", expected, " Got: ", result)


# Less than 20 in the list
test = [1, 2, 3, 4, 5]
# None, since there are less than 20 values
expected = None
result = improvedAverage(test)
if result != expected:
  print("Testing improvedAverage() with", test, "   Expected:", expected, " Got: ", result)


# More than 20 items
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
# True, average of last 10 is greater than average of other values
expected = True
result = improvedAverage(test)
if result != expected:
  print("Testing improvedAverage() with", test, "   Expected:", expected, " Got: ", result)


# More than 20 items
test = [110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# False, since the average of last 10 is less than the average of other values
expected = False
result = improvedAverage(test)
if result != expected:
  print("Testing improvedAverage() with", test, "   Expected:", expected, " Got: ", result)


# Exactly 20 in the list, the average of last 10 is greater than the average of other values
# (I have a feeling this is the intentional error 🧙)
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Should return True, not None, since there are 20 numbers
expected = True
result = improvedAverage(test)
if result != expected:
  print("Testing improvedAverage() with", test, "   Expected:", expected, " Got: ", result)


# Average of the last 10 items is equal to the rest
test = [2,2,2,2,2,2,2,2,2,1,3,1,3,2,2,2,2,2,2,2,2,2,2]
# False, since the average of the last 10 values is not GREATER than the average of the rest
expected = False
result = improvedAverage(test)
if result != expected:
  print("Testing improvedAverage() with", test, "   Expected:", expected, " Got: ", result)


# All zeros
test = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# False, since the average of the last 10 values is not GREATER than the average of the rest
expected = False
result = improvedAverage(test)
if result != expected:
  print("Testing improvedAverage() with", test, "   Expected:", expected, " Got: ", result)


# Negative numbers
test = [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3]
# False - the average of last 10 values is less than average of the rest of the items
expected = False
result = improvedAverage(test)
if result != expected:
  print("Testing improvedAverage() with", test, "   Expected:", expected, " Got: ", result)


print("\nAll tests done.")