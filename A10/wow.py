# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #

import numpy as np
import os


# extract the data from input
def get_data(filename):
  '''Reads the input file and grabs data
  Input: filename
  Output: dim - dimensions of the farm, data - list of tuples as initial coordinates of fruit trees
  '''
  with open(filename) as f:
    lines = f.readlines()
    dim = lines[0]
    init = []
    for line in lines[1:]:
      points = line.strip().split(' ')
      init.append([tuple(map(int,x.split(','))) for x in points])
  return int(dim), init


# populate farm w initial data, assuming 5 lines in the input text
def populate_initial_farm(F, data):
    '''Add initial coordinates to the farm
    Input: 
      F - 2D array representing the farm
      data - starting coordinates of fruit trees
    Output:
      None (modifies F)
    '''
      
    for i in range(1,5):
      for point in data[i-1]:
        x,y = point
        F[x, y] = i


def get_proximity(r, c):
  '''Find the fruit trees near the empty space
  Input:
    r - row of the empty space
    c - column of the empty space
  Output:
    prox - list of adjacent trees
  '''
  # proximity will be stored as list of 4 items in this order:
  # [up, down, left, right]
  prox = [None, None, None, None]
  # up
  if r - 1 >= 0:
    prox[0] = int(F[r - 1, c])
  # down
  if r + 1 < R:
    prox[1] = int(F[r + 1, c])
  # left
  if c - 1 >= 0:
    prox[2] = int(F[r, c - 1])
  # right
  if c + 1 < C:
    prox[3] = int(F[r, c + 1])
  return prox


def find_dominant_between_two(a,b):
  '''Find the dominant between two fruit trees
  Input:
    a - first fruit tree
    b - second fruit tree
  Output:
    dominant fruit tree, encoded according to the fruit_legend dictionary
  '''
  if a == b:
    return a
  elif sorted([a,b]) == [1,2]:
    return 2
  elif sorted([a,b]) == [1,3]:
    return 1
  elif sorted([a,b]) == [2,3]:
    return 3


def find_dominant(prox):
  '''Find the dominant fruit tree given a list of adjacent fruit trees
  Input:
    prox - list of adjacent trees
  Output:
    dominant fruit tree, encoded according to the fruit_legend dictionary
  '''
  # trees adjacent to the empty space
  adj = [x for x in prox if x is not None and x != 0]
  match adj:
    # no tree adjacent -> None
    case []:
      return None
    # only one tree adjacent -> that tree
    case [i]: 
      return i
    # if all adjacent trees are the same -> that tree
    case [*items] if len(set(items)) == 1:
      return items[0]
    # stellarfruit in adjacent -> stellarfruit
    case [*items] if 5 in items: 
      return 5
    # one of each basic fruit -> stellarfruit
    case [a, b, c, d] if sorted([a,b,c,d]) == [1,2,3,4]: 
      return 5
    # at least one of water, fire, grass, and no stellar and no jolt -> None
    case [*items] if (5 not in items and 4 not in items and items.count(1) and items.count(2) and items.count(3)): 
      return None
    # no stellar, has jolt, and not one of each basic fruit -> jolt
    case [*items] if 5 not in items and 4 in items and sorted(items) != [1,2,3,4]:
      return 4
    case [*items] if len(set(items)) == 2:
      a,b = list(set(items))
      return find_dominant_between_two(a, b)
    # 2 or 3 items of water, fire, grass
    case [*items] if ((len(items) == 2 or len(items) == 3) and 5 not in items and 4 not in items): 
      # if 3 items, remove the duplicate
      if len(items) == 3:
        a,b,c = items
        a,b = list(set(items))
      # else if 2 items, unpack
      else:
        a,b = items
      return find_dominant_between_two(a, b)
    case _:
      # all the combinations of trees adjacent to the empty space should be covered by the cases above
      print(prox)
      return 'There is no case found!' 


def create_proximity_map(F, R, C):
    '''Create a map of trees in proximity of each empty space
    Input:
      F - 2D array representing the farm
      R - number of rows
      C - number of columns
    Output:
      prox_map - dictionary of coordinates of empty spaces and their adjacent trees
    '''
    prox_map = {}
    for r in range(R):
      for c in range(C):
        point = F[r][c]
        if point == 0:
          prox = get_proximity(r, c)
          prox_map[(r, c)] = prox
    return prox_map


def harvest(F, harvest_count):
  '''Harvest the farm
    Input:
      F - 2D array representing the farm
      harvest_count - dictionary of fruit types and their harvest count
    Output:
      None (modifies harvest_count)'''
  for r in range(R):
    for c in range(C):
      tree = F[r][c]
      if tree != 0:
        harvest_count[tree] += 1


def final_harvest(F, final_harvest_count):
  '''Harvest the farm after last growth cycle
    Input:
      F - 2D array representing the farm
      final_harvest_count - dictionary of fruit types and their final harvest count'''
  for r in range(R):
    for c in range(C):
      tree = F[r][c]
      if tree != 0:
        final_harvest_count[tree] += 1


def create_next_gen(F, prox_map):
    '''Create the next generation of the farm
    Input:
      F - 2D array representing the farm
      prox_map - dictionary of coordinates of empty spaces and their adjacent trees
    Output:
      None (modifies F)
    '''
    # for each empty space, find the dominant fruit tree
    for i in prox_map:
      next_gen = find_dominant(prox_map[i])
      if next_gen:
        F[i] = next_gen

def main(filename):
  '''Main function
  Input:
    filename - name of the file containing the farm layout
  Output:
    None
  '''
  # populate farm with fruits at gen 0
  populate_initial_farm(F, data) 
  prox_map = create_proximity_map(F, R, C)
  year = 0

  while True:
    # spring propagation
    create_next_gen(F, prox_map)

    # check if next generation propagation is the same as current
    # the farm is stable if they're the same
    if prox_map == create_proximity_map(F, R, C): 
      break

    # create new proximity map
    prox_map = create_proximity_map(F, R, C)
    # fall harvest
    harvest(F, harvest_count)
    # increment year
    year += 1

  # final harvest
  final_harvest(F, final_harvest_count)
  # print('Final harvest:', final_harvest_count)

  print('Fruit yield from final year:')
  print('****************************')
  
  for fruit in fruit_legend:
    print(f"{fruit_legend[fruit]} : {final_harvest_count[fruit]}")

  print()
  print(f"Total farm yield after {year} years:")
  print('**********************************')
  for fruit in fruit_legend:
    print(f"{fruit_legend[fruit]} : {harvest_count[fruit]}")


if __name__ == '__main__':
  while True:
    filename = input("Which file would you like to use? ")
    
    # map fruits to ints for ease of working with them
    fruit_legend = {
      1: 'Firefruit',
      2: 'Waterfruit',
      3: 'Grassfruit',
      4: 'Joltfruit',
      5: 'Stellarfruit'
    }

    harvest_count = {
      1: 0,
      2: 0,
      3: 0,
      4: 0,
      5: 0
    }

    final_harvest_count = {
      1: 0,
      2: 0,
      3: 0,
      4: 0,
      5: 0
    }
    
    dim, data = get_data(filename)
    # row and colum of farm
    R = C = dim
    # intialize empty farm of correct dimensions
    F = np.zeros((R, C), dtype=int) 

    main(filename)

    answer = input("\nWould you like to see another file? y/n: ")
    if answer == 'n':
      break
    if answer != 'y' or answer != 'yes':
      answer = input("\nWould you like to see another file? y/n: ")