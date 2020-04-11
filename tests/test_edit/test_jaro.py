# built-in
from math import isclose

# external
import pytest

# project
import textdistance


ALG = textdistance.JaroWinkler


@pytest.mark.parametrize('left, right, expected', [
    ('hello', 'haloa', 0.7333333333333334),
    ('fly', 'ant', 0.0),
    ('frog', 'fog', 0.9166666666666666),
    ('ATCG', 'TAGC', 0.8333333333333334),
    ('MARTHA', 'MARHTA', 0.944444444),
    ('DWAYNE', 'DUANE', 0.822222222),
    ('DIXON', 'DICKSONX', 0.7666666666666666),

    # https://github.com/life4/textdistance/issues/41
    ('Sint-Pietersplein 6, 9000 Gent', 'Test 10, 1010 Brussel', 0.5182539682539683),
])
def test_distance(left, right, expected):
    actual = ALG(winklerize=False, external=False)(left, right)
    assert isclose(actual, expected)

    actual = ALG(winklerize=False, external=True)(left, right)
    assert isclose(actual, expected)
