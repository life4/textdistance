# built-in
from math import isclose

# external
import pytest

# project
import textdistance


ALG = textdistance.Overlap


@pytest.mark.parametrize('left, right, expected', [
    ('test', 'text', 3.0 / 4),
    ('testme', 'textthis', 4.0 / 6),
    ('nelson', 'neilsen', 5.0 / 6),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert isclose(actual, expected)

    actual = ALG(external=True)(left, right)
    assert isclose(actual, expected)
