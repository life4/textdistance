# external
import pytest

# project
import textdistance


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
    ('ab', 'bc', 2),
    ('ab', 'bca', 3),
    ('abcd', 'bdac', 4),
])
def test_distance_restricted(left, right, expected):
    alg = textdistance.DamerauLevenshteinRestricted

    actual = alg(external=False)(left, right)
    assert actual == expected

    actual = alg(external=True)(left, right)
    assert actual == expected

    actual = alg()._pure_python(left, right)
    assert actual == expected


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
    ('ab', 'bc', 2),
    ('ab', 'bca', 2),
    ('abcd', 'bdac', 3),
])
def test_distance_unrestricted(left, right, expected):
    alg = textdistance.DamerauLevenshteinUnrestricted

    actual = alg(external=False)(left, right)
    assert actual == expected

    actual = alg(external=True)(left, right)
    assert actual == expected

    actual = alg()._pure_python(left, right)
    assert actual == expected


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
    ('ab', 'bc', 2),
    ('ab', 'bca', 2),
    ('abcd', 'bdac', 3),
])
def test_distance(left, right, expected):
    alg = textdistance.DamerauLevenshtein

    actual = alg(external=False)(left, right)
    assert actual == expected

    actual = alg(external=True)(left, right)
    assert actual == expected

    actual = alg()._pure_python(left, right)
    assert actual == expected
