def total_distance(path, distance):
    total = 0
    prev_city = None

    for city in path:
        if prev_city is not None:
            total += distance(prev_city, city)
        prev_city = city

    return total