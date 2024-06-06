import re


def correct_dates(string):
    return re.sub(r'([1-9]|1[0-2])/([1-9]|[1-2][0-9]|3[0-1])/(\d{2}|\d{4})', r'\2/\1/\3', string)


