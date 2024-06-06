from intervals import overlapping_intervals


def test_overlapping_intervals1():
    assert overlapping_intervals((1, 5), (3, 6))

def test_overlapping_intervals2():
    assert not overlapping_intervals((2, 5), (7, 10))



