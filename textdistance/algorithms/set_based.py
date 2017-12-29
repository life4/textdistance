from collections import Counter
from .base import Base as _Base
from textdistance.utils import find_ngrams


__all__ = ['jaccard', 'sorensen']


class Jaccard(_Base):
    '''
    Compute the Jaccard distance between the two sequences.
    They should contain hashable items.
    The return value is a float between 0 and 1, where 0 means equal,
    and 1 totally different.
    '''
    def __call__(self, *sequences):
        sequences = map(set, sequences)
        return 1 - len(set.intersection(sequences)) / float(len(set.union(sequences)))


class Sorensen(_Base):
    '''
    Compute the Sorensen distance between the two sequences.
    They should contain hashable items.
    The return value is a float between 0 and 1, where 0 means equal,
    and 1 totally different.
    '''
    def __call__(self, *sequences):
        sequences = map(set, sequences)
        total_length = sum(map(len, sequences))
        return 1 - (2 * len(set.intersection(sequences)) / float(total_length))


class Tversky(_Base):
    """Tversky index
    https://en.wikipedia.org/wiki/Tversky_index
    """
    def __init__(self, qval=2, alpha=1, beta=1, bias=None):
        self.qval = qval
        self.alpha = alpha
        self.beta = beta
        self.bias = bias

    def __call__(self, s1, s2):
        if s1 == s2:
            return 1.0
        elif len(s1) == 0 or len(s2) == 0:
            return 0.0

        if self.qval and self.qval > 0:
            s1 = Counter(find_ngrams(s1, self.qval))
            s2 = Counter(find_ngrams(s2, self.qval))
        else:
            s1 = Counter(s1.strip().split())
            s2 = Counter(s2.strip().split())

        if len(s1) == 0 or len(s2) == 0:
            return 0.0

        q_intersection_mag = sum((s1 & s2).values())
        s1 = sum(s1.values())
        s2 = sum(s2.values())

        if self.bias is None:
            result = q_intersection_mag
            result += self.alpha * (s1 - q_intersection_mag)
            result += self.beta * (s2 - q_intersection_mag)
            return q_intersection_mag / result
        else:
            a_val = min(
                s1 - q_intersection_mag,
                s2 - q_intersection_mag
            )
            b_val = max(
                s1 - q_intersection_mag,
                s2 - q_intersection_mag
            )
            c_val = q_intersection_mag + self.bias
            result = self.alpha * a_val + (1 - self.alpha) * b_val
            result = self.beta * result + c_val
            return c_val / result


jaccard = Jaccard()
sorensen = Sorensen()
tversky = Tversky()
