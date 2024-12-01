# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #

from a9q3 import read_pokedata, pokemon_in_continent
from a9q3 import find_continents as list_all_continents

db = read_pokedata('pokemonLocations.txt')

# {
#   "bulbasaur": {
#     "name": "bulbasaur",
#     "type": "grass",
#     "locations": ["Asia", "Europe"]
#   }
# }

def list_all_pokemon(db):
  res = []
  for i in db.keys():
    res.append(i)
  return res

def list_all_types(db):
  res = []
  for i in db.values():
    type = i["type"]
    if type not in res:
      res.append(type)
  return res

def show_pokemon_info(db, pokemon):
  type = db[pokemon]["type"]
  locations = db[pokemon]["locations"]
  return type, locations

def show_pokemon_info():
  pokemon = input("Which pokemon do you want to learn about?")
  type, locations = show_pokemon_info(db, pokemon)
  a = ''
  if len(locations) <= 1:
    a = locations[0]
  else:
    a = ", ".join(locations[:-1])
    a += " and " + locations[-1]
  print(f"{pokemon}: A {type} type pokemon. It can be found in {a}.", end="")



# in db, select pokemon where type is "grass"

# learn about pokemons

# - list all pokemons
# - list all types
# - list all