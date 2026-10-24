# external
import pytest

# project
import textdistance


ALG = textdistance.LCSStr


@pytest.mark.parametrize('left, right, expected', [
    # prefix
    ('ab', 'abcd', 'ab'),
    ('abcd', 'ab', 'ab'),

    # middle
    ('abcd', 'bc', 'bc'),
    ('bc', 'abcd', 'bc'),

    # suffix
    ('abcd', 'cd', 'cd'),
    ('abcd', 'cd', 'cd'),

    # no
    ('abcd', 'ef', ''),
    ('ef', 'abcd', ''),

    # long
    # https://github.com/life4/textdistance/issues/40
    ('MYTEST' * 100, 'TEST', 'TEST'),
    ('TEST', 'MYTEST' * 100, 'TEST'),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert actual == expected

    actual = ALG(external=True)(left, right)
    assert actual == expected


@pytest.mark.parametrize('sequences, qval, expected', [
    ((b'abc', b'xbc', b'ybc'), 1, b'bc'),
    (([1, 2, 3], [0, 2, 3], [4, 2, 3]), 1, [2, 3]),
    (((1, 2, 3), (0, 2, 3), (4, 2, 3)), 1, (2, 3)),
    (([[1], [2]], [[0], [2]], [[3], [2]]), 1, [[2]]),
    (('red blue', 'blue green', 'blue yellow'), None, ['blue']),
    (('abab', 'baba', 'abaca'), 2, [('a', 'b'), ('b', 'a')]),
    ((b'x' * 197 + b'bc', b'bc'), 1, b'bc'),
    ((b'x' * 198 + b'bc', b'bc'), 1, b'bc'),
    ((b'x' * 200 + b'bc', b'bc'), 1, b'bc'),
    (([0] * 200 + [2, 3], [2, 3]), 1, [2, 3]),
    (((0,) * 200 + (2, 3), (2, 3)), 1, (2, 3)),
    ((['x'] * 200 + ['blue'], ['blue']), 1, ['blue']),
    (('red blue', 'blue green', 'yellow orange'), None, []),
    (([1, 2], [3, 4], [5, 6]), 1, []),
    ((b'abc', b'def', b'ghi'), 1, b''),
    ((('a', 'b'), ('ab',), ('ab',)), 1, ()),
    (([1, 2, 3], (0, 2, 3), [4, 2, 3]), 1, [2, 3]),
    (('abc', ['x', 'b', 'c'], ('y', 'b', 'c')), 1, 'bc'),
    ((b'abc', [0, 98, 99], (1, 98, 99)), 1, b'bc'),
])
def test_prepared_subsequences(sequences, qval, expected):
    alg = ALG(qval=qval)
    actual = alg(*sequences)
    assert actual == expected
    assert type(actual) is type(expected)
    assert alg.similarity(*sequences) == len(expected)


def test_three_strings():
    assert ALG()('abcde', 'xbcdy', 'zbcdw') == 'bcd'
