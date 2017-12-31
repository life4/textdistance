from itertools import groupby
try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest
from .base import BaseSimilarity as _BaseSimilarity


class MRA(_BaseSimilarity):
    """Western Airlines Surname Match Rating Algorithm comparison rating
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

mra = MRA()
