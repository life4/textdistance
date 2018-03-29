from importlib import import_module
from __main__ import unittest, textdistance


class ExternalTest(unittest.TestCase):
    test_cases = (
        ('test', 'test'),
        ('test', 'text'),
        ('test', 'testit'),
        ('qwer', 'asdf'),
    )

    def test_common(self):
        for alg, paths in textdistance.libraries.LIBRARIES.items():
            for path in paths:
                module_name, _, func_name = path.rpartition('.')
                module = import_module(module_name)
                external_func = getattr(module, func_name)
                internal_func = getattr(textdistance, alg)(external=False)

                for s1, s2 in self.test_cases:
                    with self.subTest(alg=alg, lib=path, s1=s1, s2=s2):
                        self.assertEqual(internal_func(s1, s2), external_func(s1, s2))


# Tversky.as_set=True
