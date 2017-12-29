
# python3
try:
    from functools import reduce
except ImportError:
    pass


class Base(object):
    def __call__(self, *sequences):
        raise NotImplementedError

    def maximum(self, *sequences):
        return max(map(len, sequences))

    def distance(self, *sequences):
        return self(*sequences)

    def similarity(self, *sequences):
        return self.maximum(*sequences) - self.distance(*sequences)

    def normalized_distance(self, *sequences):
        return self.distance(*sequences) / self.maximum(*sequences)

    def normalized_similarity(self, *sequences):
        return 1 - self.normalized_distance(*sequences)

    def _ident(self, *sequences):
        return reduce(lambda s1, s2: s1 == s2, sequences)
