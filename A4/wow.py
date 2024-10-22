# Raphael De Los Reyes
# 11189672
# gld141

# Optimize number of dice for Pikachu to play, given the health of Koffing

import random as r
import matplotlib.pyplot as plt

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

def simulate(dice, koff_health):
  wins = 0
  # Simulate the attack 1000 times, increment wins with each successful attack
  for i in range(1000):
    if attack(dice, koff_health) == True:
      wins += 1
  percentage = round((wins / 1000) * 100, 1)
  return percentage

koffing_health = int(input("Enter Koffing health: "))

# Plot with matplotlib
win_percentage_list = []

for i in range(1, 51):
  win_percentage = simulate(i,koffing_health)
  win_percentage_list.append(win_percentage)
  print(f"Dice: {i} --> Win %: {win_percentage}")

max_win_precentage = max(win_percentage_list)
optimal_number_dice = win_percentage_list.index(max_win_precentage) + 1
print("Optimal number of dice:", optimal_number_dice)

# Graph labels
plt.title(f"Win % with number of dice given Koffing health of {koffing_health}")
plt.xlabel('Number of dice')
plt.ylabel('Win percentage (%)')

plt.plot([i for i in range(50)], win_percentage_list)
plt.show()