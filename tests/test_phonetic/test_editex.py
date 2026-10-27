# external
import pytest

# project
import textdistance


ALG = textdistance.Editex


@pytest.mark.parametrize('left, right, expected', [
    # https://github.com/chrislit/abydos/blob/master/tests/distance/test_distance_editex.py
    ('', '', 0),
    ('nelson', '', len('nelson') * 2),
    ('', 'neilsen', len('neilsen') * 2),
    ('ab', 'a', 2),
    ('ab', 'c', 4),
    ('nelson', 'neilsen', 2),
    ('neilsen', 'nelson', 2),
    ('niall', 'neal', 1),
    ('neal', 'niall', 1),
    ('niall', 'nihal', 2),
    ('nihal', 'niall', 2),
    ('neal', 'nihl', 3),
    ('nihl', 'neal', 3),

    # https://anhaidgroup.github.io/py_stringmatching/v0.3.x/Editex.html
    ('cat', 'hat', 2),
    ('Niall', 'Neil', 2),
    ('aluminum', 'Catalan', 12),
    ('ATCG', 'TAGC', 6),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert actual == expected

    actual = ALG(external=True)(left, right)
    assert actual == expected


@pytest.mark.parametrize('left, right, expected', [
    ('', '', 0),
    ('nelson', '', 12),
    ('', 'neilsen', 14),
    ('ab', 'a', 2),
    ('ab', 'c', 2),
    ('nelson', 'neilsen', 2),
    ('neilsen', 'nelson', 2),
    ('niall', 'neal', 1),
    ('neal', 'niall', 1),
    ('niall', 'nihal', 2),
    ('nihal', 'niall', 2),
    ('neal', 'nihl', 3),
    ('nihl', 'neal', 3),
])
def test_local(left, right, expected):
    actual = ALG(external=False, local=True)(left, right)
    assert actual == expected

    actual = ALG(external=True, local=True)(left, right)
    assert actual == expected


@pytest.mark.parametrize('text, expected', [('a', 1), ('abc', 3), ('AbC', 3)])
def test_configured_match_cost_for_identical_inputs(text, expected):
    assert ALG(match_cost=1, group_cost=2, mismatch_cost=3)(text, text) == expected


def test_default_match_cost_and_empty_input_controls():
    assert ALG()('abc', 'abc') == 0
    assert ALG(match_cost=1, group_cost=2, mismatch_cost=3)('', 'abc') == 9
