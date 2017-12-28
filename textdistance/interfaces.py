import warnings

from . import algorithms
from .utils import words_combinations


class Distance(object):
    h = staticmethod(algorithms.hamming)
    dl = staticmethod(algorithms.damerau_levenshtein)
    l = staticmethod(algorithms.levenshtein)
    s = staticmethod(algorithms.sorensen)
    j = staticmethod(algorithms.jaccard)

    def __call__(self, algorithm, *sequences):
        warnings.warn("This interface is deprecated", DeprecationWarning)

        if algorithm[0] == 'h':
            f = algorithms.hamming
        elif algorithm[:2] == 'dl':
            f = algorithms.damerau_levenshtein
        elif algorithm[0] == 'l':
            f = algorithms.levenshtein
        elif algorithm[0] == 's':
            f = algorithms.sorensen
        elif algorithm[0] == 'j':
            f = algorithms.jaccard
        else:
            raise KeyError('bad algorithm!')

        if algorithm[-2:] == 'we':
            f.equality = True
            return words_combinations(f, *sequences)
        if algorithm[-1] == 'w':
            f.equality = False
            return words_combinations(f, *sequences)
        return f(*sequences)

    def compare(self, algorithm, sequence, sequences):
        for t in sequences:
            yield self(algorithm, sequence, t), t

    def find_minimal(self, algorithm, sequence, sequences):
        return min(self.compare(algorithm, sequence, sequences))

    def find_similar(self, algorithm, sequence, sequences, n=3):
        for difference, seq in self.compare(algorithm, sequence, sequences):
            if difference <= n:
                return difference, seq


distance = Distance()
