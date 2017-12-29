from collections import Counter
from itertools import repeat
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
    def __init__(self, qval=2, ks=None, bias=None):
        self.qval = qval
        self.ks = ks
        self.bias = bias

    def __call__(self, *sequences):
        # all is equeal
        if len(set(sequences)) <= 1:
            return 1.0
        # any set is empty
        elif not min(map(len, sequences)):
            return 0.0

        if self.qval and self.qval > 0:
            sequences = [Counter(find_ngrams(s, self.qval)) for s in sequences]
        else:
            sequences = [s.split() for s in sequences]

        intersection = sequences[0]
        for s in sequences[1:]:
            intersection &= s
        intersection = sum(intersection.values())
        sequences = [sum(s.values()) for s in sequences]
        ks = self.ks[:len(sequences)]

        if self.bias is None:
            result = intersection
            for k, s in zip(ks, sequences):
                result += k * (s - intersection)
            return intersection / result

        a_val = min([s - intersection for s in sequences])
        b_val = max([s - intersection for s in sequences])
        c_val = intersection + self.bias
        ks_prod = map(lambda a, b: a * b, ks)
        ks_beta = ks[0] and (ks_prod / ks[0])
        result = ks_prod * (a_val - b_val) + b_val * ks_beta
        return c_val / (result + c_val)


jaccard = Jaccard()
sorensen = Sorensen()
tversky = Tversky()
