def rotate(xs, n):
    new_xs = [None] * len(xs)  
    for i in range(len(xs)):
        new_index = (i + n) % len(xs)  
        new_xs[new_index] = xs[i]      
    return new_xs

print(rotate([1,4,3],2))
