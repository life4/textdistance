# built-in
from math import isclose

# external
import hypothesis
import pytest

# project
import textdistance


ALG = textdistance.Jaccard


@pytest.mark.parametrize('left, right, expected', [
    ('test', 'text', 3.0 / 5),
    ('nelson', 'neilsen', 5.0 / 8),
    ('decide', 'resize', 3.0 / 9),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert isclose(actual, expected)

    actual = ALG(external=True)(left, right)
    assert isclose(actual, expected)


@hypothesis.given(
    left=hypothesis.strategies.text(),
    right=hypothesis.strategies.text(),
)
def test_compare_with_tversky(left, right):
    td = textdistance.Tversky(ks=[1, 1]).distance(left, right)
    jd = ALG().distance(left, right)
    assert isclose(jd, td)


@hypothesis.given(
    left=hypothesis.strategies.text(),
    right=hypothesis.strategies.text(),
)
def test_compare_with_tversky_as_set(left, right):
    td = textdistance.Tversky(ks=[1, 1], as_set=True).distance(left, right)
    jd = ALG(as_set=True).distance(left, right)
    assert isclose(jd, td)
