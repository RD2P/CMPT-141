from time import perf_counter

start = perf_counter()

# task
for i in range(1000):
  for j in range(1000):
    a = 3 + 4

duration = perf_counter() - start

print("Task ran in", duration, 'seconds')

