# Raphael De Los Reyes
# 11189672
# gld141

import random as r

number_dice = int(input("How many dice does Pikachu have? "))
koffing_health = int(input("How much health does Koffing have? "))

def attack(num_dice, k_health):
  '''
  Assess whether or not an attack is successful
  Inputs:
    num_dice: number of dice Pikachu has
    k_health: Koffing health
  Returns: True if the attack is successful, False if unsuccessful
  '''
  # list of all dice rolls Pikachu makes
  rolls = [r.randint(1,6) for i in range(num_dice)]
  # the attack is unsuccessful with a triplet of 1s
  if rolls.count(1) >= 3:
    return False     

  # 1 x damage from a 6
  damage = rolls.count(6) 
  # 4 x damage from a pair of 5s
  damage += 4 * (rolls.count(5) // 2)   

  if damage >= k_health:
    return True
  else:
    return False

wins = 0
# Simulate the attack 1000 times, increment wins with each successful attack
for i in range(1000):
  if attack(number_dice, koffing_health) == True:
    wins += 1

print(f"Pikachu rolled {number_dice} dice against a Koffing with {koffing_health} health.")
percentage = round((wins / 1000) * 100, 1)
print(f"Pikachu won {wins} out of 1000 times ( {percentage} %)")