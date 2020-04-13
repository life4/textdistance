# built-in
from collections import defaultdict
from itertools import groupby

# app
from .base import Base as _Base, BaseSimilarity as _BaseSimilarity


try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest
try:
    import numpy
except ImportError:
    numpy = None


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
    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.14.3856&rep=rep1&type=pdf
    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.18.2138&rep=rep1&type=pdf
    https://github.com/chrislit/blob/master/abydos/distance/_editex.py
    https://habr.com/ru/post/331174/ (RUS)
    """
    groups = (
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
    ungrouped = frozenset('HW')  # all letters in alphabet that not presented in `grouped`

    def __init__(self, local=False, match_cost=0, group_cost=1, mismatch_cost=2,
                 groups=None, ungrouped=None, external=True):
        self.match_cost = match_cost
        self.group_cost = group_cost
        self.mismatch_cost = mismatch_cost
        self.local = local
        self.external = external

        if groups is not None:
            if ungrouped is None:
                raise ValueError('`ungrouped` argument required with `groups`')
            self.groups = groups
            self.ungrouped = ungrouped
        self.grouped = frozenset.union(*self.groups)

        # backward compat
        if hasattr(self, 'letter_groups'):
            self.groups = self.letter_groups

    def maximum(self, *sequences):
        return max(map(len, sequences)) * self.mismatch_cost

    def r_cost(self, *elements):
        if self._ident(*elements):
            return self.match_cost
        if any(map(lambda x: x not in self.grouped, elements)):
            return self.mismatch_cost
        for group in self.groups:
            if all(map(lambda x: x in group, elements)):
                return self.group_cost
        return self.mismatch_cost

    def d_cost(self, *elements):
        if not self._ident(*elements) and elements[0] in self.ungrouped:
            return self.group_cost
        return self.r_cost(*elements)

    def __call__(self, s1, s2):
        result = self.quick_answer(s1, s2)
        if result is not None:
            return result

        # must do `upper` before getting length because some one-char lowercase glyphs
        # are represented as two chars in uppercase.
        s1 = ' ' + s1.upper()
        s2 = ' ' + s2.upper()
        len_s1 = len(s1) - 1
        len_s2 = len(s2) - 1
        if numpy:
            d_mat = numpy.zeros((len_s1 + 1, len_s2 + 1), dtype=numpy.int)
        else:
            d_mat = defaultdict(lambda: defaultdict(int))

        if not self.local:
            for i in range(1, len_s1 + 1):
                d_mat[i][0] = d_mat[i - 1][0] + self.d_cost(s1[i - 1], s1[i])
        for j in range(1, len_s2 + 1):
            d_mat[0][j] = d_mat[0][j - 1] + self.d_cost(s2[j - 1], s2[j])

        for i, (cs1_prev, cs1_curr) in enumerate(zip(s1, s1[1:]), start=1):
            for j, (cs2_prev, cs2_curr) in enumerate(zip(s2, s2[1:]), start=1):
                d_mat[i][j] = min(
                    d_mat[i - 1][j] + self.d_cost(cs1_prev, cs1_curr),
                    d_mat[i][j - 1] + self.d_cost(cs2_prev, cs2_curr),
                    d_mat[i - 1][j - 1] + self.r_cost(cs1_curr, cs2_curr),
                )

        return d_mat[len_s1][len_s2]


mra = MRA()
editex = Editex()
