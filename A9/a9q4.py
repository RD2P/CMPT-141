# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #

from a9q3 import read_pokedata, find_continents, pokemon_in_continent, count_types

# ----- read_pokedata() -----
# tests assume the input file is correctly formatted

# Test case 1: one record, one location
input = 'test2.txt'
expected = {"bulbasaur": {"name": "bulbasaur", "type": "grass", "locations": ["South America"]}}
result = read_pokedata(input)
if result != expected:
  print(f"Testing read_pokedata() with {input}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# Test case 2: one record, multiple locations
input = 'test3.txt'
expected = {"bulbasaur": {"name": "bulbasaur", "type": "grass", "locations": ["South America", "Africa", "Asia"]}}
result = read_pokedata(input)
if result != expected:
  print(f"Testing read_pokedata() with {input}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# Test case 3: multuple pokemon
input = 'test4.txt'
expected = {
  "bulbasaur": {"name": "bulbasaur", "type": "grass", "locations": ["South America", "Africa", "Asia"]},
  "charmander": {"name": "charmander", "type": "fire", "locations": ["North America", "Europe"]},
  }
result = read_pokedata(input)
if result != expected:
  print(f"Testing read_pokedata() with {input}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

print("\n*** All read_pokedata() tests done ***\n")


# ----- find_continents() ----- #

# empty db
input = {}
expected = []
result = find_continents(input)
if result != expected:
  print(f"Testing find_continents() with {input}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# one pokemon, one continent
input = {
  "bulbasaur": {"name": "bulbasaur", "type": "grass", "locations": ["Asia"]}
}
expected = ["Asia"]
result = find_continents(input)
if result != expected:
  print(f"Testing find_continents() with {input}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# one pokemon, multiple continents
input = {
  "bulbasaur": {"name": "bulbasaur", "type": "grass", "locations": ["Asia", "South America", "Africa"]}
}
expected = ["Asia", "South America", "Africa"]
result = find_continents(input)
if sorted(result) != sorted(expected):
  print(f"Testing find_continents() with {input}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# multiple pokemon, same continent
input = {
  "bulbasaur": {"name": "bulbasaur", "type": "grass", "locations": ["Asia"]},
  "squirtle": {"name": "squirtle", "type": "water", "locations": ["Asia"]},
}
expected = ["Asia"]
result = find_continents(input)
if sorted(result) != sorted(expected):
  print(f"Testing find_continents() with {input}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# multiple pokemon, multiple continents
input = {
  "bulbasaur": {"name": "bulbasaur", "type": "grass", "locations": ["Asia", "South America", "Africa"]},
  "squirtle": {"name": "squirtle", "type": "water", "locations": ["Asia"]},
}
expected = ["Asia", "South America", "Africa"]
result = find_continents(input)
if sorted(result) != sorted(expected):
  print(f"Testing find_continents() with {input}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

print("\n*** All find_continents() tests done ***\n")

# -----  pokemon_in_continent() ----- #

# empty db and empty string for continent
input = {}
continent = ""
expected = []
result = pokemon_in_continent(input, continent)
if sorted(result) != sorted(expected):
  print(f"Testing pokemon_in_continent() with {input} and {continent}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# One pokemon with one location, and searching the same continent
db = {
  "bulbasaur": {"name": "bulbasaur", "type": "grass", "locations": ["Asia"]}
}
continent = "Asia"
expected = ["bulbasaur"]
result = pokemon_in_continent(db, continent)
if result != expected:
  print(f"Testing pokemon_in_continent() with {db} and {continent}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# One pokemon with one location, and searching a different continent
db = {
  "bulbasaur": {"name": "bulbasaur", "type": "grass", "locations": ["Asia"]}
}
continent = "Africa"
expected = []
result = pokemon_in_continent(db, continent)
if result != expected:
  print(f"Testing pokemon_in_continent() with {db} and {continent}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# Multiple pokemon with multiple locations, and searching one of the locations
db = {
  "bulbasaur": {"name": "bulbasaur", "type": "grass", "locations": ["Asia", "Africa"]},
  "charmander": {"name": "charmander", "type": "fire", "locations": ["Asia"]},
}
continent = "Asia"
expected = ["bulbasaur", "charmander"]
result = pokemon_in_continent(db, continent)
if result != expected:
  print(f"Testing pokemon_in_continent() with {db} and {continent}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# Multiple pokemon with multiple locations, and no pokemon in the searched continent
db = {
  "bulbasaur": {"name": "bulbasaur", "type": "grass", "locations": ["Asia", "Africa"]},
  "charmander": {"name": "charmander", "type": "fire", "locations": ["Asia"]},
}
continent = "South America"
expected = []
result = pokemon_in_continent(db, continent)
if result != expected:
  print(f"Testing pokemon_in_continent() with {db} and {continent}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

print("\n*** All pokemon_in_continent() tests done ***\n")

# ----- count_types() ----- #

# Empty db and empty names
db = {}
names = []
expected = {}
result = count_types(db, names)
if result != expected:
  print(f"Testing pokemon_in_continent() with {db} and {names}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# One type, one pokemon
db = {
  "charmander": {"name": "charmander", "type": "fire", "locations": ["Asia"]}
}
names = ["charmander"]
expected = {"fire": 1}
result = count_types(db, names)
if result != expected:
  print(f"Testing pokemon_in_continent() with {db} and {names}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# Multiple pokemon, same type
db = {
  "charmander": {"name": "charmander", "type": "fire", "locations": ["Asia"]},
  "bulbasaur": {"name": "bulbasaur", "type": "fire", "locations": ["Asia"]}
}
names = ["charmander", "bulbasaur"]
expected = {"fire": 2}
result = count_types(db, names)
if result != expected:
  print(f"Testing pokemon_in_continent() with {db} and {names}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# Multiple pokemon, different types
db = {
  "charmander": {"name": "charmander", "type": "fire", "locations": ["Asia"]},
  "bulbasaur": {"name": "bulbasaur", "type": "grass", "locations": ["Asia"]}
}
names = ["charmander", "bulbasaur"]
expected = {"fire": 1, "grass": 1}
result = count_types(db, names)
if result != expected:
  print(f"Testing pokemon_in_continent() with {db} and {names}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")


print("\n*** All count_types() tests done ***\n")
