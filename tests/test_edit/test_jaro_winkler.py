# built-in
from math import isclose

# external
import pytest

# project
import textdistance
from textdistance.algorithms.base import libraries
from textdistance.libraries import prototype


ALG = textdistance.JaroWinkler


@pytest.mark.parametrize('left, right, expected', [
    ('elephant', 'hippo', 0.44166666666666665),
    ('fly', 'ant', 0.0),
    ('frog', 'fog', 0.925),
    ('MARTHA', 'MARHTA', 0.9611111111111111),
    ('DWAYNE', 'DUANE', 0.84),
    ('DIXON', 'DICKSONX', 0.8133333333333332),

    # https://github.com/life4/textdistance/issues/39
    ('duck donald', 'duck daisy', 0.867272727272),
])
def test_distance(left, right, expected):
    actual = ALG(winklerize=True, external=False)(left, right)
    assert isclose(actual, expected)

    actual = ALG(winklerize=True, external=True)(left, right)
    assert isclose(actual, expected)


@pytest.mark.parametrize('external', [False, True])
@pytest.mark.parametrize('prefix_weight, expected', [
    (0, 17 / 18),
    (0.1, 173 / 180),
    (0.2, 44 / 45),
])
def test_per_call_prefix_weight(prefix_weight, expected, external):
    similarity = ALG(external=external)
    assert similarity('martha', 'marhta', prefix_weight=prefix_weight) == pytest.approx(expected)
    # A customized call must not change the default for subsequent calls.
    assert similarity('martha', 'marhta') == pytest.approx(173 / 180)


@pytest.mark.parametrize('external', [False, True])
@pytest.mark.parametrize('left, right, expected', [
    ('', '', 1),
    ('', 'martha', 0),
    ('martha', 'martha', 1),
    ('abc', 'xyz', 0),
])
def test_nondefault_prefix_weight_boundaries(left, right, expected, external):
    assert ALG(external=external)(left, right, prefix_weight=0.2) == expected


@pytest.mark.external
@pytest.mark.parametrize('lib', prototype.get_libs('JaroWinkler'), ids=str)
@pytest.mark.parametrize('prefix_weight, expected', [(0, 17 / 18), (0.2, 44 / 45)])
def test_prefix_weight_with_each_external_library(lib, prefix_weight, expected, monkeypatch):
    if lib.get_function() is None:
        pytest.skip(f'{lib} is not installed')
    monkeypatch.setitem(libraries.libs, 'JaroWinkler', [lib])
    similarity = ALG()
    assert similarity('martha', 'marhta', prefix_weight=prefix_weight) == pytest.approx(expected)
    assert similarity('martha', 'marhta') == pytest.approx(173 / 180)


@pytest.mark.parametrize('external', [False, True])
@pytest.mark.parametrize('prefix_weight', [0, 0.2])
def test_identical_inputs_skip_matching(prefix_weight, external):
    class IdenticalText(str):
        def __getitem__(self, index):
            raise AssertionError('identical inputs must skip character matching')

    text = IdenticalText('a' * 6000)
    assert ALG(external=external)(text, text, prefix_weight=prefix_weight) == 1
