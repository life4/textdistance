import codecs
from functools import partial
from itertools import groupby, permutations

try:
    import lzma
except ImportError:
    lzma = None

from .base import Base as _Base


__all__ = [
    'bz2_ncd', 'lzma_ncd', 'arith_ncd',
    'rle_ncd', 'bwtrle_ncd', 'zlib_ncd',
]


try:
    string_types = (str, unicode)
except NameError:
    string_types = (str, )


class NCD(_Base):
    """normalized compression distance (NCD)
    https://en.wikipedia.org/wiki/Normalized_compression_distance#Normalized_compression_distance
    """
    qval = 1

    def __init__(self, compressor='bz2', probs=None, bwt_terminator='\0'):
        self.compressor = compressor
        self.probs = probs
        self.bwt_terminator = bwt_terminator

    def maximum(self, *sequences):
        return 1

    def _bz2(self, data):
        return codecs.encode(data, 'bz2_codec')[15:]

    def _lzma(self, data):
        if not lzma:
            raise ImportError('Please, install the PylibLZMA module')
        return lzma.compress(data)[14:]

    def make_probs(self, *sequences):
        sequences = self._get_counters(*sequences)
        counts = self._intersect_counters(sequences)
        counts['\x00'] = 1
        total_letters = sum(counts.values())

        total = 0
        prob_range = {}
        prev = 0.0
        counts = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
        for char, count in counts:
            current = float(total + count) / total_letters
            prob_range[char] = (prev, current)
            prev = current
            total = total + count

        assert total == total_letters
        return prob_range

    def _arith(self, data, probs):
        if '\x00' in data:
            data = data.replace('\x00', ' ')
        minval = 0.0
        maxval = 1.0
        for char in data + '\x00':
            prob_range = probs[char]
            delta = maxval - minval
            minval = minval + prob_range[0] * delta
            maxval = minval + prob_range[1] * delta

        # I tried without the /2 just to check.  Doesn't work.
        # Keep scaling up until the error range is >= 1.  That
        # gives me the minimum number of bits needed to resolve
        # down to the end-of-data character.
        delta = (maxval - minval) / 2
        nbits = 0
        while delta < 1:
            nbits = nbits + 1
            delta <<= 1
        return nbits

    def _rle(self, data):
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

    def _bwtrle(self, data):
        if not data:
            data = self.bwt_terminator
        elif self.bwt_terminator not in data:
            data += self.bwt_terminator
            modified = sorted(data[i:] + data[:i] for i in range(len(data)))
            data = ''.join([subdata[-1] for subdata in modified])
        return self._rle(data)

    def _zlib(self, data):
        return codecs.encode(data, 'zlib_codec')[2:]

    def __call__(self, *sequences):
        if not sequences:
            return 0

        empty = b''
        if isinstance(sequences[0], string_types):
            if self.compressor in ('arith', 'rle', 'bwtrle'):
                empty = ''
            else:
                sequences = [s.encode('utf-8') for s in sequences]
        
        if self.compressor == 'arith':
            if self.probs:
                probs = self.probs
            else:
                probs = self.make_probs(*sequences)
            compressor = partial(self._arith, probs=probs)
        else:
            try:
                compressor = getattr(self, '_' + self.compressor)
            except AttributeError:
                raise KeyError('Invalid compressor')

        compressed_lengths = [len(compressor(s)) for s in sequences]
        concat_length = float('Inf')
        for data in permutations(sequences):
            data = empty.join(data)
            concat_length = min(concat_length, len(compressor(data)))
        return float(concat_length - min(compressed_lengths)) / max(compressed_lengths)


bz2_ncd = NCD(compressor='bz2')
lzma_ncd = NCD(compressor='lzma')
arith_ncd = NCD(compressor='arith')
rle_ncd = NCD(compressor='rle')
bwtrle_ncd = NCD(compressor='bwtrle')
zlib_ncd = NCD(compressor='zlib')
