# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #


def create_new_pokemon(species, type, level):
  '''
  Creates a new dictionary of pokemon info based on arguments
  Inputs:
    species:  string, pokemon species (e.g. Pikachu)
    type:     string, pokemon type (e.g. Electric type)
    level:    integer, pokemon level (e.g. 68)
  Returns:  A dictionary of pokemon info in the form of { Species: string, Type: string, Level: integer }
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

  # Create new pokemon dictionary and add it to pokeDex
  pokeDex.append(create_new_pokemon(species, type, level))
  # Ask user if they want to add another pokemon
  enter_new = input("\n-----\nAre there more pokemon to add (y/n)? ")

print("\nLogging complete. Printing final PokeDex:\n")

# Display final PokeDex
print(pokeDex)