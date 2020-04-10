from math import isclose

import pytest

import textdistance


ALG = textdistance.bwtrle_ncd


@pytest.mark.parametrize('left, right, expected', [
    ('test', 'test', 0.6),
    ('test', 'nani', 0.8),
])
def test_similarity(left, right, expected):
    actual = ALG(left, right)
    assert isclose(actual, expected)
