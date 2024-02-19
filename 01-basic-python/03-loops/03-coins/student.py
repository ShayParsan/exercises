def coins(one, two, five, goal):
    for i in range(0, one +1):
        if value_one == goal:
            return True
        else:
            for k in range(0,two +1):
                if value_two(two) == goal:
                    return True
                elif value_one(i) + value_two(k) == goal:
                    return True
                else:
                    for m in range(0, five+1):
                        if value_five(m) == goal:
                            return True
                        elif value_one(i) + value_five(m) == goal:
                            return True
                        elif value_two(k) + value_five(m) == goal:
                            return True
                        elif value_one(i)+ value_two(k)+ value_five(m) == goal:
                            return True
                        
    return False          
    
               
def value_one(one):
    return one * 1

def value_two(two):
    return two *2

def value_five(five):
    return five * 5

print(coins(1, 1, 1, 4))