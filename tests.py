import unittest
from textdistance import distance


class TestAlgos(unittest.TestCase):
	
	def test_hamming(self):
		with self.subTest(length='equal', distance='1', texts='2'):
			self.assertEqual(distance.h('lorem', 'lorim'), 1)
		with self.subTest(length='not-equal', distance='2', texts='2'):
			self.assertEqual(distance.h('lorem', 'loremus'), 2)
		with self.subTest(length='not-equal', distance='3', texts='2'):
			self.assertEqual(distance.h('lorem', 'lorimus'), 3)
		with self.subTest(length='not-equal', distance='3', texts='3'):
			self.assertEqual(distance.h('lorem', 'lorimus', 'larem'), 4)
	
	def test_levenshtein(self):
		with self.subTest(category='substitution'):
			self.assertEqual(distance.l('lorem', 'lorim'), 1)
		with self.subTest(category='insertion'):
			self.assertEqual(distance.l('lorem', 'loriem'), 1)
		with self.subTest(category='deletion'):
			self.assertEqual(distance.l('lorem', 'lrem'), 1)
	
	def test_damerau_levenshtein(self):
		with self.subTest(category='substitution'):
			self.assertEqual(distance.dl('lorem', 'lorim'), 1)
		with self.subTest(category='insertion'):
			self.assertEqual(distance.dl('lorem', 'loriem'), 1)
		with self.subTest(category='deletion'):
			self.assertEqual(distance.dl('lorem', 'lrem'), 1)
		with self.subTest(category='transposition'):
			self.assertEqual(distance.dl('lorem', 'loerm'), 1)
	
	def test_word(self):
		with self.subTest(algo='dlw', distance='1'):
			self.assertEqual(distance('dlw', 'lorem ipsum', 'ipsum lorum'), 1)
		with self.subTest(algo='dlw', distance='1', words='+1'):
			self.assertEqual(distance('dlw', 'lorem ipsum dolor', 'ipsum lorum'), 7)
		with self.subTest(algo='dlwe', distance='1'):
			self.assertEqual(distance('dlwe', 'lorem ipsum dolor', 'ipsum lorum'), 1)
	
	def test_minimal(self):
		with self.subTest(algo='h', distance='1'):
			self.assertEqual(distance.find_minimal('h', 'lorem', ['larum', 'lorum']), (1, 'lorum'))


if __name__ == '__main__':
	unittest.main()
