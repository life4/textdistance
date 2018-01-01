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


class MatrixTest(unittest.TestCase):
    def test_common(self):
        # https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
        nw_matrix = {
            ('A', 'A'): 10,
            ('G', 'G'): 7,
            ('C', 'C'): 9,
            ('T', 'T'): 8,
            ('A', 'G'): -1,
            ('A', 'C'): -3,
            ('A', 'T'): -4,
            ('G', 'C'): -5,
            ('G', 'T'): -3,
            ('C', 'T'): 0,
        }
        alg = textdistance.Matrix(nw_matrix, symmetric=True)
        self.assertEqual(alg('', ''), 1)
        self.assertEqual(alg('', 'a'), 0)
        self.assertEqual(alg('abcd', 'abcd'), 1)
        self.assertEqual(alg('A', 'C'), -3)
        self.assertEqual(alg('G', 'G'), 7)
        self.assertEqual(alg('A', 'A'), 10)
        self.assertEqual(alg('T', 'A'), -4)
        self.assertEqual(alg('T', 'C'), 0)
        self.assertEqual(alg('A', 'G'), -1)
        self.assertEqual(alg('C', 'T'), 0)


class NeedlemanWunschTest(unittest.TestCase):
    alg = textdistance.NeedlemanWunsch

    def test_common(self):
        # https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
        nw_matrix = {
            ('A', 'A'): 10,
            ('G', 'G'): 7,
            ('C', 'C'): 9,
            ('T', 'T'): 8,
            ('A', 'G'): -1,
            ('A', 'C'): -3,
            ('A', 'T'): -4,
            ('G', 'C'): -5,
            ('G', 'T'): -3,
            ('C', 'T'): 0,
        }
        sim_matrix = textdistance.Matrix(nw_matrix, symmetric=True)
        alg = self.alg(gap_cost=5, sim_func=sim_matrix)
        self.assertEqual(alg('AGACTAGTTAC', 'CGAGACGT'), 16)

        sim_ident = lambda x, y: 2 * int(x == y) - 1
        alg = self.alg(sim_func=sim_ident)
        self.assertEqual(alg('GATTACA', 'GCATGCU'), 0)
        alg = self.alg(gap_cost=5, sim_func=sim_ident)
        self.assertEqual(alg('CGATATCAG', 'TGACGSTGC'), -5)
        self.assertEqual(alg('AGACTAGTTAC', 'TGACGSTGC'), -7)
        self.assertEqual(alg('AGACTAGTTAC', 'CGAGACGT'), -15)


class SmithWatermanTest(unittest.TestCase):
    alg = textdistance.SmithWaterman

    def test_common(self):
        # https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
        nw_matrix = {
            ('A', 'A'): 10,
            ('G', 'G'): 7,
            ('C', 'C'): 9,
            ('T', 'T'): 8,
            ('A', 'G'): -1,
            ('A', 'C'): -3,
            ('A', 'T'): -4,
            ('G', 'C'): -5,
            ('G', 'T'): -3,
            ('C', 'T'): 0,
        }
        sim_matrix = textdistance.Matrix(nw_matrix, symmetric=True)
        alg = self.alg(gap_cost=5, sim_func=sim_matrix)
        self.assertEqual(alg('AGACTAGTTAC', 'CGAGACGT'), 26)

        sim_ident = lambda x, y: 2 * int(x == y) - 1
        alg = self.alg(sim_func=sim_ident)
        self.assertEqual(alg('GATTACA', 'GCATGCU'), 0)
        alg = self.alg(gap_cost=5, sim_func=sim_ident)
        self.assertEqual(alg('CGATATCAG', 'TGACGSTGC'), 0)
        self.assertEqual(alg('AGACTAGTTAC', 'TGACGSTGC'), 1)
        self.assertEqual(alg('AGACTAGTTAC', 'CGAGACGT'), 0)


class GotohTest(unittest.TestCase):
    alg = textdistance.Gotoh

    def test_common(self):
        # https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
        nw_matrix = {
            ('A', 'A'): 10,
            ('G', 'G'): 7,
            ('C', 'C'): 9,
            ('T', 'T'): 8,
            ('A', 'G'): -1,
            ('A', 'C'): -3,
            ('A', 'T'): -4,
            ('G', 'C'): -5,
            ('G', 'T'): -3,
            ('C', 'T'): 0,
        }
        sim_matrix = textdistance.Matrix(nw_matrix, symmetric=True)
        alg = self.alg(sim_func=sim_matrix)
        #self.assertEqual(alg('AGACTAGTTAC', 'CGAGACGT'), 26)

        sim_ident = lambda x, y: 2 * int(x == y) - 1
        alg = self.alg(gap_open=1, gap_ext=1, sim_func=sim_ident)
        self.assertEqual(alg('GATTACA', 'GCATGCU'), 0)
        alg = self.alg(gap_open=1, gap_ext=.5, sim_func=sim_ident)
        self.assertEqual(alg('GATTACA', 'GCATGCU'), 0)
        self.assertEqual(alg('AGACTAGTTAC', 'TGACGSTGC'), 1.5)
        self.assertEqual(alg('AGACTAGTTAC', 'CGAGACGT'), 1)
        alg = self.alg(gap_open=5, gap_ext=5, sim_func=sim_ident)
        self.assertEqual(alg('AGACTAGTTAC', 'CGAGACGT'), -15)


class StrCmp95Test(unittest.TestCase):
    alg = textdistance.strcmp95

    def test_common(self):
        self.assertAlmostEqual(self.alg('MARTHA', 'MARHTA'), 0.96111111)
        self.assertAlmostEqual(self.alg('DWAYNE', 'DUANE'), 0.873)
        self.assertAlmostEqual(self.alg('DIXON', 'DICKSONX'), 0.839333333)
        self.assertAlmostEqual(self.alg('TEST', 'TEXT'), 0.90666666)
