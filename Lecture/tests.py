# writing test drivers

def double(n):
  return n*n

test_val = 9
expected = 18
if double(test_val) != expected:
  print("Error.")
else:
  print("Correct.")