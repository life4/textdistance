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
        self.libs[alg].append(lib)

    def optimize(self):
        with open(LIBRARIES_FILE, 'r') as f:
            libs_data = json.load(f)
        for alg, libs_names in libs_data.items():
            libs = self.get_libs(alg)
            if not libs:
                continue
            self.libs[alg] = [lib for lib in libs if [lib.module_name, lib.func_name] in libs_names]

    def get_algorithms(self):
        return list(self.libs.keys())

    def get_libs(self, alg):
        return self.libs[alg]

    def get_lib(self, obj, *sequences):
        alg = obj.__class__.__name__
        if alg not in self.libs:
            return
        for lib in self.libs[alg]:
            if lib.check_conditions(obj, *sequences) and lib.get_function():
                return lib


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


libraries = LibrariesManager()

libraries.register('DamerauLevenshtein', LibraryBase('abydos.distance', 'damerau_levenshtein'))
libraries.register('DamerauLevenshtein', LibraryBase('pyxdameraulevenshtein', 'damerau_levenshtein_distance'))
libraries.register('DamerauLevenshtein', TextLibrary('jellyfish', 'damerau_levenshtein_distance'))
libraries.register('Hamming', LibraryBase('abydos.distance', 'hamming'))
libraries.register('Hamming', TextLibrary('jellyfish', 'hamming_distance'))
# libraries.register('Hamming', TextLibrary('Levenshtein', 'hamming'))
libraries.register('Jaro', TextLibrary('jellyfish', 'jaro_distance'))
libraries.register('Jaro', TextLibrary('py_stringmatching.similarity_measure.jaro', 'jaro'))
# libraries.register('JaroWinkler', LibraryBase('py_stringmatching.similarity_measure.jaro_winkler', 'jaro_winkler'))
libraries.register('JaroWinkler', TextLibrary('jellyfish', 'jaro_winkler'))
libraries.register('JaroWinkler', TextLibrary('Levenshtein', 'jaro_winkler'))
libraries.register('Levenshtein', LibraryBase('abydos.distance', 'levenshtein'))
libraries.register('Levenshtein', TextLibrary('jellyfish', 'levenshtein_distance'))
libraries.register('Levenshtein', TextLibrary('Levenshtein', 'distance'))
libraries.register('Levenshtein', TextLibrary('py_stringmatching.similarity_measure.levenshtein', 'levenshtein'))


not_optimized_libraries = LibrariesManager()
not_optimized_libraries.libs = deepcopy(libraries.libs)
