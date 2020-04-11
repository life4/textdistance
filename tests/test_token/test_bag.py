# external
import pytest

# project
import textdistance


ALG = textdistance.Bag


@pytest.mark.parametrize('left, right, expected', [
    ('qwe', 'qwe', 0),
    ('qwe', 'erty', 3),
    ('qwe', 'ewq', 0),
    ('qwe', 'rtys', 4),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert actual == expected

    actual = ALG(external=True)(left, right)
    assert actual == expected
