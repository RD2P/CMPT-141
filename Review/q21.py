total = 0
i = 0
j = 0
while i < 4:
  while j < 6:
    total = total + 1
    j = j + 1
  i = i + 1

print(total) # 6, because j is initialized outside of the while j loop, the loop will not run 4 times