def search(c, s):
  if len(s) == 0:
    return False
  if s[0] == c:
    return True
  else:
    return search(c, s[1:])

# def search(c,s):
#   if len(s) == 1:
#     return c == s
#   else:
#     if s[0] == c:
#       return True
#     else:
#       return search(c, s[1:])

print(search('', ''))