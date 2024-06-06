import unittest

import pytest
from search import binary_search, Student, linear_search

@pytest.mark.parametrize("students, target_id, expected_index", [
    ([], 10, None),  # Empty list
    ([Student(10), Student(20), Student(30), Student(40)], 35, None),
    ([Student(10), Student(20), Student(30), Student(40)], 10, 10),
    ([Student(10), Student(20), Student(30), Student(40)], 40, 40),
    ([Student(10), Student(20), Student(30), Student(40)], 25, None),
    ([Student(10), Student(20), Student(40)], 30, None),
    ([Student(10), Student(20), Student(30), Student(40), Student(50)], 45, None),
    ([Student(10), Student(20), Student(30), Student(40), Student(50)], 5, None),
])
def test_linear_search(students, target_id, expected_index):
    assert linear_search(students, target_id) == expected_index

@pytest.mark.parametrize("students, target_id, expected_index", [
    ([], 10, -1),  # Empty list
    ([Student(10), Student(20), Student(30), Student(40)], 35, -1),
    ([Student(10), Student(20), Student(30), Student(40)], 10, 0),
    ([Student(10), Student(20), Student(30), Student(40)], 40, 3),
    ([Student(10), Student(20), Student(30), Student(40)], 25, -1),
    ([Student(10), Student(20), Student(40)], 30, -1),
    ([Student(10), Student(20), Student(30), Student(40), Student(50)], 45, -1),
    ([Student(10), Student(20), Student(30), Student(40), Student(50)], 5, -1),
])
def test_binary_search(students, target_id, expected_index):
    assert binary_search(students, target_id) == expected_index



