word_count = 0

with open('book.txt') as f:
  for line in f:
    word_count += len(line.strip().split(' '))

print(word_count)