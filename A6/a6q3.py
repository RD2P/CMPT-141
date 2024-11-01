# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #


def closest_to_zero(num1, num2, num3):
  '''
  Takes 3 values and returns the one that is closest to 0
  Inputs: num1, num2, num3: integers whose distance from 0 will be measured and compared
  Returns:  the integer which is closest to 0;
            if more than one integer is closest, and one is negative and the other positive, return the integer that is positive'''
  
  # Initialize tuple with distane of num1 from 0 and num1 
  closest = (abs(num1), num1)

  # Iterate over the other 2 arguments
  for i in num2,num3:
    if abs(i) < closest[0]: # If current argument is closer to 0, update closest tuple
      closest = (abs(i), i)
    elif abs(i) == closest[0]: # If distance is the same as closest distance...
      # Update closest if closest[1] is negative and i is positive
      if i > closest[1]:  
        closest = (abs(i), i)

  return closest[1]