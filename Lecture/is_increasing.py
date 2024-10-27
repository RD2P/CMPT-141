def is_increasing(L):
  if len(L) <= 1:
    return True
  else:
    for i in range(1,len(L)):
      if L[i] < L[i-1]:
        return False
    return True
  

testLs = [
  [],
  [1],
  [1,2,3,4],
  [4,3,2]
]

for i in testLs:
  print(is_increasing(i))