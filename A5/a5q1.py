# Raphael De Los Reyes
# 11189672
# gld141  

populationsSK = [
  ['Pelican Narrows', 2703] ,
  ['Saskatoon', 222035] ,
  ['Moose Jaw', 33617] ,
  ['La Ronge', 5905],
]

# a) cities with at least 10k population
citiesSK = [x for x in populationsSK if x[1] >= 10000]

# b) town smaller than 40k population
smallCities = [x for x in populationsSK if x[1] < 40000]

# c) cities and town names
namesSK = [x[0] for x in populationsSK]

# d) long names
longNames = [x for x in populationsSK if len(x[0]) > 8]