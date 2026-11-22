# built-in
from collections import Counter
from math import isclose, log

# external
import pytest

# project
import textdistance


ALGS = (
    textdistance.Jaccard,
    textdistance.Sorensen,
    textdistance.Tversky,
    textdistance.Overlap,
    textdistance.Cosine,
)


@pytest.mark.parametrize('alg', ALGS)
@pytest.mark.parametrize('external', [False, True])
def test_zero_counts_are_absent_from_sets(alg, external):
    left = Counter(a=1, b=0)
    right = Counter(a=2, c=0)
    assert alg(as_set=True, external=external)(left, right) == 1
    assert dict(left) == {'a': 1, 'b': 0}
    assert dict(right) == {'a': 2, 'c': 0}


@pytest.mark.parametrize('alg', ALGS)
@pytest.mark.parametrize('left, right, expected', [
    (Counter(a=0), Counter(b=0), 1),
    (Counter(a=0), Counter(), 1),
    (Counter(), Counter(a=0), 1),
    (Counter(a=0), Counter(b=1), 0),
    (Counter(a=1), Counter(b=0), 0),
])
def test_empty_counter_sets(alg, left, right, expected):
    assert alg(as_set=True, external=False)(left, right) == expected


@pytest.mark.parametrize('alg, expected', [
    (textdistance.Jaccard, 1.0 / 3),
    (textdistance.Sorensen, .5),
    (textdistance.Tversky, 1.0 / 3),
    (textdistance.Overlap, .5),
    (textdistance.Cosine, .5),
])
def test_zero_counts_with_partial_overlap(alg, expected):
    left = Counter(a=1, b=2, x=0)
    right = Counter(b=3, c=1, y=0)
    assert isclose(alg(as_set=True, external=False)(left, right), expected)


@pytest.mark.parametrize('alg, expected', [
    (textdistance.Jaccard, .5),
    (textdistance.Sorensen, 2.0 / 3),
    (textdistance.Tversky, .5),
    (textdistance.Overlap, 1),
    (textdistance.Cosine, 1.0 / 2 ** .5),
])
def test_zero_counts_preserve_bag_weights(alg, expected):
    left = Counter(a=1, b=0)
    right = Counter(a=2, c=0)
    assert isclose(alg(external=False)(left, right), expected)


def test_tanimoto_zero_counts_as_set():
    alg = textdistance.Tanimoto(as_set=True, external=False)
    assert alg(Counter(a=1, b=0), Counter(a=2, c=0)) == 0
    assert isclose(alg(Counter(a=1, b=1, x=0), Counter(b=1, c=1, y=0)), log(1.0 / 3, 2))
