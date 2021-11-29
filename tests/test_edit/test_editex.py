# external
import pytest

# project
import textdistance


ALG = textdistance.Editex


@pytest.mark.parametrize('left, right, expected', [
    ('', '', 0),
    ('nelson', '', 12),
    ('', 'neilsen', 14),
    ('ab', 'a', 2),
    ('ab', 'c', 4),
    ('ALIE', 'ALI', 1),
    ('', 'MARTHA', 12),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert actual == expected

    actual = ALG(external=True)(left, right)
    assert actual == expected


@pytest.mark.parametrize('left, right, params, expected', [
    ('MARTHA', 'MARHTA', dict(match_cost=2), 12),
    ('MARTHA', 'MARHTA', dict(match_cost=4), 24),
    ('MARTHA', 'MARHTA', dict(group_cost=1, local=True), 3),
    ('MARTHA', 'MARHTA', dict(group_cost=2, local=True), 4),
    ('MARTHA', 'MARHTA', dict(mismatch_cost=4, local=True), 5),
])
def test_distance_with_params(left, right, params, expected):
    actual = ALG(external=False, **params)(left, right)
    assert actual == expected

    actual = ALG(external=True, **params)(left, right)
    assert actual == expected
