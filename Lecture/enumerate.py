# enumerate is built in function to iterate over sequence while tracking both index and value
# list, tuples, strings

# enumerate(sequence, start=0)

letters = ['a','b','c','d']
for i,v in enumerate(letters):
  print(i,v)


# two ways to iterate over items in dicts
my_dict = {
  1: 'one',
  2: 'two',
  3: 'three'
}

# Simple iteration
for key, value in my_dict.items():
    print(f"{key} = {value}")

# Enumerated iteration
for index, (key, value) in enumerate(my_dict.items()):
    print(f"{index}: {key} = {value}")