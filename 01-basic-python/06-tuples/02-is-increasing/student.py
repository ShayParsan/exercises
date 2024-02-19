def is_increasing(ns):
    ms = drop(ns)
    liso = list(zip(ns,ms))
    for i in range(len(liso)):
        if liso[i][0] > liso[i][1]:
            return False
    
    return True
        
    
def drop(ns):
    return ns[1:]

print(is_increasing([1, 2, 3, 4, 4, 7]))