def target_sum(ns, target):
    for x in ns:
        print(f"x is {x}")
        for y in ns:
            print(f" y is  {y}")
            if x + y == target:
                return True
    return False

print(target_sum([0, 0, 3], 6))