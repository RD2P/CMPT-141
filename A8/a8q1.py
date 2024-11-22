# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #

def spaceTime(d):
  '''
  Take a distance in meters and calculate the time required for Zeno's drive to travel this distance
  Input: d in meters
  Output: time in minutes it takes Zeno's drive to travel the distance'''
  if d <= 1:
    return 1
  else:
    return spaceTime(d/2) + 1

def askUser():
  '''Asks user for a distance in meters and calls the spaceTime function to calculate the time required in minutes for Zeno's drive to travel the distance'''
  
  distance = float(input("How far do you want to travel? (meters): "))
  time = spaceTime(distance)
  print("Zeno's drive will require", time, "minutes to get there." )

def testSpaceTime():
  '''
  Calls the spaceTime function on different distances and formats and prints the results'''
  distances = {
    'to Zeno\'s nearest coffee shop': 537,
    'from Moosetopia to its biggest moon': 3.84e8,
    'from our earth to the sun': 1.49e11,
    'from our sun to the nearest star': 4.0e16,
    'across the observable universe': 8.8e26
  }

  print("Zeno's drive requires:")
  for k,d in distances.items():
    print(spaceTime(d), "minutes to travel", d, "meters", k)

askUser()