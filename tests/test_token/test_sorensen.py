# built-in
from math import isclose

# external
import hypothesis
import pytest

# project
import textdistance


ALG = textdistance.Sorensen


@pytest.mark.parametrize('left, right, expected', [
    ('test', 'text', 2.0 * 3 / 8),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert isclose(actual, expected)

    actual = ALG(external=True)(left, right)
    assert isclose(actual, expected)


@hypothesis.given(
    left=hypothesis.strategies.text(),
    right=hypothesis.strategies.text(),
)
def test_compare_with_tversky(left, right):
    td = textdistance.Tversky(ks=[.5, .5]).distance(left, right)
    jd = ALG().distance(left, right)
    assert isclose(jd, td)


@hypothesis.given(
    left=hypothesis.strategies.text(),
    right=hypothesis.strategies.text(),
)
def test_compare_with_tversky_as_set(left, right):
    td = textdistance.Tversky(ks=[.5, .5], as_set=True).distance(left, right)
    jd = ALG(as_set=True).distance(left, right)
    assert isclose(jd, td)


@pytest.mark.parametrize('sequences, options, expected', [
    (('ab', 'ba', 'ab'), {}, 1),
    (('abc', 'abd', 'abe'), {}, 2.0 / 3),
    (('aab', 'aba', 'baa', 'aab'), {}, 1),
    (('aaab', 'aabb', 'abbb'), {}, .5),
    (('aaab', 'aabb', 'abbb'), {'as_set': True}, 1),
    (('abab', 'baba', 'abab'), {'qval': 2}, 2.0 / 3),
    (('one two', 'two one', 'one two'), {'qval': None}, 1),
])
def test_multiple_sequences(sequences, options, expected):
    actual = ALG(external=False, **options)(*sequences)
    assert isclose(actual, expected)


@pytest.mark.parametrize('sequences, expected', [
    ((), 1),
    (('ab',), 1),
    (('ab', 'ab', 'ab'), 1),
    (('ab', '', 'ba'), 0),
    (('ab', 'bc'), .5),
])
def test_sequence_count_boundaries(sequences, expected):
    assert ALG(external=False)(*sequences) == expected
