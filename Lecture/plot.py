import matplotlib.pyplot as plt

data = [2,3,6,7,8,9,7,6,5,7,6,7,8,9,7,6,5]

averages = []
for i in range(7, len(data)):
  sum = 0
  for j in range(i-7, i):
    sum+=data[j]
  averages.append(sum/7)

# print(len(averages))

plt.plot(range(10), averages)
plt.show()