# built-in
from math import isclose

# external
import hypothesis
import pytest

# project
import textdistance


ALGS = (
    textdistance.arith_ncd,
    textdistance.bwtrle_ncd,
    textdistance.bz2_ncd,

    # too slow, makes CI flaky
    # textdistance.lzma_ncd,

    textdistance.rle_ncd,
    textdistance.zlib_ncd,
    textdistance.sqrt_ncd,
    textdistance.entropy_ncd,
)


@pytest.mark.parametrize('alg', ALGS)
def test_monotonicity(alg):
    same = alg('test', 'test')
    similar = alg('test', 'text')
    diffirent = alg('test', 'nani')
    assert same <= similar <= diffirent


@pytest.mark.parametrize('alg', ALGS)
@hypothesis.given(
    left=hypothesis.strategies.text(),
    right=hypothesis.strategies.text(),
)
def test_simmetry(left, right, alg):
    assert alg.similarity(left, right) == alg.similarity(right, left)
    assert alg.distance(left, right) == alg.distance(right, left)
    assert alg.normalized_similarity(left, right) == alg.normalized_similarity(right, left)
    assert alg.normalized_distance(left, right) == alg.normalized_distance(right, left)


@pytest.mark.parametrize('alg', ALGS)
@hypothesis.given(
    left=hypothesis.strategies.text(),
    right=hypothesis.strategies.text(),
)
def test_is_normalized(left, right, alg):
    a = alg(left, right)
    d = alg.distance(left, right)
    nd = alg.normalized_distance(left, right)
    assert a == d == nd


@pytest.mark.parametrize('alg', ALGS)
@hypothesis.given(
    left=hypothesis.strategies.text(),
    right=hypothesis.strategies.text(),
)
def test_normalized_by_one(left, right, alg):
    s = alg.normalized_similarity(left, right)
    d = alg.normalized_distance(left, right)
    assert isclose(s + d, 1)
