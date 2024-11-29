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
    dict of pokemon info with pokmon names as the key and each value is a dict in the form:
        - name (str): The Pokemon's name.
        - type (str): The Pokemon's type.
        - locations (list): A list of strings representing locations where the Pokemon can be found.
  Returns: a list of unique continents where pokemon can be found'''
  res = []
  for record in db.values():
    for loc in record['locations']:
      if loc not in res:
        res.append(loc)
  return res


db =  read_pokedata('pokemonLocations.txt')

print(find_continents(db))