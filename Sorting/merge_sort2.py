l = [20, 19, 15, 10, 43]

def merge_sort(L):
  if len(L) <= 1:
    return L
  else:
    # recursively divide
    mid = len(L) // 2
    left = merge_sort(L[ : mid])
    right = merge_sort(L[mid : ])

    # conquer
    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        res.append(left[i])
        i += 1
      else:
        res.append(right[j])
        j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res

print(merge_sort(l))