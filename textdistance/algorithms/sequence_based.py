from difflib import SequenceMatcher as _SequenceMatcher
from .base import BaseSimilarity as _BaseSimilarity
from textdistance.utils import find_ngrams


__all__ = ['lcsseq', 'lcsstr', 'ratcliff_obershelp']


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


class LCSStr(_BaseSimilarity):
    """longest common substring similarity
    """
    def __init__(self, qval=1, empty=''):
        self.qval = qval
        self.empty = empty

    def _standart(self, s1, s2):
        matcher = _SequenceMatcher(a=s1, b=s2)
        match = matcher.find_longest_match(0, len(s1), 0, len(s2))
        return s1[match.a: match.a + match.size]

    def _custom(self, *sequences):
        short = min(sequences, key=len)
        length = len(short)
        for n in range(length, 0, -1):
            for subseq in find_ngrams(short, n):
                subseq = ''.join(subseq)
                for seq in sequences:
                    if subseq not in seq:
                        break
                else:
                    return subseq
        return self.empty

    def __call__(self, *sequences):
        if not all(sequences):
            return self.empty
        length = len(sequences)
        if length == 0:
            return self.empty
        if length == 1:
            return sequences[0]
        if length == 2:
            return self._standart(*sequences)
        return self._custom(*sequences)

    def similarity(self, *sequences):
        return len(self(*sequences))


class RatcliffObershelp(_BaseSimilarity):
    """Ratcliff-Obershelp similarity
    This follows the Ratcliff-Obershelp algorithm to derive a similarity
    measure:
        1. Find the length of the longest common substring in src & tar.
        2. Recurse on the strings to the left & right of each this substring
           in src & tar. The base case is a 0 length common substring, in which
           case, return 0. Otherwise, return the sum of the current longest
           common substring and the left & right recursed sums.
        3. Multiply this length by 2 and divide by the sum of the lengths of
           src & tar.

    http://www.drdobbs.com/database/pattern-matching-the-gestalt-approach/184407970
    """

    def _lcsstr_stl(self, src, tar):
        pass

    def _sstr_matches(self, src, tar):
        pass

    def __call__(self, *sequences):
        pass


lcsseq = LCSSeq()
lcsstr = LCSStr()
ratcliff_obershelp = RatcliffObershelp
