def remove_duplicates(xs):
    new_set = set()
    new_list = []
    for x in xs:
        if x not in new_set:
            new_list.append(x)
            new_set.add(x)
    
    return new_list
