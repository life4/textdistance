from itertools import takewhile
from .base import BaseSimilarity as _BaseSimilarity

__all__ = ['prefix', 'postfix']

try:
    string_types = (str, unicode)
except NameError:
    string_types = (str, )


class Prefix(_BaseSimilarity):
    """prefix distance
    """
    def __init__(self, qval=1, sim_test=None):
        self.qval = qval
        self.sim_test = sim_test or self._ident

    def __call__(self, *sequences):
        if not sequences:
            return 0
        sequences = self._get_sequences(*sequences)
        test = lambda seq: self.sim_test(*seq)
        result = [c[0] for c in takewhile(test, zip(*sequences))]

        s = sequences[0]
        if isinstance(s, string_types):
            return ''.join(result)
        if isinstance(s, bytes):
            return b''.join(result)
        return result

    def similarity(self, *sequences):
        return len(self(*sequences))


class Postfix(Prefix):
    def __call__(self, *sequences):
        s = sequences[0]
        sequences = [reversed(s) for s in sequences]
        result = reversed(super(Postfix, self).__call__(*sequences))
        if isinstance(s, string_types):
            return ''.join(result)
        if isinstance(s, bytes):
            return b''.join(result)
        return list(result)


prefix = Prefix()
postfix = Postfix()
