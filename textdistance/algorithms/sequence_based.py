from __future__ import annotations

# built-in
from difflib import SequenceMatcher as _SequenceMatcher
from typing import Any

# app
from ..utils import find_ngrams
from .base import BaseSimilarity as _BaseSimilarity
from .types import TestFunc


try:
    # external
    import numpy
except ImportError:
    # built-in
    from array import array
    numpy = None  # type: ignore[assignment]


__all__ = [
    'lcsseq', 'lcsstr', 'ratcliff_obershelp',
    'LCSSeq', 'LCSStr', 'RatcliffObershelp',
]


class LCSSeq(_BaseSimilarity):
    """longest common subsequence similarity

    https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    """

    def __init__(
        self,
        qval: int = 1,
        test_func: TestFunc = None,
        external: bool = True,
    ) -> None:
        self.qval = qval
        self.test_func = test_func or self._ident
        self.external = external

    def _dynamic(self, seq1: str, seq2: str) -> str:
        """
        https://github.com/chrislit/abydos/blob/master/abydos/distance/_lcsseq.py
        http://www.dis.uniroma1.it/~bonifaci/algo/LCSSEQ.py
        http://rosettacode.org/wiki/Longest_common_subsequence#Dynamic_Programming_8
        """
        lengths: Any
        if numpy:
            lengths = numpy.zeros((len(seq1) + 1, len(seq2) + 1), dtype=int)
        else:
            lengths = [array('L', [0] * (len(seq2) + 1)) for _ in range(len(seq1) + 1)]

        # row 0 and column 0 are initialized to 0 already
        for i, char1 in enumerate(seq1):
            for j, char2 in enumerate(seq2):
                if char1 == char2:
                    lengths[i + 1][j + 1] = lengths[i][j] + 1
                else:
                    lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

        # read the substring out from the matrix
        result = ''
        i, j = len(seq1), len(seq2)
        while i != 0 and j != 0:
            if lengths[i][j] == lengths[i - 1][j]:
                i -= 1
            elif lengths[i][j] == lengths[i][j - 1]:
                j -= 1
            else:
                assert seq1[i - 1] == seq2[j - 1]
                result = seq1[i - 1] + result
                i -= 1
                j -= 1
        return result

    def _recursive(self, *sequences: str) -> str:
        if not all(sequences):
            return type(sequences[0])()  # empty sequence
        if self.test_func(*[s[-1] for s in sequences]):
            c = sequences[0][-1]
            sequences = tuple(s[:-1] for s in sequences)
            return self(*sequences) + c
        m = type(sequences[0])()  # empty sequence
        for i, s in enumerate(sequences):
            ss = sequences[:i] + (s[:-1], ) + sequences[i + 1:]
            m = max([self(*ss), m], key=len)
        return m

    def __call__(self, *sequences: str) -> str:
        if not sequences:
            return ''
        sequences = self._get_sequences(*sequences)
        if len(sequences) == 2:
            return self._dynamic(*sequences)
        else:
            return self._recursive(*sequences)

    def similarity(self, *sequences) -> int:
        return len(self(*sequences))


class LCSStr(_BaseSimilarity):
    """longest common substring similarity
    """

    def _standart(self, s1: str, s2: str) -> str:
        matcher = _SequenceMatcher(a=s1, b=s2)
        match = matcher.find_longest_match(0, len(s1), 0, len(s2))
        return s1[match.a: match.a + match.size]

    def _custom(self, *sequences: str) -> str:
        short = min(sequences, key=len)
        length = len(short)
        for n in range(length, 0, -1):
            for subseq in find_ngrams(short, n):
                joined = ''.join(subseq)
                for seq in sequences:
                    if joined not in seq:
                        break
                else:
                    return joined
        return type(short)()  # empty sequence

    def __call__(self, *sequences: str) -> str:
        if not all(sequences):
            return ''
        length = len(sequences)
        if length == 0:
            return ''
        if length == 1:
            return sequences[0]

        sequences = self._get_sequences(*sequences)
        if length == 2 and max(map(len, sequences)) < 200:
            return self._standart(*sequences)
        return self._custom(*sequences)

    def similarity(self, *sequences: str) -> int:
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

    https://en.wikipedia.org/wiki/Gestalt_Pattern_Matching
    https://github.com/Yomguithereal/talisman/blob/master/src/metrics/ratcliff-obershelp.js
    https://xlinux.nist.gov/dads/HTML/ratcliffObershelp.html
    """

    def maximum(self, *sequences: str) -> int:
        return 1

    @staticmethod
    def _find_subsequence(sequence, subsequence):
        if isinstance(sequence, str) and isinstance(subsequence, str):
            return sequence.find(subsequence)
        if isinstance(sequence, bytes) and isinstance(subsequence, bytes):
            return sequence.find(subsequence)
        length = len(subsequence)
        for start in range(len(sequence) - length + 1):
            if all(sequence[start + i] == item for i, item in enumerate(subsequence)):
                return start
        return -1

    def _find(self, *sequences: str) -> int:
        text_sequences = all(isinstance(s, str) for s in sequences)
        short_bytes = all(isinstance(s, bytes) for s in sequences)
        if text_sequences or (len(sequences) == 2 and short_bytes and max(map(len, sequences)) < 200):
            subseq = LCSStr()(*sequences)
        elif len(sequences) == 2:
            first, second = sequences
            previous = [0] * (len(second) + 1)
            best_start = best_length = 0
            for i, item in enumerate(first):
                current = [0] * (len(second) + 1)
                for j, other in enumerate(second):
                    if item == other:
                        current[j + 1] = previous[j] + 1
                        if current[j + 1] > best_length:
                            best_length = current[j + 1]
                            best_start = i + 1 - best_length
                previous = current
            subseq = first[best_start:best_start + best_length]
        else:
            short = min(sequences, key=len)
            subseq = short[:0]
            for length in range(len(short), 0, -1):
                for start in range(len(short) - length + 1):
                    candidate = short[start:start + length]
                    if all(self._find_subsequence(s, candidate) >= 0 for s in sequences):
                        subseq = candidate
                        break
                if subseq:
                    break
        length = len(subseq)
        if length == 0:
            return 0
        starts = [self._find_subsequence(s, subseq) for s in sequences]
        before = [s[:start] for s, start in zip(sequences, starts)]
        after = [s[start + length:] for s, start in zip(sequences, starts)]
        return self._find(*before) + length + self._find(*after)

    def __call__(self, *sequences: str) -> float:
        sequences = self._get_sequences(*sequences)
        result = self.quick_answer(*sequences)
        if result is not None:
            return result
        scount = len(sequences)  # sequences count
        ecount = sum(map(len, sequences))  # elements count
        return scount * self._find(*sequences) / ecount


lcsseq = LCSSeq()
lcsstr = LCSStr()
ratcliff_obershelp = RatcliffObershelp()
