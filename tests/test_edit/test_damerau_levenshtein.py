# external
import pytest

# project
import textdistance


ALG = textdistance.DamerauLevenshtein


@pytest.mark.parametrize('left, right, expected', [
    ('test', 'text', 1),
    ('test', 'tset', 1),
    ('test', 'qwy', 4),
    ('test', 'testit', 2),
    ('test', 'tesst', 1),
    ('test', 'tet', 1),

    ('cat', 'hat', 1),
    ('Niall', 'Neil', 3),
    ('aluminum', 'Catalan', 7),
    ('ATCG', 'TAGC', 2),

    ('ab', 'ba', 1),
    ('ab', 'cde', 3),
    ('ab', 'ac', 1),
    ('ab', 'ba', 1),
    ('ab', 'bc', 2),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert actual == expected

    actual = ALG(external=True)(left, right)
    assert actual == expected

    actual = ALG()._pure_python(left, right)
    assert actual == expected
