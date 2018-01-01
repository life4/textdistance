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
        self.assertAlmostEqual(self.alg.similarity('hello', 'haloa'), 0.73333333)
        self.assertEqual(self.alg.similarity('fly', 'ant'), 0.0)
        self.assertAlmostEqual(self.alg.similarity('frog', 'fog'), 0.91666666)
        self.assertAlmostEqual(self.alg.similarity('ATCG', 'TAGC'), 0.83333333)
        self.assertAlmostEqual(self.alg.similarity('MARTHA', 'MARHTA'), 0.944444444)
        self.assertAlmostEqual(self.alg.similarity('DWAYNE', 'DUANE'), 0.822222222)
        self.assertAlmostEqual(self.alg.similarity('DIXON', 'DICKSONX'), 0.76666666)


class JaroWinklerTest(unittest.TestCase):
    alg = textdistance.jaro_winkler

    def test_common(self):
        self.assertAlmostEqual(self.alg.similarity('elephant', 'hippo'), 0.44166666)
        self.assertEqual(self.alg.similarity('fly', 'ant'), 0.0)
        self.assertAlmostEqual(self.alg.similarity('frog', 'fog'), 0.916666666)
        self.assertAlmostEqual(self.alg.similarity('MARTHA', 'MARHTA'), 0.96111111)
        self.assertAlmostEqual(self.alg.similarity('DWAYNE', 'DUANE'), 0.84)
        self.assertAlmostEqual(self.alg.similarity('DIXON', 'DICKSONX'), 0.81333333)
