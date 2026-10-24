# built-in
from difflib import SequenceMatcher

# external
import pytest

# project
from textdistance import RatcliffObershelp


@pytest.mark.parametrize('sequences,qval,expected', [
    (('one two three', 'one two four'), None, 2 / 3),
    (('one two', 'one  two'), None, 1),
    (('one', '   '), None, 0),
    ((' ', '\t'), None, 1),
    (('abX', 'abY'), 2, 1 / 2),
    (('ab', 'ac'), 3, 1),
    (('ab', 'abc'), 3, 0),
    (([1, 2, 3], [1, 2, 4]), 1, 2 / 3),
    (((1, 2, 3), (1, 2, 4)), 1, 2 / 3),
    (([1, 2, 3], [1, 2, 4], [1, 2, 5]), 1, 2 / 3),
    (([[1], [2], [3]], [[1], [2], [4]]), 1, 2 / 3),
    (((1, 2, 3), [1, 2, 4]), 1, 2 / 3),
    (('a b c', 'a b d', 'a b e'), None, 2 / 3),
    (('abX', 'abY', 'abZ'), 2, 1 / 2),
    ((b'abc', b'abd'), 1, 2 / 3),
    ((b'abc', b'abd', b'abe'), 1, 2 / 3),
    (('prefix-middle-suffix', 'prefix-other-suffix'), 1, 10 / 13),
])
def test_prepared_sequences(sequences, qval, expected):
    algorithm = RatcliffObershelp(qval=qval, external=False)
    assert algorithm(*sequences) == pytest.approx(expected)
    assert algorithm.normalized_similarity(*sequences) == pytest.approx(expected)
    assert algorithm.distance(*sequences) == pytest.approx(1 - expected)
    assert algorithm.normalized_distance(*sequences) == pytest.approx(1 - expected)


@pytest.mark.parametrize('left,right', [
    ('tide', 'diet'),
    ('aabab', 'baaa'),
    ('aabba', 'abaa'),
    ('abXYab', 'XYabZZ'),
    ('abc', 'xyz'),
    ('', ''),
    ('a' * 210 + 'X', 'a' * 210 + 'Y'),
    (b'tide', b'diet'),
])
def test_default_string_matching(left, right):
    expected = SequenceMatcher(None, left, right, autojunk=False).ratio()
    assert RatcliffObershelp(external=False)(left, right) == expected


@pytest.mark.parametrize('left,right', [('aabab', 'baaa'), ('aabba', 'abaa')])
@pytest.mark.parametrize('container', [list, tuple])
def test_generic_tie_breaking(left, right, container):
    expected = SequenceMatcher(None, left, right, autojunk=False).ratio()
    assert RatcliffObershelp(external=False)(container(left), container(right)) == expected
