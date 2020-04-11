# external
import pytest

# project
import textdistance


ALG = textdistance.NeedlemanWunsch
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


@pytest.mark.parametrize('left, right, expected', [
    ('AGACTAGTTAC', 'CGAGACGT', 16),
])
def test_distance_matrix(left, right, expected):
    sim_matrix = textdistance.Matrix(NW_MATRIX, symmetric=True)
    actual = ALG(gap_cost=5, sim_func=sim_matrix)(left, right)
    assert actual == expected


def sim_ident(x, y):
    if x == y:
        return 1
    else:
        return -1


@pytest.mark.parametrize('left, right, expected', [
    ('GATTACA', 'GCATGCU', 0),
])
def test_distance_ident(left, right, expected):
    actual = ALG(sim_func=sim_ident)(left, right)
    assert actual == expected


@pytest.mark.parametrize('left, right, expected', [
    ('CGATATCAG', 'TGACGSTGC', -5),
    ('AGACTAGTTAC', 'TGACGSTGC', -7),
    ('AGACTAGTTAC', 'CGAGACGT', -15),
])
def test_distance_ident_with_gap_5(left, right, expected):
    actual = ALG(gap_cost=5, sim_func=sim_ident)(left, right)
    assert actual == expected
