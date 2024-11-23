# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #

import a8q4 as pk

# Empty list
book = {} 
source = "Pikachu"
target = "Mewtwo"
expected = False
result = pk.can_evolve(book, source, target)
if result != expected:
  print(f"Testing can_evolve() with {book}, source: {source}, target: {target}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# Not in the book
book = {
  "charmander": ["charmeleon"],
} 
source = "Pikachu"
target = "Mewtwo"
expected = False
result = pk.can_evolve(book, source, target)
if result != expected:
  print(f"Testing can_evolve() with {book}, source: {source}, target: {target}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# Simple evolution
book = {
  "charmander": ["charmeleon"],
}
source = "charmander"
target = "charmeleon"
expected = True
result = pk.can_evolve(book, source, target)
if result != expected:
  print(f"Testing can_evolve() with {book}, source: {source}, target: {target}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# 2 stage evolution
book = {
  "charmander": ["charmeleon"],
  "charmeleon": ["charizard"]
}
source = "charmander"
target = "charmeleon"
expected = True
result = pk.can_evolve(book, source, target)
if result != expected:
  print(f"Testing can_evolve() with {book}, source: {source}, target: {target}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# Multiple evolution paths
book = {
  "eevee": ["vaporeon", "jolteon", "flareon"],
  "vaporeon": ["bigger vaporeon"],
  "jolteon": ["bigger jolteon"],
  "flareon": ["bigger flareon"]
}
source = "eevee"
target = "bigger flareon"
expected = True
result = pk.can_evolve(book, source, target)
if result != expected:
  print(f"Testing can_evolve() with {book}, source: {source}, target: {target}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")

# No paths
book = {
  "eevee": ["vaporeon", "jolteon", "flareon"],
  "pikachu": ["raichu"]
}
source = "eevee"
target = "raichu"
expected = False
result = pk.can_evolve(book, source, target)
if result != expected:
  print(f"Testing can_evolve() with {book}, source: {source}, target: {target}")
  print(f"Expected: {expected}")
  print(f"Got: {result}")


print("\nAll tests done!")