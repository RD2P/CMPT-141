# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #

import numpy as np


def get_equations(file_name):
  '''
  Take in a file name storing equations and returns lists of the equations and the constants
  Input: name of file with system of equations
  Returns: list of equations, list of constants from the file
  '''
  equations = []
  constants = []
  # open and read the file
  with open(file_name, 'r') as f:
    # iterate through each line and append to equations and constants to their respective lists
    for line in f:
      equations.append(line[:line.find('=')].strip())
      constants.append(int(line[line.find('=') + 1:].strip()))
  return equations, constants


def get_var_names(eq_list):
  '''
  Take in list of equations and returns variable names in each equation
  Input: list of equations
  Returns: list of variable names in each equation
  '''
  # split the first equation into terms
  terms = [item.strip() for item in eq_list[0].split('+')]
  var_names = []
  # iterate through each term
  for term in terms:
    for i, char in enumerate(term): # use enumerate to iterate the string with the index and value
      # find the first letter character in the term, this is the start of the variable name
      if char.isalpha():
        var_names.append(term[i:])
        break
  return var_names


def get_coefficients(eq_list):
  '''
  Takes in a list of equations and returns a list of lists containing the coefficients of each equation
  Input: list of equations
  Output: list of lists containing the coefficients of each equation
  '''
  # initialize list to store all the coefficients of all equations
  coefficients = []
  # iterate through each equation
  for eq in eq_list:
    # split the equation into terms
    terms = [x.strip() for x in eq.split('+')]
    # initialize list to store the coefficients of each equation
    eq_coefficients = []
    for term in terms:
      for i, char in enumerate(term):
        # find the first letter character in the term, this is the start of the variable name
        if char.isalpha():
          c = term[:i]
          if c == '': # if there is no coefficient in the term, it means the coefficient is 1 ( e.g. x + y + z)
            eq_coefficients.append(1)
          else:
            eq_coefficients.append(int(c))
          break # break out of the inner for loop
    coefficients.append(eq_coefficients)
  return coefficients


def main():
  '''
  Main function. Asks user for file name, reads equations from file, solves the equations, and prints the solution.
  Returns: None
  '''
  filename = input("Enter equation system file name for solving: ")

  # function calls
  equations, constants = get_equations(filename)
  coefficients = get_coefficients(equations)
  var_names = get_var_names(equations)

  # solve the equations with linalg.solve
  A = np.array(coefficients)
  B = np.array(constants)
  solution = np.linalg.solve(A, B)

  # print solution
  print("Solution for equations from ", filename, ":", sep="")
  result = [(v, float(s)) for v,s in zip(var_names, solution)]
  for (v,s) in result:
    print(f"{v} = {s:.4f}")


main()