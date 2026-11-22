# built-in
from collections import deque

# external
import pytest

# project
import textdistance
from textdistance.algorithms.base import libraries
from textdistance.libraries import prototype


ALG = textdistance.Hamming


@pytest.mark.parametrize('left, right, expected', [
    ('test', 'text', 1),
    ('test', 'tset', 2),
    ('test', 'qwe', 4),
    ('test', 'testit', 2),
    ('test', 'tesst', 2),
    ('test', 'tet', 2),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert actual == expected

    actual = ALG(external=True)(left, right)
    assert actual == expected


@pytest.mark.parametrize('external', [False, True])
@pytest.mark.parametrize('sequences, expected', [
    (('', 'abc'), 0),
    (('abc', ''), 0),
    (('abc', 'abd-more'), 1),
    (('abc', 'abd-more', 'ab'), 0),
    (([], [None]), 0),
    ((), 0),
    (('abc',), 0),
])
def test_truncate_compares_only_shared_positions(sequences, expected, external):
    assert ALG(truncate=True, external=external)(*sequences) == expected


@pytest.mark.parametrize('external', [False, True])
@pytest.mark.parametrize('sequences, expected', [
    (([1, None], [1]), 1),
    (([1], [1, None]), 1),
    (([1, None], [1], [1, None, None]), 2),
    (([None], [None]), 0),
    (([None], [0]), 1),
])
def test_missing_positions_are_distinct_from_none(sequences, expected, external):
    assert ALG(external=external)(*sequences) == expected


def test_custom_comparison_does_not_receive_padding():
    distance = ALG(test_func=lambda a, b: a.lower() == b.lower(), external=False)
    assert distance(['A', 'B'], ['a']) == 1


@pytest.mark.parametrize('qval, left, right, expected', [
    (None, '', 'one two', 0),
    (None, 'one two', 'one three four', 1),
    (2, 'a', 'abc', 0),
    (2, 'abc', 'abdf', 1),
])
def test_truncate_prepared_sequences(qval, left, right, expected):
    assert ALG(qval=qval, truncate=True)(left, right) == expected


@pytest.mark.external
@pytest.mark.parametrize('lib', prototype.get_libs('Hamming'), ids=str)
def test_truncate_with_each_external_library(lib, monkeypatch):
    if lib.get_function() is None:
        pytest.skip(f'{lib} is not installed')
    monkeypatch.setitem(libraries.libs, 'Hamming', [lib])
    distance = ALG(truncate=True)
    assert distance('abc', 'abd-extra') == 1
    assert distance('abc-extra', 'abd') == 1
    assert distance('', 'abc') == 0
    assert distance('abc', 'abd') == 1


@pytest.mark.parametrize('external', [False, True])
@pytest.mark.parametrize('sequences, expected', [
    ((deque('abc'), deque('abd')), 1),
    ((deque('abc'), deque('abd-extra')), 1),
    ((deque('abc-extra'), deque('abd')), 1),
    ((deque('abc'),), 0),
    ((deque(), deque('abc')), 0),
])
def test_truncate_sequences_without_slicing(sequences, expected, external):
    assert ALG(truncate=True, external=external)(*sequences) == expected
