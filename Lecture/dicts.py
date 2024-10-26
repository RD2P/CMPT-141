d = { 'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 1 }
e = {}
for i,j in d.items():
  # e[j] = i
  print(i,j)

# check if key is in dict
# print('a' in d) --> True
# print(1 in d) --> False

# or check if value is in dict
# print(1 in d.values()) --> True

# for i in d:
#   print(d[i])

# print(d.values())

# l = list(d.values())
# print(l)

# print(d.count(10)) --- Not allowed