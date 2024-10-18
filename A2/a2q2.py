# Glenn Raphael De Los Reyes
# 11189672
# gld141

def roadtrip_cost(distance, fuel_price, fuel_efficiency):
  '''
  Calculate the total fuel cost of a roadtrip
  Inputs:
    distance: distance of the trip in km
    fuel_price: the price of fuel in dollars
    fuel_efficiency:  efficiency of the car measured in miles per gallon
  Returns: total fuel cost of the trip in dollars
  '''

  # km/L = 0.425mpg
  km_per_L = 0.425 * fuel_efficiency
  L_per_km = 1 / km_per_L
  total_fuel_use = distance * L_per_km
  total_fuel_cost = total_fuel_use * fuel_price
  return round(total_fuel_cost, 2)

print("Roadtrip calculator")
distance = int(input("Enter the distance of the trip in km: "))
fuel_cost = float(input("Enter the cost of fuel per liter: "))
efficiency = float(input("Enter the efficiency of vehicle in MPG: "))

print("The total fuel cost of your roadtrip is $", roadtrip_cost(distance,fuel_cost,efficiency), sep="")