def drop_nth(xs, n):
    e_index = xs.index(n)
    new_xs = xs[:e_index] + xs[e_index+1:]
    return new_xs
