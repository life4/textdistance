# built-in
import codecs
import math
from collections import Counter
from fractions import Fraction
from itertools import groupby, permutations

# app
from .base import Base as _Base


try:
    import lzma
except ImportError:
    lzma = None


__all__ = [
    'ArithNCD', 'LZMANCD', 'BZ2NCD', 'RLENCD', 'BWTRLENCD', 'ZLIBNCD',
    'SqrtNCD', 'EntropyNCD',

    'bz2_ncd', 'lzma_ncd', 'arith_ncd', 'rle_ncd', 'bwtrle_ncd', 'zlib_ncd',
    'sqrt_ncd', 'entropy_ncd',
]


try:
    string_types = (str, unicode)
except NameError:
    string_types = (str, )


class _NCDBase(_Base):
    """normalized compression distance (NCD)
    https://en.wikipedia.org/wiki/Normalized_compression_distance#Normalized_compression_distance
    """
    qval = 1

    def __init__(self, qval=1):
        self.qval = qval

    def maximum(self, *sequences):
        return 1

    def _get_size(self, data):
        return len(self._compress(data))

    def __call__(self, *sequences):
        if not sequences:
            return 0
        sequences = self._get_sequences(*sequences)

        concat_length = float('Inf')
        empty = type(sequences[0])()
        for data in permutations(sequences):
            if isinstance(empty, (str, bytes)):
                data = empty.join(data)
            else:
                data = sum(data, empty)
            concat_length = min(concat_length, self._get_size(data))

        compressed_lengths = [self._get_size(s) for s in sequences]
        return float(concat_length - min(compressed_lengths)) / max(compressed_lengths)


class _BinaryNCDBase(_NCDBase):

    def __init__(self):
        pass

    def __call__(self, *sequences):
        if not sequences:
            return 0
        if isinstance(sequences[0], string_types):
            sequences = [s.encode('utf-8') for s in sequences]
        return super(_BinaryNCDBase, self).__call__(*sequences)


class ArithNCD(_NCDBase):
    """Arithmetic coding

    https://github.com/gw-c/arith
    http://www.drdobbs.com/cpp/data-compression-with-arithmetic-encodin/240169251
    https://en.wikipedia.org/wiki/Arithmetic_coding
    """

    def __init__(self, base=2, terminator=None, qval=1):
        self.base = base
        self.terminator = terminator
        self.qval = qval

    def _make_probs(self, *sequences):
        """
        https://github.com/gw-c/arith/blob/master/arith.py
        """
        sequences = self._get_counters(*sequences)
        counts = self._sum_counters(*sequences)
        if self.terminator is not None:
            counts[self.terminator] = 1
        total_letters = sum(counts.values())

        prob_pairs = {}
        cumulative_count = 0
        counts = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
        for char, current_count in counts:
            prob_pairs[char] = (
                Fraction(cumulative_count, total_letters),
                Fraction(current_count, total_letters),
            )
            cumulative_count += current_count
        assert cumulative_count == total_letters
        return prob_pairs

    def _get_range(self, data, probs):
        if self.terminator is not None:
            if self.terminator in data:
                data = data.replace(self.terminator, '')
            data += self.terminator

        start = Fraction(0, 1)
        width = Fraction(1, 1)
        for char in data:
            prob_start, prob_width = probs[char]
            start += prob_start * width
            width *= prob_width
        return start, start + width

    def _compress(self, data):
        probs = self._make_probs(data)
        start, end = self._get_range(data=data, probs=probs)
        output_fraction = Fraction(0, 1)
        output_denominator = 1
        while not (start <= output_fraction < end):
            output_numerator = 1 + ((start.numerator * output_denominator) // start.denominator)
            output_fraction = Fraction(output_numerator, output_denominator)
            output_denominator *= 2
        return output_fraction

    def _get_size(self, data):
        numerator = self._compress(data).numerator
        return math.ceil(math.log(numerator, self.base))


class RLENCD(_NCDBase):
    """Run-length encoding

    https://en.wikipedia.org/wiki/Run-length_encoding
    """

    def _compress(self, data):
        new_data = []
        for k, g in groupby(data):
            n = len(list(g))
            if n > 2:
                new_data.append(str(n) + k)
            elif n == 1:
                new_data.append(k)
            else:
                new_data.append(2 * k)
        return ''.join(new_data)


class BZ2NCD(_BinaryNCDBase):
    def _compress(self, data):
        return codecs.encode(data, 'bz2_codec')[15:]


class LZMANCD(_BinaryNCDBase):
    def _compress(self, data):
        if not lzma:
            raise ImportError('Please, install the PylibLZMA module')
        return lzma.compress(data)[14:]


class ZLIBNCD(_BinaryNCDBase):
    def _compress(self, data):
        return codecs.encode(data, 'zlib_codec')[2:]


class BWTRLENCD(RLENCD):
    def __init__(self, terminator='\0'):
        self.terminator = terminator

    def _compress(self, data):
        if not data:
            data = self.terminator
        elif self.terminator not in data:
            data += self.terminator
            modified = sorted(data[i:] + data[:i] for i in range(len(data)))
            data = ''.join([subdata[-1] for subdata in modified])
        return super(BWTRLENCD, self)._compress(data)


class SqrtNCD(_NCDBase):
    def __init__(self, qval=1):
        self.qval = qval

    def _compress(self, data):
        counter = Counter(self._get_sequences(data)[0])
        return {element: math.sqrt(count) for element, count in counter.items()}

    def _get_size(self, data):
        return sum(self._compress(data).values())


class EntropyNCD(_NCDBase):
    """
    https://en.wikipedia.org/wiki/Redundancy_(information_theory)
    """
    def __init__(self, qval=1):
        self.qval = qval

    def _compress(self, data):
        counter = Counter(self._get_sequences(data)[0])
        total_count = len(data)
        entropy = 0.0
        for element_count in counter.values():
            p = element_count / total_count
            entropy -= p * math.log(p, 2)
        assert entropy >= 0
        return entropy

        # # redundancy:
        # unique_count = len(counter)
        # absolute_entropy = math.log(unique_count, 2) / unique_count
        # return absolute_entropy - entropy / unique_count

    def _get_size(self, data):
        return 1 + self._compress(data)


arith_ncd = ArithNCD()
bwtrle_ncd = BWTRLENCD()
bz2_ncd = BZ2NCD()
lzma_ncd = LZMANCD()
rle_ncd = RLENCD()
zlib_ncd = ZLIBNCD()
sqrt_ncd = SqrtNCD()
entropy_ncd = EntropyNCD()
