def target_sum(ns, target):
    null = 0
    for i in ns:
        if null == target:
            return True
        else:
            null = null +i
            if null == target:
                return True
        i = i +1
    return False    



print(target_sum([1, 2, 3], 6))

    
    
            
        
