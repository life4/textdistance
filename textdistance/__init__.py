from itertools import zip_longest, product, permutations

class Distance:
	'''
	algorithms:
	h - hamming: substitution.
	l - levenstein: deletion, insertion, substitution.
	dl - damerau-levenshtein: deletion, insertion, substitution, transposition.
	s - sorensen. 0-1.
	j - jaccard. 0-1.
	'''
	
	#hamming
	@staticmethod
	def h(*texts):
		'''
		Compute the Hamming distance between the two or more sequences.
		The Hamming distance is the number of differing items in ordered sequences.
		'''
		f = lambda x: len(set(x)) > 1
		return len([1 for t in zip_longest(*texts) if f(t)])
	
	#jaccard
	@staticmethod
	def j(s1, s2):
		'''
		Compute the Jaccard distance between the two sequences.
		They should contain hashable items.
		The return value is a float between 0 and 1, where 0 means equal, 
		and 1 totally different.
		'''
		s1, s2 = set(s1), set(s2)
		return 1 - len(s1 & s2) / float(len(s1 | s2))
	
	#sorensen
	@staticmethod
	def s(s1, s2):
		'''
		Compute the Sorensen distance between the two sequences.
		They should contain hashable items.
		The return value is a float between 0 and 1, where 0 means equal, 
		and 1 totally different.
		'''
		s1, s2 = set(s1), set(s2)
		return 1 - (2 * len(s1 & s2) / float(len(s1) + len(s2)))
	
	#levenshtein
	@classmethod
	def l(cl, s1, s2):
		'''
		Compute the absolute Levenshtein distance between the two sequences.
		The Levenshtein distance is the minimum number of edit operations necessary
		for transforming one sequence into the other. The edit operations allowed are:
		
			* deletion:     ABC -> BC, AC, AB
			* insertion:    ABC -> ABCD, EABC, AEBC..
			* substitution: ABC -> ABE, ADC, FBC..
		'''
		if not s1 or not s2:
			return len(s1) + len(s2)
		elif s1[-1] == s2[-1]:
			return cl.l(s1[:-1], s2[:-1])
		else:
			#deletion/insertion
			a = min(cl.l(s1[:-1], s2), cl.l(s1, s2[:-1]))
			#substitution
			b = cl.l(s1[:-1], s2[:-1])
			return min(a, b) + 1
	
	#damerau-levenshtein
	@staticmethod
	def dl(s1, s2):
		'''
		Compute the absolute Damerau-Levenshtein distance between the two sequences.
		The Damerau-Levenshtein distance is the minimum number of edit operations necessary
		for transforming one sequence into the other. The edit operations allowed are:
		
			* deletion:     ABC -> BC, AC, AB
			* insertion:    ABC -> ABCD, EABC, AEBC..
			* substitution: ABC -> ABE, ADC, FBC..
			* transposition: ABC -> ACB, BAC
		'''
		d = {}
		len_s1 = len(s1)
		len_s2 = len(s2)
		for i in range(-1, len_s1 + 1):
			d[i, -1] = i + 1
		for j in range(-1, len_s2 + 1):
			d[-1, j] = j + 1
		
		for i in range(len_s1):
			for j in range(len_s2):
				if s1[i] == s2[j]:
					cost = 0
				else:
					cost = 1
				
				d[(i, j)] = min(
					d[i - 1, j] + 1,  #deletion
					d[i, j - 1] + 1,  #insertion
					d[i - 1, j - 1] + cost,  #substitution
				)
				
				if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
					d[i, j] = min(d[i, j], d[i - 2, j - 2] + cost) #transposition
		return d[len_s1 - 1, len_s2 - 1]
	
	@staticmethod
	def w(f, *texts, equality=False):
		m = float('Inf')
		#split by words
		texts = [t.split() for t in texts]
		#permutations
		texts = [permutations(words) for words in texts]
		#combinations
		for subtexts in product(*texts):
			if equality:
				words_min_cnt = len(min(subtexts, key=len))
				subtexts = [t[:words_min_cnt] for t in subtexts]
			subtexts = [' '.join(t) for t in subtexts]
			m = min(m, f(*subtexts))
		return m
	
	def __call__(self, algorithm, *texts):
		if algorithm[0] == 'h':
			f = self.h
		elif algorithm[:2] == 'dl':
			f = self.dl
		elif algorithm[0] == 'l':
			f = self.l
		elif algorithm[0] == 's':
			f = self.s
		elif algorithm[0] == 'j':
			f = self.j
		else:
			raise KeyError('bad algorithm!')
		
		if algorithm[-2:] == 'we':
			return self.w(f, *texts, equality=True)
		if algorithm[-1] == 'w':
			return self.w(f, *texts)
		return f(*texts)
	
	def find_minimal(self, algorithm, text, texts):
		return min([(self(algorithm, text, t), t) for t in texts])


distance = Distance()
