def last_digit(n):
    return n%10 
    
def remove_last_digit(n):
    return n//10

def digits_sum(n):

    sum = 0
    for i in range(n):
        r = last_digit(n)
        c = remove_last_digit(n)
        sum = sum + r
        n = c
        i = i +1
    
    print(sum)
    

digits_sum(1418)
