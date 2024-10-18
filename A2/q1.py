def cost_of_meal ( number_of_courses , number_of_diners , price_per_diner ):
  total_cost_of_supplies = number_of_courses * 250
  total_diner_cost = number_of_diners * price_per_diner
  subtotal = total_cost_of_supplies + total_diner_cost
  gratuity = total_diner_cost * 0.15
  return subtotal + gratuity

# 3 course meal for 100 pepole , at $42 .50 each
first_meal = cost_of_meal (3 , 100 , 42.50)

# 5 course meal for 40 people , at $68 .14 each
second_meal = cost_of_meal (5 , 40 , 68.14)

print(first_meal)
print(second_meal)