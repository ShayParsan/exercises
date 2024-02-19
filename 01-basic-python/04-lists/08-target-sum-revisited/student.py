def target_sum(ns, target):
    y = 0
    for x in ns:
        if x + y == target:
            return True
        else:
            y = x
         
    return False
 
print(target_sum([2, 2,], 4))