# external
import pytest

# project
import textdistance


@pytest.mark.parametrize('left, right, expected', [
    # The first pass removes BC, and the reverse pass removes FGH.
    ('bcdfgh', 'bcfgh', 5),
    ('bcdf', 'bdf', 3),
    ('bcdf', 'bcf', 3),
    # Keep the library's maximum-code-length scale for shorter codes.
    ('bcdf', 'bcdf', 4),
    ('bcdf', 'ghjk', 0),
    ('bcdfgh', 'b', 0),
    ('', 'bcdf', 0),
])
def test_mra_bidirectional_matching(left, right, expected):
    alg = textdistance.MRA()
    assert alg(left, right) == expected
    assert alg(right, left) == expected
