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
