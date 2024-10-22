# Raphael De Los Reyes
# 11189672
# gld141


import matplotlib.pyplot as plt

print("Plotting an equation of the form Ax^B + C")
A = float(input("Value for A: "))
B = float(input("Value for B: "))
C = float(input("Value for C: "))
n = int(input("How many points should we plot? "))

# Graph labels
plt.title('Ax^B + C')
plt.xlabel('x')
plt.ylabel('y')

# Plotting each x,y coordinate
for x in range(n):
  y = A * (x ** B) + C
  plt.plot(x, y, 'b.')

# Showing the graph
plt.show()