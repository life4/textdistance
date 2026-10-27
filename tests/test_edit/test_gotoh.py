# external
import pytest

# project
import textdistance


ALG = textdistance.Gotoh
# https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
NW_MATRIX = {
    ('A', 'A'): 10,
    ('G', 'G'): 7,
    ('C', 'C'): 9,
    ('T', 'T'): 8,
    ('A', 'G'): -1,
    ('A', 'C'): -3,
    ('A', 'T'): -4,
    ('G', 'C'): -5,
    ('G', 'T'): -3,
    ('C', 'T'): 0,
}


def sim_ident(x, y):
    if x == y:
        return 1
    else:
        return -1


@pytest.mark.parametrize('left, right, expected', [
    ('GATTACA', 'GCATGCU', 0),
])
def test_distance_ident(left, right, expected):
    actual = ALG(gap_open=1, gap_ext=1, sim_func=sim_ident)(left, right)
    assert actual == expected


@pytest.mark.parametrize('left, right, expected', [
    ('GATTACA', 'GCATGCU', 0),
    ('AGACTAGTTAC', 'TGACGSTGC', 1.5),
    ('AGACTAGTTAC', 'CGAGACGT', 1),
])
def test_distance_ident_with_gap_05(left, right, expected):
    actual = ALG(gap_open=1, gap_ext=.5, sim_func=sim_ident)(left, right)
    assert actual == expected


@pytest.mark.parametrize('left, right, expected', [
    ('AGACTAGTTAC', 'CGAGACGT', -15),
])
def test_distance_ident_with_gap_5(left, right, expected):
    actual = ALG(gap_open=5, gap_ext=5, sim_func=sim_ident)(left, right)
    assert actual == expected


@pytest.mark.parametrize('left, right, expected', [
    ('', '', 0), ('a', '', -2), ('', 'a', -2),
    ('abc', '', -3), ('', 'abc', -3),
])
def test_empty_sequences(left, right, expected):
    assert ALG(gap_open=2, gap_ext=.5)(left, right) == expected


@pytest.mark.parametrize('left, right', [('a', 'b'), ('ab', 'a'), ('a', 'ab')])
def test_empty_prepared_sequences(left, right):
    assert ALG(qval=3)(left, right) == 0
