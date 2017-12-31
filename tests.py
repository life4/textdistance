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

    textdistance.lcsseq,
    textdistance.lcsstr,
    textdistance.ratcliff_obershelp,

    textdistance.jaccard,
    textdistance.sorensen,
    textdistance.tversky,
    textdistance.overlap,
    textdistance.cosine,
    textdistance.strcmp95,

    textdistance.mra,

    textdistance.prefix,

#    textdistance.bz2_ncd,
#    textdistance.lzma_ncd,
#    textdistance.arith_ncd,
#    textdistance.rle_ncd,
#    textdistance.bwtrle_ncd,
#    textdistance.zlib_ncd,
]

class CommonTest(unittest.TestCase):
    def test_similar_distance(self):
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__):
                d = alg.distance('test me', 'test me')
                self.assertEqual(d, 0)

    def test_different_similarity(self):
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__):
                s = alg.similarity('spam', 'qwer')
                self.assertEqual(s, 0)


class NormalizationTest(unittest.TestCase):
    def test_similar_similarity(self):
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__):
                d = alg.normalized_similarity('test me', 'test me')
                self.assertEqual(d, 1)

    def test_different_distance(self):
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__):
                s = alg.normalized_distance('spam', 'qwer')
                self.assertEqual(s, 1)


if __name__ == '__main__':
    unittest.main()
