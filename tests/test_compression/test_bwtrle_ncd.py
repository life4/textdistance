# built-in
from math import isclose

# external
import pytest

# project
import textdistance


ALG = textdistance.bwtrle_ncd


@pytest.mark.parametrize('left, right, expected', [
    ('test', 'test', 0.6),
    ('test', 'nani', 0.8),
])
def test_similarity(left, right, expected):
    actual = ALG(left, right)
    assert isclose(actual, expected)
