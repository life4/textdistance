# python3
try:
    from functools import reduce
except ImportError:
    pass
from .base import BaseSimilarity as _BaseSimilarity


__all__ = ['lcsseq']


class LCSSeq(_BaseSimilarity):
    """cosine similarity (Ochiai coefficient)
    """
    def __call__(self, *sequences):
        pass


lcsseq =LCSSeq()
