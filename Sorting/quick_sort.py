# l = ['abc', 'a', 'bb']

m = [3,4,2,7,1,3]

# quick sort with last element as pivot
def sort_by_length(my_list):
  if len(my_list) <= 1:
    return my_list
  
  L = []
  E = []
  G = []
  p = my_list[-1]

  for i in my_list:
    if i < p:
      L.append(i)
    elif i > p:
      G.append(i)
    else:
      E.append(i)
  
  L = sort_by_length(L)
  G = sort_by_length(G)

  return L + E + G

def quick_sort(L):
  if len(L) <= 1:
    return L
  
  l, e, g = [], [], []
  pivot = L[-1]

  for i in L:
    if i < pivot:
      l.append(i)
    elif i > pivot:
      g.append(i)
    else:
      e.append(i)     

  return quick_sort(l) + e + quick_sort(g)


# print(sort_by_length(m))

print(quick_sort(m))