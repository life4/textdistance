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


@pytest.mark.parametrize('external', [False, True])
@pytest.mark.parametrize('left, right, expected', [
    ('aB', 'bA', 1),
    ('bA', 'aB', 1),
    ('aB', 'bCa', 2),
    ('bCa', 'aB', 2),
    ('aBCd', 'BDac', 3),
    ('AaB', 'bAA', 2),
    ('aBca', 'Caba', 2),
    ('AbC', 'aBc', 0),
    ('', 'aB', 2),
])
def test_unrestricted_custom_comparison(left, right, expected, external):
    distance = ALG(
        test_func=lambda a, b: a.lower() == b.lower(),
        restricted=False,
        external=external,
    )
    assert distance(left, right) == expected


@pytest.mark.parametrize('left, right, expected', [
    ([[1], [2]], [[2], [1]], 1),
    ([[1], [2]], [[2], [3], [1]], 2),
])
def test_unrestricted_custom_comparison_unhashable_tokens(left, right, expected):
    distance = ALG(test_func=lambda a, b: a == b, restricted=False, external=False)
    assert distance(left, right) == expected


@pytest.mark.parametrize('restricted, expected', [(True, 3), (False, 2)])
def test_custom_comparison_preserves_restricted_variant(restricted, expected):
    distance = ALG(
        test_func=lambda a, b: a.lower() == b.lower(),
        restricted=restricted,
        external=False,
    )
    assert distance('aB', 'bCa') == expected


@pytest.mark.parametrize('left, right, expected', [
    ('a' * 40, 'b' * 40, 40),
    ('a' * 200, 'b' * 10, 200),
    (list(range(40)), list(range(40, 80)), 40),
])
def test_custom_comparison_has_quadratic_comparison_count(left, right, expected):
    comparisons = 0

    def equal(a, b):
        nonlocal comparisons
        comparisons += 1
        return a == b

    distance = ALG(test_func=equal, restricted=False, external=False)
    assert distance(left, right) == expected
    assert comparisons <= 2 * len(left) * len(right)
