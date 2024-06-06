import unittest

import pytest
from pytest import approx

from mystatistics import average


@pytest.mark.parametrize('ns, expected', [([1, 2], 1.5)])
def test_average(ns, expected):
    assert average(ns) == expected
