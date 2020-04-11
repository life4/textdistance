# built-in
from math import isclose

# external
import pytest

# project
import textdistance


ALG = textdistance.StrCmp95


@pytest.mark.parametrize('left, right, expected', [
    ('MARTHA', 'MARHTA', 0.9611111111111111),
    ('DWAYNE', 'DUANE', 0.873),
    ('DIXON', 'DICKSONX', 0.839333333),
    ('TEST', 'TEXT', 0.9066666666666666),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert isclose(actual, expected)

    actual = ALG(external=True)(left, right)
    assert isclose(actual, expected)
