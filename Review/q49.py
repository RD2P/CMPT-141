# print all 2 letter permutations in s
s = 'ABCDEFG'

res = []
# can have AA, BB
# for l1 in s:
#   for l2 in s:
#     res.append(l1+l2)

for i in range(len(s)):
  for j in range(len(s)):
    if i != j:
      print(s[i] + s[j])

print(len(res))
print(res)
