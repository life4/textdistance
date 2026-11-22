# built-in
from fractions import Fraction
from math import isclose

# external
import pytest

# project
import textdistance


ALG = textdistance.arith_ncd


@pytest.mark.parametrize('left, right, expected', [
    ('test', 'test', 1),
    ('test', 'nani', 2.1666666666666665),
])
def test_similarity(left, right, expected):
    actual = ALG(left, right)
    assert isclose(actual, expected)


def test_make_probs():
    alg = textdistance.ArithNCD(terminator='\x00')
    probs = alg._make_probs('lol', 'lal')
    assert probs['l'] == (Fraction(0, 1), Fraction(4, 7))
    assert probs['o'][1] == Fraction(1, 7)
    assert probs['a'][1] == Fraction(1, 7)


def test_arith_output():
    alg = textdistance.ArithNCD(terminator='\x00')
    fraction = alg._compress('BANANA')
    assert fraction.numerator == 1525


@pytest.mark.parametrize('qval, left, right', [
    (None, 'one two', 'one three'),
    (2, 'abc', 'abd'),
    (2, [1, 2, 3], [1, 2, 4]),
])
def test_prepared_token_distance(qval, left, right):
    # Each input contains two distinct tokens with one token in common.
    # Their encoded sizes are 2, and either concatenation has size 6.
    alg = textdistance.ArithNCD(qval=qval)
    assert alg(left, right) == 2
    assert alg(right, left) == 2


@pytest.mark.parametrize('qval, left, right', [
    (None, '', 'one'),
    (2, 'a', 'ab'),
])
def test_empty_prepared_tokens(qval, left, right):
    assert textdistance.ArithNCD(qval=qval)(left, right) == 0


@pytest.mark.parametrize('left, right, expected', [
    ('ab', 'ac', 2),
    ('abc', 'abd', 3.5),
    ('abca', 'abda', 4 / 3),
    ('', '', 0),
])
def test_character_distances_unchanged(left, right, expected):
    assert textdistance.ArithNCD()(left, right) == expected


@pytest.mark.parametrize('qval, terminator, left, right, expected', [
    (None, '#', 'one two', 'one three', 2.5),
    (2, '#', 'abc', 'abd', 2.5),
    (None, '#', 'one # two', 'one # three', 1.25),
    (None, 'END', 'one two', 'one three', 2.5),
    (2, 'END', 'abc', 'abd', 2.5),
])
def test_prepared_token_terminator(qval, terminator, left, right, expected):
    alg = textdistance.ArithNCD(qval=qval, terminator=terminator)
    assert alg(left, right) == expected
    assert alg(right, left) == expected
