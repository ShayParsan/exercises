def split_in_two(ns):
    half = len(ns) // 2
    left = ns[:half]
    right = ns[half:]
    return left, right

def merge_sort(ns):
    left, right = split_in_two(ns)
    left = sorted(left)
    right = sorted(right)
    return sorted(left + right)

def merge_sorted(ns,ks):
    result = (ns + ks)
    result = sorted(result)
    return result

print(merge_sorted([5, 3, 4], [2, 1]))