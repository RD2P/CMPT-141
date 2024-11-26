l1 = []
l2 = [1,3,5, 8, 10]

def merge(S1, S2):
  S = []
  while len(S1) > 0 and len(S2) > 0:
    if S1[0] < S2[0]:
      S.append(S1[0])
      del S1[0]
    else:
      S.append(S2[0])
      del S2[0]

  if len(S1) > 0 or len(S2) > 0:
    if len(S1) > 0:
      S.extend(S1)
    elif len(S2) > 0:
      S.extend(S2)

  return S

print(merge(l1,l2))