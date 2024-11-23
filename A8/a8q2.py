# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #


def reverse_phrase_recursive(L):
  '''
  Reverses a list using recursion
  Input: a list L
  Output: a reversed list'''
  if len(L) == 1:
    return [L[0]]
  else:
    # add the first item in the list to the end of sublist consisting of all but the first item
    return reverse_phrase_recursive(L[1:]) + [L[0]]

def reverse_phrase(S):
  '''
  Reverses a string
  Input: a string S
  Output: the reversed string'''
  # turn the string into list of words
  word_list = S.split(' ')
  # reverse the list using reverse_phrase_recursive
  reversed_list = reverse_phrase_recursive(word_list)
  # join the reversed list back into a string
  reversed_string = ' '.join(reversed_list)
  return reversed_string

print(reverse_phrase(""))