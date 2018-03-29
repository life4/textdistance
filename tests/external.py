from __future__ import unicode_literals
from __main__ import unittest, textdistance


class ExternalTest(unittest.TestCase):
    test_cases = (
        ('test', 'test'),
        ('test', 'text'),
        ('test', 'testit'),
        ('qwer', 'asdf'),
    )

    def test_common(self):
        libs = textdistance.libraries.libraries
        for alg in libs.get_algorithms():
            for lib in libs.get_libs(alg):
                external_func = lib.get_function()

                conditions = lib.conditions or {}
                internal_func = getattr(textdistance, alg)(external=False, **conditions)

                for s1, s2 in self.test_cases:
                    with self.subTest(alg=alg, lib=lib.module_name, s1=s1, s2=s2):
                        self.assertAlmostEqual(internal_func(s1, s2), external_func(s1, s2))
