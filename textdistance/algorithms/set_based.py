from .base import Base as _Base


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


jaccard = Jaccard()
sorensen = Sorensen()
