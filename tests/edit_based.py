from __main__ import unittest, textdistance

class HammingTest(unittest.TestCase):
    alg = textdistance.hamming

    def test_common(self):
        self.assertEqual(self.alg.distance('test', 'text'), 1)
        self.assertEqual(self.alg.distance('test', 'tset'), 2)
        self.assertEqual(self.alg.distance('test', 'qwe'), 4)
        self.assertEqual(self.alg.distance('test', 'testit'), 2)
        self.assertEqual(self.alg.distance('test', 'tesst'), 2)
        self.assertEqual(self.alg.distance('test', 'tet'), 2)


class LevenshteinTest(unittest.TestCase):
    alg = textdistance.levenshtein

    def test_common(self):
        self.assertEqual(self.alg.distance('test', 'text'), 1)
        self.assertEqual(self.alg.distance('test', 'tset'), 2)
        self.assertEqual(self.alg.distance('test', 'qwe'), 4)
        self.assertEqual(self.alg.distance('test', 'testit'), 2)
        self.assertEqual(self.alg.distance('test', 'tesst'), 1)
        self.assertEqual(self.alg.distance('test', 'tet'), 1)


class DamerauLevenshteinTest(unittest.TestCase):
    alg = textdistance.damerau_levenshtein

    def test_common(self):
        self.assertEqual(self.alg.distance('test', 'text'), 1)
        self.assertEqual(self.alg.distance('test', 'tset'), 1)
        self.assertEqual(self.alg.distance('test', 'qwe'), 4)
        self.assertEqual(self.alg.distance('test', 'testit'), 2)
        self.assertEqual(self.alg.distance('test', 'tesst'), 1)
        self.assertEqual(self.alg.distance('test', 'tet'), 1)


class JaroTest(unittest.TestCase):
    alg = textdistance.jaro

    def test_common(self):
        self.assertGreater(self.alg.similarity('hello', 'haloa'), 0.733)
        self.assertLess(self.alg.similarity('hello', 'haloa'), 0.734)
        self.assertEqual(self.alg.similarity('fly', 'ant'), 0.0)
        self.assertGreater(self.alg.similarity('frog', 'fog'), 0.916)
        self.assertLess(self.alg.similarity('frog', 'fog'), 0.917)
        self.assertGreater(self.alg.similarity('ATCG', 'TAGC'), 0.833)
        self.assertLess(self.alg.similarity('ATCG', 'TAGC'), 0.834)


class JaroWinklerTest(unittest.TestCase):
    alg = textdistance.jaro_winkler

    def test_common(self):
        self.assertGreater(self.alg.similarity('elephant', 'hippo'), 0.441)
        self.assertLess(self.alg.similarity('elephant', 'hippo'), 0.442)
        self.assertEqual(self.alg.similarity('fly', 'ant'), 0.0)
        self.assertGreater(self.alg.similarity('frog', 'fog'), 0.916)
        self.assertLess(self.alg.similarity('frog', 'fog'), 0.917)
