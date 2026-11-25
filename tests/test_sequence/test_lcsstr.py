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


@pytest.mark.parametrize('sequences, expected', [
    ([b'abcd', b'xbcx', b'ybcz'], b'bc'),
    ([[0, 1, 2, 3], [4, 1, 2, 5], [1, 2]], [1, 2]),
    ([(0, 1, 2, 3), (4, 1, 2, 5), (1, 2)], (1, 2)),
    ([['lead', 'red', 'blue'], ['red', 'blue', 'tail'], ['red', 'blue']], ['red', 'blue']),
    ([['ab', 'c'], ['a', 'bc'], ['ab', 'c']], []),
    ([[[0], [1], [2]], [[1], [2]], [[1], [2], [3]]], [[1], [2]]),
    ([[1, 2, 3], (0, 1, 2), [1, 2]], [1, 2]),
    ([b'abc', b'def', b'ghi'], b''),
    ([(1, 2), (3, 4), (5, 6)], ()),
    ([b'x' * 200 + b'ab', b'zab'], b'ab'),
    ([[0] * 200 + [1, 2], [3, 1, 2]], [1, 2]),
    ([(0,) * 200 + (1, 2), (3, 1, 2)], (1, 2)),
])
def test_fallback_sequence_elements(sequences, expected):
    algorithm = ALG(external=False)
    assert algorithm(*sequences) == expected
    assert type(algorithm(*sequences)) is type(expected)
    assert algorithm.similarity(*sequences) == len(expected)


@pytest.mark.parametrize('qval, sequences, expected', [
    (None, ['a red blue z', 'red blue x', 'y red blue'], ['red', 'blue']),
    (None, ['filler ' * 200 + 'red blue', 'red blue'], ['red', 'blue']),
    (2, ['abcd', 'xbcx', 'ybcz'], [('b', 'c')]),
    (2, ['x' * 200 + 'abc', 'yabc'], [('a', 'b'), ('b', 'c')]),
])
def test_fallback_prepared_tokens(qval, sequences, expected):
    algorithm = ALG(qval=qval, external=False)
    assert algorithm(*sequences) == expected
    assert algorithm.similarity(*sequences) == len(expected)
