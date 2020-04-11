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
