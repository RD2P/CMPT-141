# Raphael De Los Reyes
# 11189672
# gld141

def get_effectiveness(attacking_type, defending_type):
  '''
  Determine the effectiveness of a pokemon attack based on the pokemon types
  Inputs:
    attacking_type: type of attacking pokemon
    defending_type: type of defending pokemon
  Returns: string indicating the effectiveness of the attack
  '''

  # return strings
  okay = "okay"
  effective = "super effective!!!"
  weak = "not very effective"

  # normal attacking
  if attacking_type == "normal":
    return okay
  
  # fire attacking
  elif attacking_type == "fire":
    if defending_type == "fire" or defending_type == "water":
      return weak
    elif defending_type == "grass" or defending_type == "ice":
      return effective
    else:
      return okay
  
  # water attacking
  elif attacking_type == "water":
    if defending_type == "fire":
      return effective
    elif defending_type == "water" or defending_type == "grass":
      return weak
    else:
      return okay
  
  # grass attacking
  elif attacking_type == "grass":
    if defending_type == "water":
      return effective
    elif defending_type == "fire" or defending_type == "grass":
      return weak
    else:
      return okay

  # electric attacking
  elif attacking_type == "electric":
    if defending_type == "water":
      return effective
    elif defending_type == "grass" or defending_type == "electric":
      return weak
    else:
      return okay

  # ice attacking
  elif attacking_type == "ice":
    if defending_type == "grass":
      return effective
    elif defending_type == "normal" or defending_type == "electric":
      return okay
    else:
      return weak

attacking = input("Type of attacking pokemon: ")
defending = input("Type of defending pokemon: ")
print(f"Using {attacking} against {defending} is", get_effectiveness(attacking, defending))