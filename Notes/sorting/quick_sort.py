l = ['abc', 'a', 'bb']

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

print(sort_by_length(m))