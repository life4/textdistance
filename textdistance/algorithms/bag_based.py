from .base import BaseSimilarity as _BaseSimilarity


__all__ = ['bag']


class Bag(_BaseSimilarity):
    """cosine similarity (Ochiai coefficient)
    """
    def __call__(self, *sequences):
        sequences = self._get_counters(*sequences)              # sets
        intersection = self._intersect_counters(*sequences)     # set
        return self._count_counters(intersection)               # int


bag = Bag()
