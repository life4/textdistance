from __main__ import unittest, textdistance
from fractions import Fraction


class CommonNCDTest(unittest.TestCase):
    def test_monotonicity(self):
        algos = (
            textdistance.arith_ncd,
            # textdistance.bwtrle_ncd,
            textdistance.bz2_ncd,
            # textdistance.lzma_ncd,
            # textdistance.rle_ncd,
            # textdistance.zlib_ncd,
            textdistance.nc_ncd,
            textdistance.redundancy_ncd,
        )
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__, func=alg):
                same = alg('test', 'test')
                similar = alg('test', 'text')
                diffirent = alg('test', 'nani')
                self.assertLess(same, similar)
                self.assertLess(similar, diffirent)

    def test_monotonicity2(self):
        algos = (
            textdistance.arith_ncd,
            textdistance.bwtrle_ncd,
            textdistance.bz2_ncd,
            textdistance.lzma_ncd,
            textdistance.rle_ncd,
            textdistance.zlib_ncd,
            textdistance.nc_ncd,
            textdistance.redundancy_ncd,
        )
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__, func=alg):
                same = alg('test', 'test')
                similar = alg('test', 'text')
                diffirent = alg('test', 'nani')
                self.assertLessEqual(same, similar)
                self.assertLessEqual(similar, diffirent)

    def test_symmetry(self):
        algos = (
            # textdistance.arith_ncd,
            # textdistance.bwtrle_ncd,
            textdistance.bz2_ncd,
            textdistance.lzma_ncd,
            textdistance.rle_ncd,
            textdistance.zlib_ncd,
            textdistance.nc_ncd,
            textdistance.redundancy_ncd,
        )
        for alg in algos:
            with self.subTest(algorithm=alg.__class__.__name__, func=alg):
                self.assertEqual(alg('aab', 'aab'), alg('abb', 'abb'))
                self.assertEqual(alg('aab', 'abb'), alg('abb', 'aab'))
                self.assertEqual(alg('a', 'b'), alg('b', 'a'))
                self.assertEqual(alg('ab', 'ba'), alg('ba', 'ab'))


class ArithNCDTest(unittest.TestCase):
    alg = textdistance.ArithNCD(terminator='\x00')

    def test_make_probs(self):
        probs = self.alg._make_probs('lol', 'lal')
        self.assertEqual(probs['l'], (Fraction(0, 1), Fraction(4, 7)))
        self.assertEqual(probs['o'][1], Fraction(1, 7))
        self.assertEqual(probs['a'][1], Fraction(1, 7))

    def test_arith_output(self):
        fraction = self.alg._compress('BANANA')
        self.assertEqual(fraction.numerator, 1525)

    def test_arith_distance(self):
        same = self.alg('test', 'test')
        similar = self.alg('test', 'text')
        diffirent = self.alg('test', 'nani')
        self.assertLess(same, similar)
        self.assertLess(similar, diffirent)


class NCNCDTest(unittest.TestCase):
    alg = textdistance.nc_ncd

    def test_simmetry_compressor(self):
        self.assertEqual(self.alg._compress('ab'), self.alg._compress('ba'))

    def test_idempotency_compressor(self):
        # I've modified idempotency to some kind of distributivity for constant.
        # Now it indicates that compressor really compress.
        self.assertLess(self.alg._get_size('aa'), self.alg._get_size('a') * 2)

    def test_monotonicity_compressor(self):
        self.assertLess(self.alg._get_size('ab'), self.alg._get_size('abc'))

    def test_distributivity_compressor(self):
        self.assertLess(
            self.alg._get_size('ab') + self.alg._get_size('c'),
            self.alg._get_size('ac') + self.alg._get_size('bc'),
        )

    def test_distance(self):
        same = self.alg('test', 'test')
        similar = self.alg('test', 'text')
        diffirent = self.alg('test', 'nani')
        self.assertLess(same, similar)
        self.assertLess(similar, diffirent)

    def test_simmetry_distance(self):
        self.assertEqual(self.alg('aab', 'aab'), self.alg('abb', 'abb'))
        self.assertEqual(self.alg('aab', 'abb'), self.alg('abb', 'aab'))
        self.assertEqual(self.alg('a', 'b'), self.alg('b', 'a'))
        self.assertEqual(self.alg('ab', 'ba'), self.alg('ba', 'ab'))
