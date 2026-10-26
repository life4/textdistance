# external
import pytest

# project
import textdistance


@pytest.mark.parametrize('algorithm, sequences, expected', [
    (textdistance.prefix, (b'prefix-old', b'prefix-new'), b'prefix-'),
    (textdistance.postfix, (b'old-suffix', b'new-suffix'), b'-suffix'),
    (textdistance.prefix, (b'abc', b'abd', b'axy'), b'a'),
    (textdistance.postfix, (b'abc', b'xbc', b'zyc'), b'c'),
    (textdistance.prefix, (b'\x00\x80\xff', b'\x00\x80\xfe'), b'\x00\x80'),
    (textdistance.postfix, (b'\x00\x80\xff', b'\x01\x80\xff'), b'\x80\xff'),
])
def test_byte_affixes(algorithm, sequences, expected):
    result = algorithm(*sequences)
    assert result == expected
    assert isinstance(result, bytes)
    assert algorithm.similarity(*sequences) == len(expected)


@pytest.mark.parametrize('algorithm', [textdistance.prefix, textdistance.postfix])
@pytest.mark.parametrize('sequences, expected', [
    ((b'abc', b'abc'), b'abc'),
    ((b'abc',), b'abc'),
    ((b'abc', b'xyz'), b''),
    ((b'abc', b''), b''),
    ((b'', b''), b''),
])
def test_byte_affix_boundaries(algorithm, sequences, expected):
    result = algorithm(*sequences)
    assert result == expected
    assert isinstance(result, bytes)
