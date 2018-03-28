import importlib
from collections import namedtuple

from tabulate import tabulate

from .constants import LIBRARIES_FILE
from .labraries import LIBRARIES

Lib = namedtuple('Lib', ['algorithm', 'library', 'function', 'object'])


def _silent_import(module):
    path, _, cls = module.rpartition('.')
    module = importlib.import_module(path)
    return getattr(module, cls, None)


def _get_installed():
    for alg, paths in LIBRARIES.items():
        for path in paths:
            module_name, _, func_name = path.rpartition('.')
            try:
                module = importlib.import_module(module_name)
            except ImportError:
                print(module_name)
                continue
            yield Lib(
                algorithm=alg,
                library=module_name,
                function=func_name,
                object=getattr(module, func_name),
            )

def _get_benchmark(installed):
    pass


def benchmark():
    installed = list(_get_installed())
    print('# Installed libraries:\n')
    print(tabulate(
        [tuple(i[:-1]) for i in installed],
        headers=['algorithm', 'library', 'function'],
    ))
    print('Total: {} libs.\n\n'.format(len(installed)))


if __name__ == '__main__':
    benchmark()
