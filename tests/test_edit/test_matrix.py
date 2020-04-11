# external
import pytest

# project
import textdistance


ALG = textdistance.Matrix
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
    ('', '', 1),
    ('', 'a', 0),
    ('abcd', 'abcd', 1),
    ('A', 'C', -3),
    ('G', 'G', 7),
    ('A', 'A', 10),
    ('T', 'A', -4),
    ('T', 'C', 0),
    ('A', 'G', -1),
    ('C', 'T', 0),
])
def test_distance(left, right, expected):
    actual = ALG(NW_MATRIX, symmetric=True)(left, right)
    assert actual == expected
