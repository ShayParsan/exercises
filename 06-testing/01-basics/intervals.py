def overlapping_intervals(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    if start1 in range(start2, end2) or end1 in range(start2, end2):
        return True
    else:
        return False

print(overlapping_intervals((0, 3), (4, 5)))
