def directors(movies):
    return {n.director for n in movies}


def common_elements(xs, ys):
    return {x for x in xs if x in ys}
