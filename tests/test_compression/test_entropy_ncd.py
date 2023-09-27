# built-in
from math import isclose

# external
import hypothesis
import pytest

# project
import textdistance


ALG = textdistance.entropy_ncd


@pytest.mark.parametrize('left, right, expected', [
    ('test', 'test', 1),
    ('aaa', 'bbb', 0),
    ('test', 'nani', 0.6),
])
def test_similarity(left, right, expected):
    actual = ALG.similarity(left, right)
    assert isclose(actual, expected)


@hypothesis.given(text=hypothesis.strategies.text(min_size=1))
def test_simmetry_compressor(text):
    rev = ''.join(reversed(text))
    assert isclose(ALG._compress(text), ALG._compress(rev))


@hypothesis.given(text=hypothesis.strategies.text(min_size=1))
def test_idempotency_compressor(text):
    # I've modified idempotency to some kind of distributivity for constant.
    # Now it indicates that compressor actually does compression.
    assert ALG._get_size(text * 2) < ALG._get_size(text) * 2


@hypothesis.given(
    left=hypothesis.strategies.text(min_size=1),
    right=hypothesis.strategies.characters(),
)
def test_monotonicity_compressor(left, right):
    if right in left:
        return
    assert ALG._get_size(left) <= ALG._get_size(left + right)


@hypothesis.given(
    left1=hypothesis.strategies.text(min_size=1),
    left2=hypothesis.strategies.text(min_size=1),
    right=hypothesis.strategies.characters(),
)
def test_distributivity_compressor(left1, left2, right):
    if right in left1 or right in left2:
        return
    actual1 = ALG._get_size(left1 + left2) + ALG._get_size(right)
    actual2 = ALG._get_size(left1 + right) + ALG._get_size(left2 + right)
    assert actual1 <= actual2


@hypothesis.given(text=hypothesis.strategies.text(min_size=1))
def test_normalization_range(text):
    assert 0 <= ALG.normalized_similarity(text, text) <= 1
    assert 0 <= ALG.normalized_distance(text, text) <= 1
