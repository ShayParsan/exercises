import re

#   pattern = re.compile(r'[AEIOUaeiou]*', re.IGNORECASE)
    #matches = pattern.finditer(string)
   # 
  #  for i in matches:
 #       return i
#


def only_vowels(string):
    pattern = re.compile(r'[^AEIOUaeiou]' , re.IGNORECASE)
    if not pattern.search(string):
        return string
    else:
        return None