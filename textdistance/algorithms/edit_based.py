try:
    # python3
    from itertools import zip_longest
except ImportError:
    # python2
    from itertools import izip_longest as zip_longest
from .base import Base as _Base


__all__ = ['hamming', 'levenshtein', 'damerau_levenshtein']


class Hamming(_Base):
    '''
    Compute the Hamming distance between the two or more sequences.
    The Hamming distance is the number of differing items in ordered sequences.
    '''
    def __call__(self, *sequences):
        return len([1 for t in zip_longest(*sequences) if len(set(t)) > 1])


class Levenshtein(_Base):
    '''
    Compute the absolute Levenshtein distance between the two sequences.
    The Levenshtein distance is the minimum number of edit operations necessary
    for transforming one sequence into the other. The edit operations allowed are:

        * deletion:     ABC -> BC, AC, AB
        * insertion:    ABC -> ABCD, EABC, AEBC..
        * substitution: ABC -> ABE, ADC, FBC..
    '''
    def __call__(self, s1, s2):
        if not s1 or not s2:
            return len(s1) + len(s2)
        elif s1[-1] == s2[-1]:
            return self(s1[:-1], s2[:-1])
        else:
            # deletion/insertion
            a = min(self(s1[:-1], s2), self(s1, s2[:-1]))
            # substitution
            b = self(s1[:-1], s2[:-1])
            return min(a, b) + 1


class DamerauLevenshtein(_Base):
    '''
    Compute the absolute Damerau-Levenshtein distance between the two sequences.
    The Damerau-Levenshtein distance is the minimum number of edit operations necessary
    for transforming one sequence into the other. The edit operations allowed are:

        * deletion:      ABC -> BC, AC, AB
        * insertion:     ABC -> ABCD, EABC, AEBC..
        * substitution:  ABC -> ABE, ADC, FBC..
        * transposition: ABC -> ACB, BAC
    '''
    def __call__(self, s1, s2):
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


hamming = Hamming()
levenshtein = Levenshtein()
damerau_levenshtein = DamerauLevenshtein()
