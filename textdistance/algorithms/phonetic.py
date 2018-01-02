# built-in
from itertools import groupby
try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest
# external
try:
    import numpy
except ImportError:
    numpy = None
# project
from .base import Base as _Base, BaseSimilarity as _BaseSimilarity


__all__ = [
    'MRA', 'Editex',
    'mra', 'editex',
]


class MRA(_BaseSimilarity):
    """Western Airlines Surname Match Rating Algorithm comparison rating
    https://en.wikipedia.org/wiki/Match_rating_approach
    https://github.com/Yomguithereal/talisman/blob/master/src/metrics/distance/mra.js
    """

    def maximum(self, *sequences):
        sequences = [list(self._calc_mra(s)) for s in sequences]
        return max(map(len, sequences))

    def _calc_mra(self, word):
        if not word:
            return word
        word = word.upper()
        word = word[0] + ''.join(c for c in word[1:] if c not in 'AEIOU')
        # remove repeats like an UNIX uniq
        word = ''.join(char for char, _ in groupby(word))
        if len(word) > 6:
            return word[:3] + word[-3:]
        return word

    def __call__(self, *sequences):
        if not all(sequences):
            return 0
        sequences = [list(self._calc_mra(s)) for s in sequences]
        lengths = list(map(len, sequences))
        count = len(lengths)
        max_length = max(lengths)
        if abs(max_length - min(lengths)) > count:
            return 0

        for _ in range(count):
            new_sequences = []
            minlen = min(lengths)
            for chars in zip(*sequences):
                if not self._ident(*chars):
                    new_sequences.append(chars)
            #import pdb; pdb.set_trace()
            new_sequences = map(list, zip(*new_sequences))
            # update sequences
            ss = zip_longest(new_sequences, sequences, fillvalue=list())
            sequences = [s1 + s2[minlen:] for s1, s2 in ss]
            # update lengths
            lengths = list(map(len, sequences))

        if not lengths:
            return max_length
        return max_length - max(lengths)


class Editex(_Base):
    """
    https://anhaidgroup.github.io/py_stringmatching/v0.3.x/Editex.html
    """
    letter_groups = (
        frozenset('AEIOUY'),
        frozenset('BP'),
        frozenset('CKQ'),
        frozenset('DT'),
        frozenset('LR'),
        frozenset('MN'),
        frozenset('GJ'),
        frozenset('FPV'),
        frozenset('SXZ'),
        frozenset('CSZ'),
    )
    all_letters = frozenset('AEIOUYBPCKQDTLRMNGJFVSXZ')

    def __init__(self, local=False, match_cost=0, group_cost=1, mismatch_cost=2):
        self.match_cost = match_cost
        self.group_cost = group_cost
        self.mismatch_cost = mismatch_cost
        self.local = local

    def maximum(self, *sequences):
        return max(map(len, sequences)) * self.mismatch_cost

    def r_cost(self, *sequences):
        if self._ident(*sequences):
            return self.match_cost
        if any(map(lambda x: x not in self.all_letters, sequences)):
            return self.mismatch_cost
        for group in self.letter_groups:
            if all(map(lambda x: x in group, sequences)):
                return self.group_cost
        return self.mismatch_cost

    def d_cost(self, *sequences):
        if not self._ident(*sequences) and sequences[0] in 'HW':
            return self.group_cost
        return self.r_cost(*sequences)

    def __call__(self, s1, s2):
        if not numpy:
            raise ImportError('Please, install numpy for Editex measure')
        result = self.quick_answer(s1, s2)
        if result is not None:
            return result

        len_s1 = len(s1)
        len_s2 = len(s2)
        d_mat = numpy.zeros((len_s1 + 1, len_s2 + 1), dtype=numpy.int)
        s1 = ' ' + s1
        s2 = ' ' + s2

        if not self.local:
            for i in range(1, len_s1 + 1):
                d_mat[i, 0] = d_mat[i - 1, 0] + self.d_cost(s1[i - 1], s1[i])
        for j in range(1, len_s2 + 1):
            d_mat[0, j] = d_mat[0, j - 1] + self.d_cost(s2[j - 1], s2[j])

        for i, (cs1_prev, cs1_curr) in enumerate(zip(s1, s1[1:]), start=1):
            for j, (cs2_prev, cs2_curr) in enumerate(zip(s2, s2[1:]), start=1):
                d_mat[i, j] = min(
                    d_mat[i - 1, j] + self.d_cost(cs1_prev, cs1_curr),
                    d_mat[i, j - 1] + self.d_cost(cs2_prev, cs2_curr),
                    d_mat[i - 1, j - 1] + self.r_cost(cs1_curr, cs2_curr),
                )

        return d_mat[len_s1, len_s2]


mra = MRA()
editex = Editex()
