# Raphael De Los Reyes
# 11189672
# gld141  


# import temperatures data, which is in another file in the same directory
from temperatures_fahrenheit_starter import temperatures


# functions
def fahrenheit_to_celsius(f):
  '''
  Take in a temperature in Fahrenheit and convert to Celsius using: °C = (°F - 32) * 0.56
  Input: f - temp in fahrenheit
  Returns: temp in celsius, to one decimal place
  '''
  celsius = (f - 32) * 5/9 # conversion
  return round(celsius, 1) # round to 1 decimal place and return

def convert_temp_data(list2D):
  '''
  Convert each temp in a 2D list from fahrenheit to celsius
  The conversion is done in place
  Inputs:
    list2D: list of lists containing temp data in fahrenheit
  Returns: None
  '''
  for i in range(len(list2D)):
    for j in range(len(list2D[i])):
      list2D[i][j] = fahrenheit_to_celsius(list2D[i][j])

def get_monthly_averages(list2D):
  '''
  Take a list of lists containing temperature data and returns a list of average temperature for each month
  Inputs:
    list2D: list of lists containing temperatures in celsius for the year 2023
  Returns:
    list of average temperatures for each month of the year
  '''
  avgs = []
  for list in list2D:
    avg = sum(list)/len(list)
    avgs.append(round(avg, 2))
  print(len(avgs))
  return avgs


# function calls
convert_temp_data(temperatures)
monthly_avg_temps = get_monthly_averages(temperatures)

print(
  '''Saskatoon average temperature highs , 2023
  --------------''')

months = [
  "January",
  "February",
  "March",
  "April",
  "May",1
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
]

for i in range(len(monthly_avg_temps)):
  print(f"Average temperature in {months[i]} : {monthly_avg_temps[i]}")