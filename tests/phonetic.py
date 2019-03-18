# project
from __main__ import textdistance, unittest, NUMPY


class EditexTest(unittest.TestCase):
    alg = textdistance.editex

    def test_common(self):
        # https://github.com/chrislit/abydos/blob/master/tests/distance/test_distance_editex.py
        self.assertEqual(self.alg.distance('', ''), 0)
        self.assertEqual(self.alg.distance('nelson', ''), len('nelson') * 2)
        self.assertEqual(self.alg.distance('', 'neilsen'), len('neilsen') * 2)
        self.assertEqual(self.alg.distance('ab', 'a'), 2)
        self.assertEqual(self.alg.distance('ab', 'c'), 4)
        self.assertEqual(self.alg.distance('nelson', 'neilsen'), 2)
        self.assertEqual(self.alg.distance('neilsen', 'nelson'), 2)
        self.assertEqual(self.alg.distance('niall', 'neal'), 1)
        self.assertEqual(self.alg.distance('neal', 'niall'), 1)
        self.assertEqual(self.alg.distance('niall', 'nihal'), 2)
        self.assertEqual(self.alg.distance('nihal', 'niall'), 2)
        self.assertEqual(self.alg.distance('neal', 'nihl'), 3)
        self.assertEqual(self.alg.distance('nihl', 'neal'), 3)

        # https://anhaidgroup.github.io/py_stringmatching/v0.3.x/Editex.html
        self.assertEqual(self.alg.distance('cat', 'hat'), 2)
        self.assertEqual(self.alg.distance('Niall', 'Neil'), 2)
        self.assertEqual(self.alg.distance('aluminum', 'Catalan'), 12)
        self.assertEqual(self.alg.distance('ATCG', 'TAGC'), 6)

    def test_local(self):
        alg = textdistance.Editex(local=True)
        self.assertEqual(alg.distance('', ''), 0)
        self.assertEqual(alg.distance('nelson', ''), 12)
        self.assertEqual(alg.distance('', 'neilsen'), 14)
        self.assertEqual(alg.distance('ab', 'a'), 2)
        self.assertEqual(alg.distance('ab', 'c'), 2)
        self.assertEqual(alg.distance('nelson', 'neilsen'), 2)
        self.assertEqual(alg.distance('neilsen', 'nelson'), 2)
        self.assertEqual(alg.distance('niall', 'neal'), 1)
        self.assertEqual(alg.distance('neal', 'niall'), 1)
        self.assertEqual(alg.distance('niall', 'nihal'), 2)
        self.assertEqual(alg.distance('nihal', 'niall'), 2)
        self.assertEqual(alg.distance('neal', 'nihl'), 3)
        self.assertEqual(alg.distance('nihl', 'neal'), 3)
