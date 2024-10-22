# matplot_example.py
# Simple example of how to do very basic plotting using Matplotlib
# Written by Jeff Long, Summer 2023, for CMPT 141, University of Saskatchewan

import matplotlib.pyplot as plt
import random as rand



plt.figure()
plt.title('Plot of meaningless random values')
plt.xlabel('Sample')
plt.ylabel('Random Value')

# loop to generate each data point
# each point is added to the plot using the .plot() method
for s in range(10):
    value = rand.randint(1,20)
    plt.plot(s, value, 'r.')    

# this last method call is necessary to actually display the plot so you can see it!    
plt.show()
