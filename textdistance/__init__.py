from itertools import product, permutations
try:
    # python3
    from itertools import zip_longest
except ImportError:
    # python2
    from itertools import izip_longest as zip_longest


class Distance(object):
    '''
    algorithms:
    h - hamming: substitution.
    l - levenstein: deletion, insertion, substitution.
    dl - damerau-levenshtein: deletion, insertion, substitution, transposition.
    s - sorensen. 0-1.
    j - jaccard. 0-1.
    '''

    # hamming
    @staticmethod
    def h(*sequences):
        '''
        Compute the Hamming distance between the two or more sequences.
        The Hamming distance is the number of differing items in ordered sequences.
        '''
        return len([1 for t in zip_longest(*sequences) if len(set(t)) > 1])

    # jaccard
    @staticmethod
    def j(*sequences):
        '''
        Compute the Jaccard distance between the two sequences.
        They should contain hashable items.
        The return value is a float between 0 and 1, where 0 means equal,
        and 1 totally different.
        '''
        sequences = map(set, sequences)
        return 1 - len(set.intersection(sequences)) / float(len(set.union(sequences)))

    # sorensen
    @staticmethod
    def s(*sequences):
        '''
        Compute the Sorensen distance between the two sequences.
        They should contain hashable items.
        The return value is a float between 0 and 1, where 0 means equal,
        and 1 totally different.
        '''
        sequences = map(set, sequences)
        total_length = sum(map(len, sequences))
        return 1 - (2 * len(set.intersection(sequences)) / float(total_length))

    # levenshtein
    @classmethod
    def l(cls, s1, s2):
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
            return cls.l(s1[:-1], s2[:-1])
        else:
            # deletion/insertion
            a = min(cls.l(s1[:-1], s2), cls.l(s1, s2[:-1]))
            # substitution
            b = cls.l(s1[:-1], s2[:-1])
            return min(a, b) + 1

    # damerau-levenshtein
    @staticmethod
    def dl(s1, s2):
        '''
        Compute the absolute Damerau-Levenshtein distance between the two sequences.
        The Damerau-Levenshtein distance is the minimum number of edit operations necessary
        for transforming one sequence into the other. The edit operations allowed are:

            * deletion:      ABC -> BC, AC, AB
            * insertion:     ABC -> ABCD, EABC, AEBC..
            * substitution:  ABC -> ABE, ADC, FBC..
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
                    d[i - 1, j] + 1,            # deletion
                    d[i, j - 1] + 1,            # insertion
                    d[i - 1, j - 1] + cost,     # substitution
                )

                if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                    d[i, j] = min(d[i, j], d[i - 2, j - 2] + cost)  # transposition
        return d[len_s1 - 1, len_s2 - 1]

    @staticmethod
    def w(f, *texts):
        m = float('Inf')
        # split by words
        texts = [t.split() for t in texts]
        # permutations
        texts = [permutations(words) for words in texts]
        # combinations
        for subtexts in product(*texts):
            if f.equality:
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
            f.equality = True
            return self.w(f, *texts)
        if algorithm[-1] == 'w':
            f.equality = False
            return self.w(f, *texts)
        return f(*texts)

    def find_minimal(self, algorithm, text, texts):
        return min([(self(algorithm, text, t), t) for t in texts])


distance = Distance()
