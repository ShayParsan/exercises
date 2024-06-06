def group_by(xs, key_function):
    groups = {}
    for x in xs:
        key = key_function(x)
        if key in groups:
            groups[key].append(x)
        else:
            groups[key] = [x]
    return groups