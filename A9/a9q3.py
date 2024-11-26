# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #


def read_pokedata(filename):
  db = {}
  with open(filename) as f:
    for i in f:
      info = i.strip().split(',')
      name = info[0]
      type = info[1]
      locations = info[2:]
      db[name] = {
        "name": name,
        "type": type,
        "locations": []
      }
      for loc in locations:
        db[name]["locations"].append(loc)
  return db

res =  read_pokedata('pokemonLocations.txt')
for i in res.items():
  print(i)