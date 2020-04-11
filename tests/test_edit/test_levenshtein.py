# external
import pytest

# project
import textdistance


ALG = textdistance.Levenshtein


@pytest.mark.parametrize('left, right, expected', [
    ('test', 'text', 1),
    ('test', 'tset', 2),
    ('test', 'qwe', 4),
    ('test', 'testit', 2),
    ('test', 'tesst', 1),
    ('test', 'tet', 1),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert actual == expected

    actual = ALG(external=True)(left, right)
    assert actual == expected
