import re


def ababa(string):
    return re.fullmatch(r'(.+)(.+)\1\1', string)
