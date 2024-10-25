# Make 
provs = ["SK", "AB", "CA"]
pops = [4200, 4700, 8000]


# for loop
# prov_pops = []
# for i in range(len(provs)):
#   prov_pops.append([provs[i], pops[i]])


# list comprehension
# prov_pops = [[x, y] for x,y in zip(provs, pops)]
# print(prov_pops)


# get index of item in list
# for p in provs:
#   print(provs.index(p))


# Object comprehension
obj = {1: "one", 2: "two"}
obj2 = {3: "three", 4: "four"}
obj3 = {x: "something" for x in obj}
print(obj3)
