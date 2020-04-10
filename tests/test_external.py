from math import isclose

import hypothesis
import pytest

import textdistance
from textdistance.libraries import prototype


libraries = prototype.clone()


@pytest.mark.external
@pytest.mark.parametrize('alg', libraries.get_algorithms())
@hypothesis.given(
    left=hypothesis.strategies.text(),
    right=hypothesis.strategies.text(),
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
