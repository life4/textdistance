# built-in
from itertools import takewhile

# app
from .base import Base as _Base, BaseSimilarity as _BaseSimilarity


__all__ = [
    'Prefix', 'Postfix', 'Length', 'Identity', 'Matrix',
    'prefix', 'postfix', 'length', 'identity', 'matrix',
]


class Prefix(_BaseSimilarity):
    """prefix similarity
    """
    def __init__(self, qval=1, sim_test=None):
        self.qval = qval
        self.sim_test = sim_test or self._ident

    def __call__(self, *sequences):
        if not sequences:
            return 0
        sequences = self._get_sequences(*sequences)
        test = lambda seq: self.sim_test(*seq)  # noQA
        result = [c[0] for c in takewhile(test, zip(*sequences))]

        s = sequences[0]
        if isinstance(s, str):
            return ''.join(result)
        if isinstance(s, bytes):
            return b''.join(result)
        return result

    def similarity(self, *sequences):
        return len(self(*sequences))


class Postfix(Prefix):
    """postfix similarity
    """
    def __call__(self, *sequences):
        s = sequences[0]
        sequences = [reversed(s) for s in sequences]
        result = reversed(super().__call__(*sequences))
        if isinstance(s, str):
            return ''.join(result)
        if isinstance(s, bytes):
            return b''.join(result)
        return list(result)


class Length(_Base):
    """Length distance
    """
    def __call__(self, *sequences):
        lengths = list(map(len, sequences))
        return max(lengths) - min(lengths)


class Identity(_BaseSimilarity):
    """Identity similarity
    """

    def maximum(self, *sequences):
        return 1

    def __call__(self, *sequences):
        return int(self._ident(*sequences))


class Matrix(_BaseSimilarity):
    """Matrix similarity
    """

    def __init__(self, mat=None, mismatch_cost=0, match_cost=1, symmetric=True, external=True):
        self.mat = mat
        self.mismatch_cost = mismatch_cost
        self.match_cost = match_cost
        self.symmetric = symmetric
        # self.alphabet = sum(mat.keys(), ())

    def maximum(self, *sequences):
        return self.match_cost

    def __call__(self, *sequences):
        if not self.mat:
            if self._ident(*sequences):
                return self.match_cost
            return self.mismatch_cost

        # search in matrix
        if sequences in self.mat:
            return self.mat[sequences]
        # search in symmetric matrix
        if self.symmetric:
            sequences = tuple(reversed(sequences))
            if sequences in self.mat:
                return self.mat[sequences]
        # if identity then return match_cost
        if self._ident(*sequences):
            return self.match_cost
        # not found
        return self.mismatch_cost


prefix = Prefix()
postfix = Postfix()
length = Length()
identity = Identity()
matrix = Matrix()
