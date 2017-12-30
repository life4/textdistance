# python3
from .base import BaseSimilarity as _BaseSimilarity


__all__ = ['lcsseq']


class LCSSeq(_BaseSimilarity):
    """longest common substring similarity
    """
    def __init__(self, qval=1, sim_test=None, empty=''):
        self.qval = qval
        self.empty = empty
        self.sim_test = sim_test or self._ident

    def __call__(self, *sequences):
        if not all(sequences):
            return self.empty
        if self.sim_test(*[s[-1] for s in sequences]):
            c = sequences[0][-1]
            sequences = [s[:-1] for s in sequences]
            return self(*sequences) + c
        m = self.empty
        for i, s in enumerate(sequences):
            ss = sequences[:i] + (s[:-1], ) + sequences[i + 1:]
            m = max([self(*ss), m], key=len)
        return m

    def similarity(self, *sequences):
        return len(self(*sequences))


lcsseq = LCSSeq()
