from difflib import SequenceMatcher as _SequenceMatcher
from .base import BaseSimilarity as _BaseSimilarity
from textdistance.utils import find_ngrams


__all__ = ['lcsseq', 'lcsstr', 'ratcliff_obershelp']


class LCSSeq(_BaseSimilarity):
    """longest common subsequence similarity

    https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    """
    def __init__(self, qval=1, test_func=None):
        self.qval = qval
        self.test_func = test_func or self._ident

    def _find(self, *sequences):
        if not all(sequences):
            return type(sequences[0])()  # empty sequence
        if self.test_func(*[s[-1] for s in sequences]):
            c = sequences[0][-1]
            sequences = [s[:-1] for s in sequences]
            return self(*sequences) + c
        m = type(sequences[0])()  # empty sequence
        for i, s in enumerate(sequences):
            ss = sequences[:i] + (s[:-1], ) + sequences[i + 1:]
            m = max([self(*ss), m], key=len)
        return m

    def __call__(self, *sequences):
        if not sequences:
            return ''
        sequences = self._get_sequences(*sequences)
        return self._find(*sequences)

    def similarity(self, *sequences):
        return len(self(*sequences))


class LCSStr(_BaseSimilarity):
    """longest common substring similarity
    """
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
        return type(short)()  # empty sequence

    def __call__(self, *sequences):
        if not all(sequences):
            return ''
        length = len(sequences)
        if length == 0:
            return ''
        if length == 1:
            return sequences[0]

        sequences = self._get_sequences(*sequences)
        if length == 2:
            return self._standart(*sequences)
        return self._custom(*sequences)

    def similarity(self, *sequences):
        return len(self(*sequences))


class RatcliffObershelp(_BaseSimilarity):
    """Ratcliff-Obershelp similarity
    This follows the Ratcliff-Obershelp algorithm to derive a similarity
    measure:
        1. Find the length of the longest common substring in sequences.
        2. Recurse on the strings to the left & right of each this substring
           in sequences. The base case is a 0 length common substring, in which
           case, return 0. Otherwise, return the sum of the current longest
           common substring and the left & right recursed sums.
        3. Multiply this length by 2 and divide by the sum of the lengths of
           sequences.

    http://collaboration.cmc.ec.gc.ca/science/rpn/biblio/ddj/Website/articles/DDJ/1988/8807/8807c/8807c.htm
    https://github.com/Yomguithereal/talisman/blob/master/src/metrics/distance/ratcliff-obershelp.js
    https://xlinux.nist.gov/dads/HTML/ratcliffObershelp.html
    """

    def maximum(self, *sequences):
        return 1

    def _find(self, *sequences):
        subseq = LCSStr()(*sequences)
        length = len(subseq)
        if length == 0:
            return 0
        before = [s[:s.find(subseq)] for s in sequences]
        after = [s[s.find(subseq) + length:] for s in sequences]
        return self._find(*before) + length + self._find(*after)

    def __call__(self, *sequences):
        result = self.quick_answer(*sequences)
        if result is not None:
            return result
        scount = len(sequences)  # sequences count
        ecount = sum(map(len, sequences))  # elements count
        sequences = self._get_sequences(*sequences)
        return scount * self._find(*sequences) / ecount


lcsseq = LCSSeq()
lcsstr = LCSStr()
ratcliff_obershelp = RatcliffObershelp()
