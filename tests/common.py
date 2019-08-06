# project
from __main__ import NUMPY, textdistance, unittest


algos = [
    textdistance.bag,

    textdistance.hamming,
    textdistance.levenshtein,
    textdistance.damerau_levenshtein,
    textdistance.jaro,
    textdistance.jaro_winkler,
    textdistance.mlipns,

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
    # textdistance.length,
    #
    # textdistance.bz2_ncd,
    # textdistance.lzma_ncd,
    # textdistance.arith_ncd,
    # textdistance.rle_ncd,
    # textdistance.bwtrle_ncd,
    # textdistance.zlib_ncd,
]

if NUMPY:
    algos.extend([
        textdistance.gotoh,
        textdistance.needleman_wunsch,
        # textdistance.smith_waterman,
        # textdistance.editex,
    ])


CAN_BE_NEGATIVE = {'NeedlemanWunsch', 'Gotoh'}


class CommonTest(unittest.TestCase):
    def test_similar_distance(self):
        for alg in algos:
            if alg.__class__.__name__ in CAN_BE_NEGATIVE:
                continue
            with self.subTest(algorithm=alg.__class__.__name__, func=alg):
                d = alg.distance('test me', 'test me')
                self.assertEqual(d, 0)

    def test_different_similarity(self):
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__, func=alg):
                s = alg.similarity('spam', 'qwer')
                self.assertEqual(s, 0)


class CommonEmptyTest(unittest.TestCase):
    def test_equal_distance(self):
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__, func=alg):
                d = alg.distance('', '')
                self.assertEqual(d, 0)

    def test_unequal_distance(self):
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__, func=alg):
                if alg.maximum('', 'qwertyui'):
                    d = alg.distance('', 'qwertyui')
                    self.assertGreater(d, 0)


class CommonNormalizationTest(unittest.TestCase):
    def test_similar_similarity(self):
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__, func=alg):
                d = alg.normalized_similarity('test me', 'test me')
                self.assertEqual(d, 1)

    def test_different_distance(self):
        for alg in algos:
            if alg.__class__.__name__ in CAN_BE_NEGATIVE:
                continue
            with self.subTest(algorithm=alg.__class__.__name__, func=alg):
                s = alg.normalized_distance('spam', 'qwer')
                self.assertEqual(s, 1)


class CommonCompareTest(unittest.TestCase):
    texts = (
        ('text', 'test'),
        ('bulk', 'test'),
        ('xx', 'xxx'),
        ('x', 'xxx'),
    )

    def test_normalized(self):
        for alg in algos:
            alg_name = alg.__class__.__name__
            for t1, t2 in self.texts:
                with self.subTest(algorithm=alg_name, func=alg, t1=t1, t2=t2, cat='dist'):
                    d = alg.normalized_distance(t1, t2)
                    self.assertGreaterEqual(d, 0)
                    self.assertLessEqual(d, 1)

                with self.subTest(algorithm=alg_name, func=alg, t1=t1, t2=t2, cat='sim'):
                    s = alg.normalized_similarity(t1, t2)
                    self.assertGreaterEqual(s, 0)
                    self.assertLessEqual(s, 1)
