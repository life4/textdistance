# built-in
from math import isclose

# external
import pytest

# project
import textdistance


ALG = textdistance.bz2_ncd


@pytest.mark.parametrize('left, right, expected', [
    ('test', 'test', 0.08),
    ('test', 'nani', 0.16),
])
def test_similarity(left, right, expected):
    actual = ALG(left, right)
    assert isclose(actual, expected)
