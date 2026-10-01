# built-in
from math import isclose

# external
import pytest

# project
import textdistance


ALG = textdistance.MongeElkan


@pytest.mark.parametrize('left, right, expected', [
    (['Niall'], ['Neal'], .805),
    (['Niall'], ['Nigel'], 0.7866666666666667),
])
def test_similarity(left, right, expected):
    actual = ALG(qval=1, algorithm=textdistance.jaro_winkler).similarity(left, right)
    assert isclose(actual, expected)


def test_two_tokens_average_the_best_match_once():
    jaro = textdistance.JaroWinkler(external=False)
    alg = ALG(qval=1, algorithm=jaro, external=False)
    expected = (
        max(jaro.similarity('Niall', 'Neal'), jaro.similarity('Niall', 'Jon'))
        + max(jaro.similarity('John', 'Neal'), jaro.similarity('John', 'Jon'))
    ) / 2
    assert alg.similarity(['Niall', 'John'], ['Neal', 'Jon']) == expected
