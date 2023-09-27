# external
import pytest

# project
import textdistance


ALG = textdistance.DamerauLevenshtein

COMMON = [
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
    ('ab', 'bc', 2),
]


@pytest.mark.parametrize('left, right, expected', COMMON + [
    ('ab', 'bca', 3),
    ('abcd', 'bdac', 4),
])
def test_distance_restricted(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert actual == expected

    actual = ALG(external=True)(left, right)
    assert actual == expected

    actual = ALG()._pure_python_restricted(left, right)
    assert actual == expected


@pytest.mark.parametrize('left, right, expected', COMMON + [
    ('ab', 'bca', 2),
    ('abcd', 'bdac', 3),
])
def test_distance_unrestricted(left, right, expected):
    actual = ALG(external=False, restricted=False)(left, right)
    assert actual == expected

    actual = ALG(external=True, restricted=False)(left, right)
    assert actual == expected

    actual = ALG()._pure_python_unrestricted(left, right)
    assert actual == expected
