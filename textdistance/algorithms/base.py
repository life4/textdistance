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

    def quick_answer(self, *sequences):
        if not sequences:
            return 0
        if len(sequences) == 1:
            return 0
        if self._ident(*sequences):
            return 0
        if not all(sequences):
            return self.maximum(*sequences)

    def _ident(self, *elements):
        try:
            # for hashable elements
            return len(set(elements)) == 1
        except TypeError:
            # for unhashable elements
            for e1, e2 in zip(elements, elements[1:]):
                if e1 != e2:
                    return False
            return True

    def _get_sequences(self, *sequences):
        # by words
        if not self.qval:
            return [s.split() for s in sequences]
        # by chars
        if self.qval == 1:
            return sequences
        # by n-grams
        return [find_ngrams(s, self.qval) for s in sequences]

    def _get_counters(self, *sequences):
        # already Counters
        if all(isinstance(s, Counter) for s in sequences):
            return sequences
        return [Counter(s) for s in self._get_sequences(*sequences)]

    def _intersect_counters(self, *sequences):
        intersection = sequences[0].copy()
        for s in sequences[1:]:
            intersection &= s
        return intersection

    def _union_counters(self, *sequences):
        union = sequences[0]
        for s in sequences[1:]:
            union |= s
        return union

    def _count_counters(self, counter):
        if getattr(self, 'as_set', False):
            return len(set(counter))
        else:
            return sum(counter.values())


class BaseSimilarity(Base):
    def distance(self, *sequences):
        return self.maximum(*sequences) - self.similarity(*sequences)

    def similarity(self, *sequences):
        return self(*sequences)

    def quick_answer(self, *sequences):
        if not sequences:
            return self.maximum(*sequences)
        if len(sequences) == 1:
            return self.maximum(*sequences)
        if self._ident(*sequences):
            return self.maximum(*sequences)
        if not all(sequences):
            return 0
