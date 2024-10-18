
# Glenn Raphael De Los Reyes
# 11189672
# gld141

# ==== HELPERS ==== #

def draw_fish():
  '''Print a fish 🐟'''
  print('''><(((('>''')


def draw_cat():
  '''Print a cat 😺'''
  print(''' 
 /\_/\  
( o.o ) 
 > ^ < / ''')


def draw_dead_cat():
  '''Print a dead cat 😿'''
  print(''' 
 /\_/\  
( x.x ) 
 > ^ < / ''')


def draw_FAT_cat():
  '''Print a very chubby cat 😿⚖️'''
  print(''' 
   /\_____________/\  
  (      a.a        ) 
 (      > ^ <        )  / 
(    m        m       )/''')


def get_info():
  '''
  Ask user input to determine the number of cats and fish 🙋‍♂️
  Returns the numbers of cats and fish
  '''
  num_cats = int(input("How many cats are there? 🐈 "))
  num_fish = int(input("How many fish are there? 🐟 "))
  return num_cats, num_fish


def draw(remainder, num_cats, num_fish):
  '''
  Draws the specified number of cats and fish
  Inputs:
    remainder: difference between the numbre of fish and cats
    num_cats: number of cats
    num_fish: number of fish
  Returns: None
  '''
  if remainder > 0: # fish surplus 😻
    for c in range(num_cats - 1):
      draw_cat()
      draw_fish()
    draw_FAT_cat() # this cat hoards the surplus
    draw_fish()
    for i in range(remainder):
      draw_fish()
  elif remainder == 0: # supply perfectly meets demand 🐱
    for c in range(num_cats):
      draw_cat()
      draw_fish()
  else: # fish scarcity 🙀
    for i in range(num_cats - num_fish): # number of cats without fish (i.e. dead cats)
      draw_dead_cat()
    for f in range(num_fish): # fish that can be distributed
      draw_cat()
      draw_fish()


# ==== MAIN FUNCTION ==== #

def start():
  '''The function that calls the helper functions'''

  print("Please provide non-negative integers as input 🙏🥺")
  [num_cats, num_fish] = get_info()
  remainder = num_fish - num_cats
  draw(remainder, num_cats, num_fish)


start()