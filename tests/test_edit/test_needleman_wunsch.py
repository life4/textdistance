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


@pytest.mark.parametrize('gap_cost', [0, .5, 2, 3])
def test_custom_gap_normalization(gap_cost):
    alg = ALG(gap_cost=gap_cost)
    assert alg.normalized_similarity('abc', 'abc') == 1
    assert alg.normalized_distance('abc', 'abc') == 0
    assert alg.normalized_similarity('abc', 'ab') == pytest.approx(2 / 3)
    assert alg.normalized_distance('abc', 'ab') == pytest.approx(1 / 3)


@pytest.mark.parametrize('gap_cost, expected', [(0, 0), (.5, 1 / 3), (2, 2 / 3), (3, .75)])
def test_custom_gap_nonmatching_normalization(gap_cost, expected):
    alg = ALG(gap_cost=gap_cost)
    assert alg.normalized_similarity('abc', 'xyz') == pytest.approx(expected)
    assert alg.normalized_distance('abc', 'xyz') == pytest.approx(1 - expected)
