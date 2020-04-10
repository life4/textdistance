# project
from __main__ import textdistance, unittest


class LCSStrTest(unittest.TestCase):
    alg = textdistance.lcsstr

    def test_common(self):
        # prefix
        self.assertEqual(self.alg('ab', 'abcd'), 'ab')
        self.assertEqual(self.alg('abcd', 'ab'), 'ab')

        # middle
        self.assertEqual(self.alg('abcd', 'bc'), 'bc')
        self.assertEqual(self.alg('bc', 'abcd'), 'bc')

        # suffix
        self.assertEqual(self.alg('abcd', 'cd'), 'cd')
        self.assertEqual(self.alg('abcd', 'cd'), 'cd')

        # no
        self.assertEqual(self.alg('abcd', 'ef'), '')
        self.assertEqual(self.alg('ef', 'abcd'), '')

        # long
        # https://github.com/life4/textdistance/issues/40
        self.assertEqual(self.alg('MYTEST' * 100, 'TEST'), 'TEST')
        self.assertEqual(self.alg('TEST', 'MYTEST' * 100), 'TEST')
