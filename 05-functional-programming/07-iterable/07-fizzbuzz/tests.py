from itertools import islice
import student
import solution


def test_fizzbuzz():
    expected = islice(solution.fizzbuzz(), 1000)
    actual = islice(student.fizzbuzzlist(), 1000)
    assert list(expected) == list(actual)
