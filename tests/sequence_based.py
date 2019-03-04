# project
from __main__ import textdistance, unittest


class LCSSeqTest(unittest.TestCase):
    alg = textdistance.lcsseq

    def test_common(self):
        self.assertEqual(self.alg('ab', 'cd'), '')
        self.assertEqual(self.alg('abcd', 'abcd'), 'abcd')

        self.assertEqual(self.alg('test', 'text'), 'tet')
        self.assertEqual(self.alg('thisisatest', 'testing123testing'), 'tsitest')
        self.assertEqual(self.alg('DIXON', 'DICKSONX'), 'DION')
        self.assertEqual(self.alg('random exponential', 'layer activation'), 'ratia')

        self.assertEqual(self.alg('a', 'b', 'c'), '')
        self.assertEqual(self.alg('a', 'a', 'a'), 'a')
        self.assertEqual(self.alg('test', 'text', 'tempest'), 'tet')

        self.assertEqual(self.alg('a' * 80, 'a' * 80), 'a' * 80)
        self.assertEqual(self.alg('a' * 80, 'b' * 80), '')
