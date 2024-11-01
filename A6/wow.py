# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #

import time

# Nested object containing information about the numbers 0-5
nums = {
  # How to display the number 0
  0: {
    0: [1,2], # First row of the grid ( 0 1 2 3 ), light up colums 1 and 2
    1: [0,3], # Second row of the grid ( 0 1 2 3 ), light up colums 0 and 3
    2: [0,3],
    3: [0,3],
    4: [0,3],
    5: [0,3],
    6: [1,2]
  },
  1: {
    0: [1,2],
    1: [2],
    2: [2],
    3: [2],
    4: [2],
    5: [2],
    6: [1,2,3]
  },
  2: {
    0: [1,2],
    1: [3],
    2: [3],
    3: [1,2],
    4: [0],
    5: [0],
    6: [0,1,2,3]
  },
  3: {
    0: [0,1,2],
    1: [3],
    2: [3],
    3: [0,1,2],
    4: [3],
    5: [3],
    6: [0,1,2]
  },
  4: {
    0: [0,3],
    1: [0,3],
    2: [0,3],
    3: [0,1,2,3],
    4: [3],
    5: [3],
    6: [3]
  },
  5: {
    0: [0,1,2,3],
    1: [0],
    2: [0],
    3: [0,1,2,3],
    4: [3],
    5: [3],
    6: [0,1,2,3]
  }
}

def print_num(n):
  '''
  Display a number in a 7x4 grid
  Input: n - number to display
  Return: None  '''
  width = 4
  height = 7
  print()
  for y in range(height):
    for x in range(width):
      if x in nums[n][y]:
        print('🟩', end='')
      else:
        print('⬛', end='')
    print()

def main():
  '''
  Main function
  Displays the numbers 5 to 0 in reverse order
  Input: nil
  Return: None '''
  for i in range(5, -1, -1):
    print_num(i)
    time.sleep(1)

  print("\n\n *** LIFTOFF! 🚀 *** \n\n")

# Call the main function
main()