from itertools import product, permutations

def w_intern(f, equality, *texts):
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
