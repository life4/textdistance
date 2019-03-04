# built-in
import json
import os
import os.path
from collections import defaultdict
from copy import deepcopy
from importlib import import_module


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
LIBRARIES_FILE = os.path.join(CURRENT_DIR, 'libraries.json')


class LibrariesManager(object):
    def __init__(self):
        self.libs = defaultdict(list)

    def register(self, alg, lib):
        """Register new lib
        """
        self.libs[alg].append(lib)

    def optimize(self):
        """Sort algorithm implementations by speed.
        """
        # load benchmarks results
        with open(LIBRARIES_FILE, 'r') as f:
            libs_data = json.load(f)
        # optimize
        for alg, libs_names in libs_data.items():
            libs = self.get_libs(alg)
            if not libs:
                continue
            # drop slow libs
            self.libs[alg] = [lib for lib in libs if [lib.module_name, lib.func_name] in libs_names]
            # sort libs by speed
            self.libs[alg].sort(key=lambda lib: libs_names.index([lib.module_name, lib.func_name]))

    def get_algorithms(self):
        """Get list of available algorithms.
        """
        return list(self.libs.keys())

    def get_libs(self, alg):
        """Get libs list for algorithm
        """
        if alg not in self.libs:
            return []
        return self.libs[alg]

    def clone(self):
        """Clone library manager prototype
        """
        obj = self.__class__()
        obj.libs = deepcopy(self.libs)
        return obj


class LibraryBase(object):
    func = NotImplemented

    def __init__(self, module_name, func_name, attr=None, presets=None, conditions=None):
        self.module_name = module_name
        self.func_name = func_name
        self.presets = presets
        self.conditions = conditions
        self.attr = attr

    def check_conditions(self, obj, *sequences):
        # external libs can compare only 2 strings
        if len(sequences) != 2:
            return False
        if not self.conditions:
            return True
        for name, value in self.conditions.items():
            if getattr(obj, name) != value:
                return False

        return True

    def prepare(self, *sequences):
        return sequences

    def get_function(self):
        if self.func is NotImplemented:
            # import module
            try:
                module = import_module(self.module_name)
            except ImportError:
                self.func = None
                return

            # get object from module
            obj = getattr(module, self.func_name)
            # init class
            if self.presets is not None:
                obj = obj(**self.presets)
            # get needed attribute
            if self.attr:
                obj = getattr(obj, self.attr)
            self.func = obj

        return self.func


class TextLibrary(LibraryBase):
    def check_conditions(self, obj, *sequences):
        if not super(TextLibrary, self).check_conditions(obj, *sequences):
            return False
        # compare only by letters
        if getattr(obj, 'qval', 0) != 1:
            return False
        return True

    def prepare(self, *sequences):
        # convert list of letters to string
        if isinstance(sequences[0], (tuple, list)):
            sequences = list(map(lambda x: u''.join(x), sequences))

        # convert to unicode for python2
        try:
            sequences = list(map(unicode, sequences))
        except NameError:
            pass

        return sequences


class SameLengthLibrary(LibraryBase):
    def check_conditions(self, obj, *sequences):
        if not super(SameLengthLibrary, self).check_conditions(obj, *sequences):
            return False
        # compare only same length iterators
        if min(map(len, sequences)) != max(map(len, sequences)):
            return False
        return True


class SameLengthTextLibrary(SameLengthLibrary, TextLibrary):
    pass


prototype = LibrariesManager()

prototype.register('DamerauLevenshtein', LibraryBase('abydos.distance', 'damerau_levenshtein'))
prototype.register('DamerauLevenshtein', LibraryBase('pylev', 'damerau_levenshtein'))
prototype.register('DamerauLevenshtein', LibraryBase('pyxdameraulevenshtein', 'damerau_levenshtein_distance'))
prototype.register('DamerauLevenshtein', TextLibrary('jellyfish', 'damerau_levenshtein_distance'))

prototype.register('Hamming', LibraryBase('abydos.distance', 'hamming'))
prototype.register('Hamming', SameLengthLibrary('distance', 'hamming'))
prototype.register('Hamming', SameLengthTextLibrary('Levenshtein', 'hamming'))
prototype.register('Hamming', TextLibrary('jellyfish', 'hamming_distance'))

prototype.register('Jaro', TextLibrary('jellyfish', 'jaro_distance'))
prototype.register('Jaro', TextLibrary('Levenshtein', 'jaro'))
prototype.register('Jaro', TextLibrary('py_stringmatching.similarity_measure.jaro', 'jaro'))

# libraries.register('JaroWinkler', LibraryBase('py_stringmatching.similarity_measure.jaro_winkler', 'jaro_winkler'))
prototype.register('JaroWinkler', TextLibrary('jellyfish', 'jaro_winkler', conditions=dict(winklerize=True)))
prototype.register('JaroWinkler', TextLibrary('Levenshtein', 'jaro_winkler', conditions=dict(winklerize=True)))

prototype.register('Levenshtein', LibraryBase('abydos.distance', 'levenshtein'))
prototype.register('Levenshtein', LibraryBase('distance', 'levenshtein'))
prototype.register('Levenshtein', LibraryBase('pylev', 'levenshtein'))
prototype.register('Levenshtein', TextLibrary('jellyfish', 'levenshtein_distance'))
prototype.register('Levenshtein', TextLibrary('Levenshtein', 'distance'))
prototype.register('Levenshtein', TextLibrary('py_stringmatching.similarity_measure.levenshtein', 'levenshtein'))
