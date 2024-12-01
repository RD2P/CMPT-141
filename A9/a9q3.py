# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #


def read_pokedata(filename):
  '''Reads a file of pokemon information and creates a database of pokemon info
  Input: filename - a name of a file containing tabular pokemon info
  Returns:
    dict: A dictionary where each key is a Pokemon's name and each value is a dictionary containing:
        - name (str): The Pokemon's name.
        - type (str): The Pokemon's type.
        - locations (list): A list of strings representing locations where the Pokemon can be found.'''
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


def  find_continents(db):
  '''Constructs a list of all continents in which pokemon can be found, given a database of pokemon info
  Input:
    dict of pokemon info with pokemon names as the key and each value is a dict in the form:
        - name (str): The pokemon's name.
        - type (str): The pokemon's type.
        - locations (list): A list of locations where the pokemon can be found.
  Returns: a list of unique continents where pokemon can be found'''
  result = []
  for record in db.values():
    for loc in record['locations']:
      if loc not in result:
        result.append(loc)
  return result


def  pokemon_in_continent(db, continent):
  '''Creates a list of pokemon names that can be found in the continent
  Input:
    dict of pokemon info with pokmon names as the key and each value is a dict in the form:
        - name (str): The pokemon's name
        - type (str): The pokemon's type
        - locations (list): A list of locations where the Pokemon can be found
    continent (str): The name of the continent
  Returns: a list of pokemon names that can be found in the continent'''
  result = []
  for record in db.values():
    if continent in record["locations"]:
      result.append(record["name"])
  return result


def count_types(db, names):
  '''Creates a dictionary of pokemon types and the number of pokemon of each type in the list
  Input:
    dict of pokemon info with pokmon names as the key and each value is a dict in the form:
        - name (str): The pokemon's name.
        - type (str): The pokemon's type.
        - locations (list): A list of locations where the pokemon can be found.
    names (list): A list of pokemon names
  Returns: a dictionary of pokemon types and the number of pokemon of each type in the list'''
  result = {}
  for name in names:
    type = db[name]["type"]
    if type in result:
      result[type] += 1
    else:
      result[type] = 1
  return result

# since a9q3 is being imported in a9q4 for testing, this prevents the code below from executing during testing
if __name__ == "__main__": 
  db =  read_pokedata('pokemonLocations.txt') # create the database
  continents = find_continents(db) # create list of continents

  # iterate over the continents to print the write up about each continent
  for continent in continents:
    pokemons = pokemon_in_continent(db, continent)
    print(f"{continent}: {len(pokemons)} total pokemon")
    print(count_types(db, pokemons))
    print()