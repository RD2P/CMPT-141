# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #


def create_new_pokemon(species, type, level):
  '''
  Creates a new dictionary of pokemon info based in arguments
  Inputs:
    species:  pokemon species (e.g. Pikachu)
    type:     pokemon type (e.g. Electric type)
    level:    pokemon level (e.g. 68)
  Returns:  A dictionary of pokemon info in the form of { Species: string, Type: string, Level: int }
  '''
  return {
    "Species": species,
    "Type": type,
    "Level": level
  }

# Initialize empty list for pokedex
pokeDex = []

print("Welcome to PokeDex Logger!\nEnter info for newly-caught Pokemon.\n")

enter_new = 'y'

# Ask user for pokemon information while enter_new is 'y'
while enter_new == 'y':
  species = input("\nPokemon’s species? ")
  type = input("Pokemon’s type? ")
  level = input("Pokemon’s level? ")
  pokeDex.append(create_new_pokemon(species, type, level))
  enter_new = input("\n-----\nAre there more pokemon to add (y/n)? ")

print("\nLogging complete. Printing final PokeDex:\n")

# Display final PokeDex
print(pokeDex)