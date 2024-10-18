# Raphael De Los Reyes
# 11189672
# gld141

import random as r

secret = r.randint(1,10)
guess = int(input("Guess a number from 1 to 10: "))

while guess != secret:
  if guess < secret:
    print("Too low...")
  elif guess > secret:
    print("Too high...")
  guess = int(input("Guess a number from 1 to 10: ")) # allow another guess and an opportunity to break out of the while loop

print("You got it, the secret number was", secret)