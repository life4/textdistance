# external
import pytest

# project
import textdistance


@pytest.mark.parametrize('qval, sequences, expected', [
    (None, ('one two three', 'zero two three'), ['two', 'three']),
    (2, ('abcd', 'xbcd'), [('b', 'c'), ('c', 'd')]),
    (2, ([1, 2, 3, 4], [0, 2, 3, 4]), [(2, 3), (3, 4)]),
    (None, ('one two', 'zero two', 'three two'), ['two']),
    (None, ('one two', 'three four'), []),
    (None, ('', 'one two'), []),
    (2, ('a', 'ba'), []),
    (1, ('abcd', 'xbcd'), 'bcd'),
    (1, ((1, 2, 3), (0, 2, 3)), [2, 3]),
])
def test_postfix_preserves_prepared_units(qval, sequences, expected):
    assert textdistance.Postfix(qval=qval)(*sequences) == expected


def test_postfix_word_comparator():
    def ignore_case(*words):
        return len({word.lower() for word in words}) == 1

    alg = textdistance.Postfix(qval=None, sim_test=ignore_case)
    assert alg('first TWO Three', 'other two three') == ['TWO', 'Three']


def test_postfix_no_sequences():
    assert textdistance.Postfix()() == ''
