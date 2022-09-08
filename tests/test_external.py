# built-in
from math import isclose

# external
import hypothesis
import pytest

# project
import textdistance
from textdistance.libraries import prototype


libraries = prototype.clone()

# numpy throws a bunch of warning about abydos using `np.int` isntead of `int`.
ABYDOS_WARNINGS = (
    'ignore:`np.int` is a deprecated alias',
    'ignore:`np.float` is a deprecated alias',
    'ignore:Using or importing the ABCs',
)


@pytest.mark.filterwarnings(*ABYDOS_WARNINGS)
@pytest.mark.external
@pytest.mark.parametrize('alg', libraries.get_algorithms())
@hypothesis.settings(deadline=None)
@hypothesis.given(
    left=hypothesis.strategies.text(min_size=1),
    right=hypothesis.strategies.text(min_size=1),
)
def test_compare(left, right, alg):
    for lib in libraries.get_libs(alg):
        conditions = lib.conditions or {}
        internal_func = getattr(textdistance, alg)(external=False, **conditions)
        external_func = lib.get_function()
        if external_func is None:
            raise RuntimeError('cannot import {}'.format(str(lib)))

        if not lib.check_conditions(internal_func, left, right):
            continue

        int_result = internal_func(left, right)
        s1, s2 = lib.prepare(left, right)
        ext_result = external_func(s1, s2)
        assert isclose(int_result, ext_result), str(lib)


@pytest.mark.filterwarnings(*ABYDOS_WARNINGS)
@pytest.mark.external
@pytest.mark.parametrize('alg', libraries.get_algorithms())
@hypothesis.given(
    left=hypothesis.strategies.text(min_size=1),
    right=hypothesis.strategies.text(min_size=1),
)
@pytest.mark.parametrize('qval', (None, 1, 2, 3))
def test_qval(left, right, alg, qval):
    for lib in libraries.get_libs(alg):
        conditions = lib.conditions or {}
        internal_func = getattr(textdistance, alg)(external=False, **conditions)
        external_func = lib.get_function()
        if external_func is None:
            raise RuntimeError('cannot import {}'.format(str(lib)))
        # algorithm doesn't support q-grams
        if not hasattr(internal_func, 'qval'):
            continue

        internal_func.qval = qval
        # if qval unsopporting already set for lib
        s1, s2 = internal_func._get_sequences(left, right)
        if not lib.check_conditions(internal_func, s1, s2):
            continue
        quick_answer = internal_func.quick_answer(s1, s2)
        if quick_answer is not None:
            continue

        # test
        int_result = internal_func(left, right)
        s1, s2 = lib.prepare(s1, s2)
        ext_result = external_func(s1, s2)
        assert isclose(int_result, ext_result), f'{lib}({repr(s1)}, {repr(s2)})'


@pytest.mark.filterwarnings(*ABYDOS_WARNINGS)
@pytest.mark.external
@pytest.mark.parametrize('alg', libraries.get_algorithms())
@hypothesis.given(
    left=hypothesis.strategies.lists(hypothesis.strategies.integers()),
    right=hypothesis.strategies.lists(hypothesis.strategies.integers()),
)
def test_list_of_numbers(left, right, alg):
    for lib in libraries.get_libs(alg):
        conditions = lib.conditions or {}
        internal_func = getattr(textdistance, alg)(external=False, **conditions)
        external_func = lib.get_function()
        if external_func is None:
            raise RuntimeError('cannot import {}'.format(str(lib)))

        quick_answer = internal_func.quick_answer(left, right)
        if quick_answer is not None:
            continue
        if not lib.check_conditions(internal_func, left, right):
            continue

        int_result = internal_func(left, right)
        s1, s2 = lib.prepare(left, right)
        ext_result = external_func(s1, s2)
        assert isclose(int_result, ext_result), f'{lib}({repr(s1)}, {repr(s2)})'
