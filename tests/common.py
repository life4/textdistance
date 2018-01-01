from __main__ import unittest, textdistance


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
    textdistance.mlipns,
    textdistance.editex,

    textdistance.lcsseq,
    textdistance.lcsstr,
    textdistance.ratcliff_obershelp,

    textdistance.jaccard,
    textdistance.sorensen,
    textdistance.tversky,
    textdistance.overlap,
    textdistance.cosine,
    textdistance.strcmp95,
    textdistance.monge_elkan,

    textdistance.mra,

    textdistance.prefix,
    textdistance.postfix,
    textdistance.identity,
#    textdistance.length,

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
            with self.subTest(algorithm=alg.__class__.__name__, func=alg):
                d = alg.distance('test me', 'test me')
                self.assertEqual(d, 0)

    def test_different_similarity(self):
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__, func=alg):
                s = alg.similarity('spam', 'qwer')
                self.assertEqual(s, 0)

class EmptyTest(unittest.TestCase):
    def test_equal_distance(self):
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__, func=alg):
                d = alg.distance('', '')
                self.assertEqual(d, 0)


class NormalizationTest(unittest.TestCase):
    def test_similar_similarity(self):
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__, func=alg):
                d = alg.normalized_similarity('test me', 'test me')
                self.assertEqual(d, 1)

    def test_different_distance(self):
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__, func=alg):
                s = alg.normalized_distance('spam', 'qwer')
                self.assertEqual(s, 1)

class CompareTest(unittest.TestCase):
    def test_absolute(self):
        for alg in algos:
            alg_name = alg.__class__.__name__

            with self.subTest(algorithm=alg_name, func=alg):
                d = alg.distance('test', 'text')
                s = alg.similarity('test', 'text')
                self.assertGreaterEqual(d, 0)
            with self.subTest(algorithm=alg_name, func=alg):
                d = alg.distance('test', 'bulk')
                s = alg.similarity('test', 'bulk')
                self.assertGreaterEqual(d, s)

    def test_normalized(self):
        for alg in algos:
            alg_name = alg.__class__.__name__
            with self.subTest(algorithm=alg_name, func=alg):
                d = alg.normalized_distance('test', 'text')
                s = alg.normalized_similarity('test', 'text')
                self.assertGreaterEqual(d, 0)
                self.assertLessEqual(d, 1)
                self.assertGreaterEqual(s, 0)
                self.assertLessEqual(s, 1)
            with self.subTest(algorithm=alg_name, func=alg):
                d = alg.normalized_distance('test', 'bulk')
                s = alg.normalized_similarity('test', 'bulk')
                self.assertGreaterEqual(d, s)
