import unittest

import pytest

from parentheses import matching_parentheses

@pytest.mark.parametrize('string', ["hello world", "", "()"])
def test_parameterized_tests(string):
    assert matching_parentheses(string), f"{string} is not"

@pytest.mark.parametrize('string', ["(hello world", ")", "("])
def test_parameterized_tests2(string):
    assert not matching_parentheses(string), f"{string} is not balanced"


