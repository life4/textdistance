# external
import pytest

# project
import textdistance


ALG = textdistance.LCSSeq


@pytest.mark.parametrize('left, right, expected', [
    ('ab', 'cd', ''),
    ('abcd', 'abcd', 'abcd'),

    ('test', 'text', 'tet'),
    ('thisisatest', 'testing123testing', 'tsitest'),
    ('DIXON', 'DICKSONX', 'DION'),
    ('random exponential', 'layer activation', 'ratia'),

    ('a' * 80, 'a' * 80, 'a' * 80),
    ('a' * 80, 'b' * 80, ''),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert actual == expected

    actual = ALG(external=True)(left, right)
    assert actual == expected


@pytest.mark.parametrize('seqs, expected', [
    (('a', 'b', 'c'), ''),
    (('a', 'a', 'a'), 'a'),
    (('test', 'text', 'tempest'), 'tet'),
])
def test_distance_multiseq(seqs, expected):
    actual = ALG(external=False)(*seqs)
    assert actual == expected

    actual = ALG(external=True)(*seqs)
    assert actual == expected


@pytest.mark.parametrize('left, right, expected', [
    (b'abcd', b'axcd', b'acd'),
    ([1, 2, 3], [1, 4, 3], [1, 3]),
    ((1, 2, 3), (1, 4, 3), (1, 3)),
])
def test_sequence_type(left, right, expected):
    assert ALG(external=False)(left, right) == expected


@pytest.mark.parametrize('sequences, qval, expected', [
    (('red blue green', 'red black green'), None, ['red', 'green']),
    (('abcd', 'abxd'), 2, [('a', 'b')]),
    (('red blue green', 'red black green', 'red green'), None, ['red', 'green']),
    (('abcd', 'abxd', 'abyd'), 2, [('a', 'b')]),
])
def test_prepared_sequences(sequences, qval, expected):
    assert ALG(qval=qval, external=False)(*sequences) == expected


def test_custom_match_function():
    alg = ALG(test_func=lambda a, b: a.lower() == b.lower(), external=False)
    assert alg('AbC', 'axc') == 'AC'
