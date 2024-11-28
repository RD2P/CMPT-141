
def merge(S1, S2):
  S = []
  while len(S1) > 0 and len(S2) > 0:
    if S1[0] < S2[0]:
      S.append(S1[0])
      del S1[0]
    else:
      S.append(S2[0])
      del S2[0]

  if len(S1) > len(S2):
      S.extend(S1)
  else:
      S.extend(S2)
      
  return S

def merge_sort(L):
  if len(L) <= 1:
    return L

  mid = len(L) // 2
  S1 = L[:mid]
  S2 = L[mid:]
  return merge(merge_sort(S1), merge_sort(S2))

l = [6,5,4,3,2,1,4,5,6,7,8]
print(merge_sort(l))