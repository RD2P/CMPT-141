# Raphael De Los Reyes
# 11189672
# gld141  


# import is_prime function from the starter file in same directory
from cache_primes_starter import is_prime 


def cache_primes(filename):
  '''
  1. Takes the name of a file containing numbers in list format
  2. Open the given file
  3. Read the numbers in it 
  4. Determine whether or not each number is prime
  5. Store the result in a dictionary
  Inputs: filename, the name of a text file containing numbers in list format
  Returns: cache, a dictionary containing whethere or not each number is a prime { number: bool }
  '''
  
  # Read the file
  f = open(filename, 'r')

  # Initialize the cache dict
  cache = {}

  # Iterate over each line (number) in the file and call is_prime()
  for line in f:
    num = int(line.strip())
    if is_prime(num):
      cache[num] = True # number is prime, store { num: True }
    else:
      cache[num] = False # number is not prime, store { num: False }
  return cache


# Call the function and print the return value
print(cache_primes('numbers.txt'))