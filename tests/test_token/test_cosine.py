# built-in
from math import isclose

# external
import pytest

# project
import textdistance


ALG = textdistance.Cosine


@pytest.mark.parametrize('left, right, expected', [
    ('test', 'text', 3.0 / 4),
    ('nelson', 'neilsen', 5.0 / pow(6 * 7, .5)),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert isclose(actual, expected)

    actual = ALG(external=True)(left, right)
    assert isclose(actual, expected)
