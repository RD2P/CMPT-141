# Raphael De Los Reyes
# 11189672
# gld141

print("\n\n---Let's catch some pokemon 😈 ---\n\n")
pokemon_caught = []
catch = 'y'

# Phase 1: catch pokemon
while catch == 'y':
  new_pokemon = input("What pokemon did you catch? ")
  pokemon_caught.append(new_pokemon)
  print("So far you've caught:", pokemon_caught, "\n")
  catch = input("Do you want to catch a new pokemon? (y/n) ")

print("\n\n--- Now let's go to the gym! 💪 ---")
gym_team = []

def print_pokemons():
  '''Procedure to print pokemons in collection and in the gym team'''
  print("\nPokemon in your collection:", pokemon_caught)
  print("Pokemon on your gym team:", gym_team, "\n")

print_pokemons()

# Phase 2: transfer pokemons from the collection to the gym team
while len(gym_team) < 6 and len(pokemon_caught) > 0:
  add_to_gym_team = input("What Pokemon will you add to your team? ")
  pokemon_caught.remove(add_to_gym_team)
  gym_team.append(add_to_gym_team)
  print(add_to_gym_team.upper(), ", I CHOOSE YOU!", sep='')
  print_pokemons()

print("\n\n--- Now we're ready for the gym 🥊 ---\n\n")