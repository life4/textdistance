from collections import defaultdict
from importlib import import_module


class LibrariesManager(object):
    def __init__(self):
        self.libs = defaultdict(list)

    def register(self, alg, lib):
        self.libs[alg].append(lib)

    def get_algorithms(self):
        return list(self.libs.keys())

    def get_libs(self, alg):
        return self.libs[alg]

    def get_lib(self, obj):
        alg = obj.__class__.__name__
        for lib in self.libs[alg]:
            if lib.check_conditions(obj) and lib.get_function():
                return lib

    def get_function(self, obj):
        lib = self.get_lib(obj)
        if lib:
            return lib.func


class LibraryBase(object):
    func = NotImplemented

    def __init__(self, module_name, func_name, presets=None, conditions=None):
        self.module_name = module_name
        self.func_name = func_name
        self.presets = presets
        self.conditions = conditions

    def check_conditions(self, obj):
        if not self.conditions:
            return True
        for name, value in self.conditions.items():
            if getattr(obj, name) != value:
                return False
        return True

    def get_function(self):
        if self.func is NotImplemented:
            # import module
            try:
                module = import_module(self.module_name)
            except ImportError:
                return

            # get object from module
            obj = getattr(module, self.func_name)

            # init class
            if obj is not None and self.presets is not None:
                self.func = obj(**self.presets)
            else:
                self.func = obj

        return self.func


libraries = LibrariesManager()

libraries.register('DamerauLevenshtein', LibraryBase('abydos.distance', 'damerau_levenshtein'))
libraries.register('DamerauLevenshtein', LibraryBase('jellyfish', 'damerau_levenshtein_distance'))
libraries.register('DamerauLevenshtein', LibraryBase('pyxdameraulevenshtein', 'damerau_levenshtein_distance'))
libraries.register('Hamming', LibraryBase('abydos.distance', 'hamming'))
libraries.register('Hamming', LibraryBase('jellyfish', 'hamming_distance'))
libraries.register('JaroWinkler', LibraryBase('jellyfish', 'jaro_distance', conditions=dict(winklerize=False)))
libraries.register('JaroWinkler', LibraryBase('jellyfish', 'jaro_winkler'))
# libraries.register('JaroWinkler', LibraryBase('py_stringmatching.similarity_measure.jaro_winkler', 'jaro_winkler'))
libraries.register('JaroWinkler', LibraryBase('py_stringmatching.similarity_measure.jaro', 'jaro', conditions=dict(winklerize=False)))  # noQA
libraries.register('Levenshtein', LibraryBase('abydos.distance', 'levenshtein'))
libraries.register('Levenshtein', LibraryBase('jellyfish', 'levenshtein_distance'))
libraries.register('Levenshtein', LibraryBase('py_stringmatching.similarity_measure.levenshtein', 'levenshtein'))
