import numpy as np

l = [3,2,4,5,1,8,7,6]
arr = np.array([5,4,3,2,1])

# sort by making new sequence
def sort(L):
  S = []
  for n in L:
    i = 0
    while i < len(S) and n >= S[i]:
      i += 1
    S.insert(i, n)
  return S

# sort in place
def sort_in_place(L):
  for i in range(1,len(L)):
    j = i
    while L[j-1] > L[j] and j > 0:
      L[j-1], L[j] = L[j], L[j-1]
      j -= 1
  return L

def sort_array(L):
  for i in range(1, L.size):
    j = i
    while L[j] < L[j-1] and j > 0:
      L[j], L[j-1] = L[j-1], L[j]
      j -= 1
  return L

# print(sort(l))
# print(sort_in_place(l))
print(sort_array(arr))