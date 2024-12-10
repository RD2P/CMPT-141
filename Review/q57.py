def count_clues(city, x, y, path):
  count = 0
  seen = {}
  if city[x][y] == '*':
    count += 1
  for d in path:
    if d == 'N':
      y += 1
      if (x, y) not in seen:
        seen[(x, y)] = True
        if city[x][y] == '*':
          count += 1
    if d == 'S':
      y -= 1
      if (x, y) not in seen:
        seen[(x, y)] = True
        if city[x][y] == '*':
          count += 1
    if d == 'W':
      x += 1
      if (x, y) not in seen:
        seen[(x, y)] = True
        if city[x][y] == '*':
          count += 1
    if d == 'E':
      x += 1
      if (x, y) not in seen:
        seen[(x, y)] = True
        if city[x][y] == '*':
          count += 1
    for i in seen.items():
      print(i)
  return count
    
city = [
  ['*','','*'],
  ['','*',''],
  ['*','*','*'],
]
x,y = 0,0
path = 'SESE'

print(count_clues(city, x, y, path))