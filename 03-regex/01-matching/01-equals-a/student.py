import re


def equals_a(string):
    return re.fullmatch('a', string)

print(equals_a("a"))