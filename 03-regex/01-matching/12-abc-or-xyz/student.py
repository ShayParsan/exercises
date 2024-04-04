import re

def abc_or_xyz(string):
    pattern = re.compile(r'abc|xyz')
    matches = pattern.findall(string)
    
    for i in matches:
        print(i)
