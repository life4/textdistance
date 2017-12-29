from collections import Counter
from textdistance.utils import find_ngrams

# python3
try:
    from functools import reduce
except ImportError:
    pass


class Base(object):
    def __init__(self, qval=1):
        self.qval = qval

    def __call__(self, *sequences):
        raise NotImplementedError

    def maximum(self, *sequences):
        return max(map(len, sequences))

    def distance(self, *sequences):
        return self(*sequences)

    def similarity(self, *sequences):
        return self.maximum(*sequences) - self.distance(*sequences)

    def normalized_distance(self, *sequences):
        return self.distance(*sequences) / self.maximum(*sequences)

    def normalized_similarity(self, *sequences):
        return 1 - self.normalized_distance(*sequences)

    def _ident(self, *sequences):
        return reduce(lambda s1, s2: s1 == s2, sequences)

    def _get_counters(self, *sequences):
        # already Counters
        if all(isinstance(s, Counter) for s in sequences):
            return sequences
        # by words
        if not self.qval:
            return [s.split() for s in sequences]
        # by chars
        if self.qval == 1:
            return [Counter(s) for s in sequences]
        # by n-grams
        return [Counter(find_ngrams(s, self.qval)) for s in sequences]

    def _intersect_counters(self, *sequences):
        intersection = sequences[0]
        for s in sequences[1:]:
            intersection &= s
        return intersection

    def _union_counters(self, *sequences):
        union = sequences[0]
        for s in sequences[1:]:
            union |= s
        return union

    def _count_counters(self, counter):
        return sum(counter.values())


class BaseSimilarity(Base):
    def distance(self, *sequences):
        return self.maximum(*sequences) - self.distance(*sequences)

    def similarity(self, *sequences):
        return self(*sequences)
