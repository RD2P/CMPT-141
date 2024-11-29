# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #

from a9q3 import read_pokedata, find_continents, pokemon_in_continent, count_types

# ----- read_pokedata() -----
# tests assume the input file is correctly formatted

# Test case 1: empty file
input = 'test1.txt'
expected = {}
result = read_pokedata(input)
if result != expected:
  print(f"Testing read_pokedata() with {input}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# Test case 2: one record, one location
input = 'test2.txt'
expected = {"bulbasaur": {"name": "bulbasaur", "type": "grass", "locations": ["South America"]}}
result = read_pokedata(input)
if result != expected:
  print(f"Testing read_pokedata() with {input}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# Test case 3: one record, multiple locations
input = 'test3.txt'
expected = {"bulbasaur": {"name": "bulbasaur", "type": "grass", "locations": ["South America", "Africa", "Asia"]}}
result = read_pokedata(input)
if result != expected:
  print(f"Testing read_pokedata() with {input}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

print("\n*** All read_pokedata() tests done ***\n")


# ----- find_continents() ----- #

print("\n*** All find_continents() tests done ***\n")

# -----  pokemon_in_continent() ----- #

print("\n*** All pokemon_in_continent() tests done ***\n")

# ----- count_types() ----- #

print("\n*** All count_types() tests done ***\n")
