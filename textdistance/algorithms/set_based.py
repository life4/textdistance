

__all__ = ['jaccard', 'sorensen']


def jaccard(*sequences):
    '''
    Compute the Jaccard distance between the two sequences.
    They should contain hashable items.
    The return value is a float between 0 and 1, where 0 means equal,
    and 1 totally different.
    '''
    sequences = map(set, sequences)
    return 1 - len(set.intersection(sequences)) / float(len(set.union(sequences)))


def sorensen(*sequences):
    '''
    Compute the Sorensen distance between the two sequences.
    They should contain hashable items.
    The return value is a float between 0 and 1, where 0 means equal,
    and 1 totally different.
    '''
    sequences = map(set, sequences)
    total_length = sum(map(len, sequences))
    return 1 - (2 * len(set.intersection(sequences)) / float(total_length))
