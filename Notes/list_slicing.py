# make list of even numbers [0,50)
x = [x for x in range(50) if x % 2 == 0]

print(x)

y = [i for i in range(10)]
print(y[2:8:2]) # start, stop (exclusive), step