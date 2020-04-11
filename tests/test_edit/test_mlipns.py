# external
import pytest

# project
import textdistance


ALG = textdistance.MLIPNS


@pytest.mark.parametrize('left, right, expected', [
    ('', '', 1),
    ('a', '', 0),
    ('', 'a', 0),
    ('a', 'a', 1),
    ('ab', 'a', 1),
    ('abc', 'abc', 1),
    ('abc', 'abcde', 1),
    ('abcg', 'abcdeg', 1),
    ('abcg', 'abcdefg', 0),
    ('Tomato', 'Tamato', 1),
    ('ato', 'Tam', 1),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert actual == expected

    actual = ALG(external=True)(left, right)
    assert actual == expected
