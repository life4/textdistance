from __main__ import unittest, textdistance
from fractions import Fraction


class ArithNCDTest(unittest.TestCase):
    alg = textdistance.arith_ncd

    def test_make_probs(self):
        probs = self.alg._make_probs('lol', 'lal')
        self.assertEqual(probs['l'], (Fraction(0, 1), Fraction(4, 7)))
        # self.assertEqual(probs['o'], Fraction(1, 7))
        # self.assertEqual(probs['a'], Fraction(1, 7))
