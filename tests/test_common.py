# built-in
from math import isclose

# external
import hypothesis
import pytest

# project
import textdistance


ALGS = (
    textdistance.bag,

    textdistance.hamming,
    textdistance.levenshtein,
    textdistance.damerau_levenshtein,
    textdistance.jaro,
    textdistance.jaro_winkler,
    textdistance.mlipns,

    textdistance.lcsseq,
    textdistance.lcsstr,
    textdistance.ratcliff_obershelp,

    textdistance.jaccard,
    textdistance.sorensen,
    textdistance.tversky,
    textdistance.overlap,
    textdistance.cosine,
    textdistance.strcmp95,
    textdistance.monge_elkan,

    textdistance.mra,

    textdistance.prefix,
    textdistance.postfix,
    textdistance.identity,
    # textdistance.length,

    # numpy-based:
    # textdistance.gotoh,
    textdistance.needleman_wunsch,
    textdistance.smith_waterman,
    textdistance.editex,
)


@pytest.mark.parametrize('alg', ALGS)
@hypothesis.given(
    left=hypothesis.strategies.text(),
    right=hypothesis.strategies.text(),
)
def test_normalization_range(left, right, alg):
    assert 0 <= alg.normalized_distance(left, right) <= 1
    assert 0 <= alg.normalized_similarity(left, right) <= 1


@pytest.mark.parametrize('alg', ALGS)
@hypothesis.given(
    left=hypothesis.strategies.text(),
    right=hypothesis.strategies.text(),
)
def test_normalization_by_one(left, right, alg):
    d = alg.normalized_distance(left, right)
    s = alg.normalized_similarity(left, right)
    assert isclose(s + d, 1)


@pytest.mark.parametrize('alg', ALGS)
@hypothesis.given(text=hypothesis.strategies.text())
def test_normalization_same(text, alg):
    assert alg.normalized_distance(text, text) == 0
    if alg is not textdistance.needleman_wunsch:
        assert alg.distance(text, text) == 0
    assert alg.normalized_similarity(text, text) == 1


@pytest.mark.parametrize('alg', ALGS)
@hypothesis.settings(deadline=None)
@hypothesis.given(
    left=hypothesis.strategies.text(min_size=1),
    right=hypothesis.strategies.text(min_size=1),
)
def test_normalization_monotonic(left, right, alg):
    nd = alg.normalized_distance(left, right)
    ns = alg.normalized_similarity(left, right)
    d = alg.distance(left, right)
    s = alg.similarity(left, right)
    assert (nd < ns) == (d < s)


@pytest.mark.parametrize('alg', ALGS)
def test_no_common_chars(alg):
    if alg is textdistance.editex:
        return
    assert alg.similarity('spam', 'qwer') == 0


@pytest.mark.parametrize('alg', ALGS)
def test_empty(alg):
    assert alg.distance('', '') == 0


@pytest.mark.parametrize('alg', ALGS)
def test_unequal_distance(alg):
    if alg.maximum('', 'qwertyui'):
        assert alg.distance('', 'qwertyui') > 0
