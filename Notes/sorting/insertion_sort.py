l = [3,2,4,5,1,8,7,9]

def sort(L):
  for i in range(1,len(L)):
    j = i
    while L[j-1] > L[j] and j > 0:
      L[j-1], L[j] = L[j], L[j-1]
      j -= 1
  return L

print(sort(l))