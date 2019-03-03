from __main__ import unittest, textdistance
from fractions import Fraction


class ArithNCDTest(unittest.TestCase):
    alg = textdistance.arith_ncd

    def test_make_probs(self):
        probs = self.alg._make_probs('lol', 'lal')
        self.assertEqual(probs['l'], (Fraction(0, 1), Fraction(4, 7)))
        self.assertEqual(probs['o'][1], Fraction(1, 7))
        self.assertEqual(probs['a'][1], Fraction(1, 7))

    def test_arith_output(self):
        probs = self.alg._make_probs('BANA', 'NA')
        numerator = self.alg._compress('BANANA', probs=probs)
        self.assertEqual(int(numerator, 2), 1525)
