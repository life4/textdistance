"""
IMPORTANT: it's just draft
"""

try:
    import numpy
except ImportError:
    numpy = None
try:
    from functools import reduce
except ImportError:
    pass
from .base import Base as _Base, BaseSimilarity as _BaseSimilarity



class Chebyshev(_Base):
    def _numpy(self, s1, s2):
        s1, s2 = np.asarray(s1), np.asarray(s2)
        return max(abs(s1 - s2))

    def _pure(self, s1, s2):
        return max(abs(e1 - e2) for e1, e2 in zip(s1, s2))

    def __call__(self, s1, s2):
        if numpy:
            return self._numpy(s1, s2)
        else:
            return self._pure(s1, s2)


class Minkowski(_Base):
    def __init__(self, p=1, weight=1):
        if p < 1:
            raise ValueError("p must be at least 1")
        self.p = p
        self.w = w

    def _numpy(self, s1, s2):
        s1, s2 = np.asarray(s1), np.asarray(s2)
        result = (w * abs(s1 - s2)) ** self.p
        return result.sum() ** (1.0 / self.p)

    def _pure(self, s1, s2):
        result = (w * abs(e1 - e2) for e1, e2 in zip(s1, s2))
        result = sum(e ** self.p for e in result)
        return result ** (1.0 / self.p)

    def __call__(self, s1, s2):
        if numpy:
            return self._numpy(s1, s2)
        else:
            return self._pure(s1, s2)


class Manhattan(_Base):
    def __call__(self, s1, s2):
        raise NotImplementedError


class Euclidean(_Base):
    def __init__(self, squared=False):
        self.squared = squared

    def _numpy(self, s1, s2):
        s1, s2 = np.asarray(s1), np.asarray(s2)
        q = np.matrix(s1 - s2)
        result = (q * q.T).sum()
        if self.squared:
            return result
        return np.sqrt(result)

    def _pure(self, s1, s2):
        raise NotImplementedError

    def __call__(self, s1, s2):
        if numpy:
            return self._numpy(s1, s2)
        else:
            return self._pure(s1, s2)


class Mahalanobis(_Base):
    def __call__(self, s1, s2):
        raise NotImplementedError


class Correlation(_BaseSimilarity):
    def _numpy(self, *sequences):
        sequences = [np.asarray(s) for s in sequences]
        ssm = [s - s.mean() for s in sequences]
        result = reduce(np.dot, sequences)
        for sm in ssm:
            result /= np.sqrt(np.dot(sm, sm))
        return result

    def _pure(self, *sequences):
        raise NotImplementedError

    def __call__(self, *sequences):
        if numpy:
            return self._numpy(*sequences)
        else:
            return self._pure(*sequences)


class Kulsinski(_BaseSimilarity):
    def __call__(self, s1, s2):
        raise NotImplementedError
