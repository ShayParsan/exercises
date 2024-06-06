import unittest

import pytest
from _pytest.python_api import approx

from mergesort import merge_sort, merge_sorted, split_in_two


@pytest.mark.parametrize(('test_input', 'expected'), [([1, 2, 3, 4, 5, 6], ([1, 2, 3], [4, 5, 6]))])
def test(test_input, expected):
    assert split_in_two(test_input) == approx(expected, abs=0.1)


@pytest.mark.parametrize(('test_input', 'expected'),
                         [(ns, (ns[0:len(ns) // 2], ns[len(ns) // 2:])) for ns in [[x] for x in range(100)]])
def test2(test_input, expected):
    assert split_in_two(test_input) == approx(expected, abs=0.1)


@pytest.mark.parametrize(('test_input', 'expected'), [(ns, (sorted(ns))) for ns in [[x] for x in range(100)]])
def test3(test_input, expected):
    assert merge_sort(test_input) == approx(expected, abs=0.1)


@pytest.mark.parametrize(('test_input', 'expected'),
                         [((ns, ks), sorted(ns + ks)) for ns, ks in [([x], [x+1]) for x in range(100)]])
def test4(test_input, expected):
    assert merge_sorted(*test_input) == approx(expected, abs=0.1)

