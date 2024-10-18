# Raphael De Los Reyes
# 11189672
# gld141


# import function from the file a3q4.py
from a3q3 import get_effectiveness 

# Testing
types = ["normal", "fire", "water", "grass", "electric", "ice"]
for a in types:
  print(a, "attacks:")
  for d in types:
    print(f"    {d}:", get_effectiveness(a, d))