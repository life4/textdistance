try:
    import unittest2 as unittest
except ImportError:
    import unittest
import textdistance


algos = [
    textdistance.bag,
    textdistance.hamming,
    textdistance.levenshtein,
    textdistance.damerau_levenshtein,
    textdistance.jaro,
    textdistance.jaro_winkler,
    textdistance.needleman_wunsch,
    textdistance.gotoh,
    textdistance.smith_waterman,
]

class CommonTest(unittest.TestCase):
    def test_similar_distance(self):
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__):
                d = alg.distance('test me', 'test me')
                self.assertEqual(d, 0)


if __name__ == '__main__':
    unittest.main()
