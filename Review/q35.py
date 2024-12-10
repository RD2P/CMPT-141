# should grab all negative nums
def getNegs(L):
  result = []
  for num in L:
    if not num > 0: # wrong line
      result.append(num)
  return result

# print(getNegs([10, 0, -3, 0, 6, -7])) # still get the 0s

sum = 0
for i in range(2,1002,2):
  sum = sum + i
print(sum)