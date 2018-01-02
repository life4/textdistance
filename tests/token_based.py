from __main__ import unittest, textdistance


class TverskyTest(unittest.TestCase):
    alg = textdistance.Tversky

    def test_common(self):
        pass

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
        #self.assertAlmostEqual(self.alg.similarity('test', 'text'), 3.0 / 5)
        #self.assertAlmostEqual(self.alg.similarity('nelson', 'neilsen'), 5.0 / 8)
        #self.assertAlmostEqual(self.alg.similarity('decide', 'resize'), 3.0 / 9)

        td = float(textdistance.Tversky(ks=[.5, .5]).distance('nelson', 'neilsen'))
        sd = float(textdistance.sorensen.distance('nelson', 'neilsen'))
        self.assertAlmostEqual(sd, td)
