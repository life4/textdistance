# external
import pytest

# project
import textdistance


ALG = textdistance.Levenshtein


@pytest.mark.parametrize('left, right, expected', [
    ('test', 'text', 1),
    ('test', 'tset', 2),
    ('test', 'qwe', 4),
    ('test', 'testit', 2),
    ('test', 'tesst', 1),
    ('test', 'tet', 1),
])
def test_distance(left, right, expected):
    actual = ALG(external=False)(left, right)
    assert actual == expected

    actual = ALG(external=True)(left, right)
    assert actual == expected


def test_similarity_with_qval_greater_than_one():
    # `maximum()` used to measure the raw sequences while `distance()` compares
    # q-grams, so every normalized result was wrong by qval - 1 for qval > 1.

    # No shared characters: similarity 0 and normalized_distance 1.0, any qval.
    left = 'abcdefghij'
    right = 'jihgfedcba'
    alg = ALG(qval=2, external=False)
    assert alg.similarity(left, right) == 0
    assert alg.normalized_distance(left, right) == 1.0
    assert alg.normalized_similarity(left, right) == 0.0

    # Identical strings: normalized_similarity 1.0 regardless of qval.
    alg = ALG(qval=3, external=False)
    assert alg.normalized_distance(left, left) == 0.0
    assert alg.normalized_similarity(left, left) == 1.0
