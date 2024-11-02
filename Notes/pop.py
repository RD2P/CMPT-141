l = [1, 2, 6, 7, 3, 4, 6, 8, 9, 9]

'''
ways to handle removing things from sequence:
'''
for i in range(len(l)-1, 0, -1):
  if l[i] > 5:
    l.pop(i)


print(l)