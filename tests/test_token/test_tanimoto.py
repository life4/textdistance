# built-in
from math import isclose, log2

# external
import pytest

# project
from textdistance import Tanimoto


@pytest.mark.parametrize('left, right, coefficient', [
    ('a', 'a', 1.0),
    ('a', 'b', 0.0),
    ('ab', 'ac', 1.0 / 3),
    ('', '', 1.0),
    ('', 'a', 0.0),
])
def test_tanimoto_distance_and_normalization(left, right, coefficient):
    algorithm = Tanimoto(external=False)
    distance = -log2(coefficient) if coefficient else float('inf')
    assert isclose(algorithm.distance(left, right), distance)
    assert isclose(algorithm.normalized_similarity(left, right), coefficient)
    assert isclose(algorithm.normalized_distance(left, right), 1 - coefficient)
    assert algorithm.maximum(left, right) == 0


@pytest.mark.parametrize('left, right, coefficient', [
    ('a', 'a', 1.0),
    ('a', 'b', 0.0),
    ('ab', 'ac', 1.0 / 3),
])
def test_tanimoto_raw_similarity_is_logarithmic(left, right, coefficient):
    expected = log2(coefficient) if coefficient else float('-inf')
    assert isclose(Tanimoto(external=False)(left, right), expected)


@pytest.mark.parametrize('options, left, right, coefficient', [
    ({'as_set': True}, 'aab', 'ab', 1.0),
    ({'qval': 2}, 'aab', 'aac', 1.0 / 3),
    ({'qval': 0}, 'a b', 'a c', 1.0 / 3),
])
def test_tanimoto_normalization_preserves_token_options(options, left, right, coefficient):
    algorithm = Tanimoto(external=False, **options)
    assert isclose(algorithm.normalized_similarity(left, right), coefficient)
