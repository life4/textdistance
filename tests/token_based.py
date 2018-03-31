from __main__ import unittest, textdistance


class JaccardTest(unittest.TestCase):
    alg = textdistance.jaccard

    def test_common(self):
        self.assertAlmostEqual(self.alg.similarity('test', 'text'), 3.0 / 5)
        self.assertAlmostEqual(self.alg.similarity('nelson', 'neilsen'), 5.0 / 8)
        self.assertAlmostEqual(self.alg.similarity('decide', 'resize'), 3.0 / 9)

        td = float(textdistance.Tversky(ks=[1, 1]).distance('nelson', 'neilsen'))
        jd = float(textdistance.jaccard.distance('nelson', 'neilsen'))
        self.assertAlmostEqual(jd, td)


class SorensenTest(unittest.TestCase):
    alg = textdistance.sorensen

    def test_common(self):
        self.assertAlmostEqual(self.alg.similarity('test', 'text'), 2.0 * 3 / 8)

        td = float(textdistance.Tversky(ks=[.5, .5]).distance('nelson', 'neilsen'))
        sd = float(textdistance.sorensen.distance('nelson', 'neilsen'))
        self.assertAlmostEqual(sd, td)


class OverlapTest(unittest.TestCase):
    alg = textdistance.overlap

    def test_common(self):
        self.assertAlmostEqual(self.alg('test', 'text'), 3.0 / 4)
        self.assertAlmostEqual(self.alg('testme', 'textthis'), 4.0 / 6)
        self.assertAlmostEqual(self.alg('nelson', 'neilsen'), 5.0 / 6)


class CosineTest(unittest.TestCase):
    alg = textdistance.cosine

    def test_common(self):
        self.assertAlmostEqual(self.alg('test', 'text'), 3.0 / 4)
        self.assertAlmostEqual(self.alg('nelson', 'neilsen'), 5.0 / pow(6 * 7, .5))


class MongeElkanTest(unittest.TestCase):
    alg = textdistance.MongeElkan(qval=2).normalized_distance

    def test_common(self):
        self.assertAlmostEqual(self.alg('Niall', 'Neal'), 3.0 / 4)
        self.assertEqual(self.alg('Niall', 'Niel'), 3.0 / 4)
        self.assertEqual(self.alg('Niall', 'Nigel'), 3.0 / 4)

        alg = textdistance.MongeElkan(qval=2, symmetric=True).normalized_distance
        self.assertAlmostEqual(alg('text', 'test'), 2.0 / 3)


class BagTest(unittest.TestCase):
    alg = textdistance.bag

    def test_common(self):
        self.assertAlmostEqual(self.alg('qwe', 'qwe'), 0)
        self.assertAlmostEqual(self.alg('qwe', 'erty'), 3)
        self.assertAlmostEqual(self.alg('qwe', 'ewq'), 0)
        self.assertAlmostEqual(self.alg('qwe', 'rtys'), 4)


class CompareTest(unittest.TestCase):
    test_cases = (
        ('test', 'text'),
        ('qwe', 'rty'),
        ('test', 'testme'),
        ('qewr', 'qwer'),
    )

    def test_jaccard_tversky(self):
        for s1, s2 in self.test_cases:
            with self.subTest(s1=s1, s2=s2):
                self.assertAlmostEqual(
                    textdistance.jaccard.distance(s1, s2),
                    textdistance.Tversky(ks=[1, 1]).distance(s1, s2),
                )

    def test_sorensen_tversky(self):
        for s1, s2 in self.test_cases:
            with self.subTest(s1=s1, s2=s2):
                self.assertAlmostEqual(
                    textdistance.sorensen.distance(s1, s2),
                    textdistance.Tversky(ks=[.5, .5]).distance(s1, s2),
                )

    def test_jaccard_tversky_as_set(self):
        for s1, s2 in self.test_cases:
            with self.subTest(s1=s1, s2=s2):
                self.assertAlmostEqual(
                    textdistance.Jaccard(as_set=True).distance(s1, s2),
                    textdistance.Tversky(as_set=True, ks=[1, 1]).distance(s1, s2),
                )

    def test_sorensen_tversky_as_set(self):
        for s1, s2 in self.test_cases:
            with self.subTest(s1=s1, s2=s2):
                self.assertAlmostEqual(
                    textdistance.Sorensen(as_set=True).distance(s1, s2),
                    textdistance.Tversky(as_set=True, ks=[.5, .5]).distance(s1, s2),
                )
