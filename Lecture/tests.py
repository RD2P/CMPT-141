# writing test drivers

def double(n):
  return n*n

input = 9
expected = 18
reason = "Checking correct input"
result = double(input)
if result != expected:
  print("Error:", input, expected, result, reason)
else:
  print("Correct.")


print("All tests done")