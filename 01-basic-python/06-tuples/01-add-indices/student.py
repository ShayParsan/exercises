def add_indices(xs):
    ys = tuple(range(len(xs)))
    new_list = list(zip(ys, xs))
    return new_list

print(add_indices(['a', 'b', 'c']))
