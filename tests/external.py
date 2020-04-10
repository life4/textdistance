from __future__ import unicode_literals

# project
from __main__ import libraries, textdistance, unittest


class ExternalTest(unittest.TestCase):
    test_cases = (
        ('test', 'test'),
        ('test', 'text'),
        ('test', 'testit'),
        ('qwer', 'asdf'),
    )

    def test_qval(self):
        for alg in libraries.get_algorithms():
            for lib in libraries.get_libs(alg):
                conditions = lib.conditions or {}
                internal_func = getattr(textdistance, alg)(external=False, **conditions)
                external_func = lib.get_function()
                # algorithm doesn't support q-grams
                if not hasattr(internal_func, 'qval'):
                    continue
                for qval in (None, 1, 2, 3):
                    for s1, s2 in self.test_cases:
                        internal_func.qval = qval
                        # if qval unsopporting already set for lib
                        if not lib.check_conditions(internal_func, s1, s2):
                            continue
                        # test
                        with self.subTest(alg=alg, lib=lib.module_name, s1=s1, s2=s2, qval=qval):
                            int_result = internal_func(s1, s2)
                            s1, s2 = internal_func._get_sequences(s1, s2)
                            s1, s2 = lib.prepare(s1, s2)
                            ext_result = external_func(s1, s2)
                            self.assertAlmostEqual(int_result, ext_result)
