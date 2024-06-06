def movies_from_year(movies, year):
    return [n.title for n in movies if n.year == year]


def movies_from_director(movies, actor):
    return [n.title for n in movies if actor in n.actors]


def divisors(ns):
    return [n for n in range(ns + 1) if n >= 1 and ns % n == 0]


