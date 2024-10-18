# Glenn Raphael De Los Reyes
# 11189672
# gld141


def walls_area(W, H):
  '''
  Calculate the area of four equal-sized walls
  Inputs:
    W: width of the wall in meters
    H: height of the wall in meters
  Returns: area of the wall in square meters
  '''
  return 4 * W * H


def roof_area(W, T):
  '''
  Calculate the surface area of a pyramid-shaped roof
  Inputs:
    W: base of each triangle in meters
    T: slant height in meters
  Returns: area of the roof in square meters
  '''

  return 2 * W * T


def total_cost(w, h, t, c):
  '''
  Calculate the total cost of paint given the house dimensions and cost of paint
  Inputs:
    w: width of walls and base of roof triangles in meters
    h: height of walls  in meters
    t: slant height of roof in meters
    c: cost of paint per meter squared in dollars
  Returns: total cost of paint to cover the house in dollars
  '''

  walls_surface_area = walls_area(w,h)
  roof_surface_area = roof_area(w,t)
  total_surface_area = walls_surface_area + roof_surface_area

  total_cost_of_paint = total_surface_area * c

  return total_cost_of_paint

print("House Paint Calculator:")
width = int(input("Width of house walls (m): "))
height = int(input("Height of house walls (m): "))
# assuming valid user input for slant_height means it needs to be gemoetrically possible, so slant_height > width / 2 
slant_height = int(input("Roof slant height (m): ")) 
paint_cost = int(input("Cost of paint for each square meter ($): "))

print("Total cost for an all-blue house : $", total_cost(width, height, slant_height, paint_cost), sep="")