import importlib
from collections import namedtuple
from timeit import timeit

from tabulate import tabulate

from . import algorithms as textdistance
from .constants import LIBRARIES_FILE
from .labraries import LIBRARIES


# python3 -m textdistance.benchmark


Lib = namedtuple('Lib', ['algorithm', 'library', 'function', 'time', 'object'])


class Benchmark(object):
    @staticmethod
    def get_installed():
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
                    time=float('Inf'),
                    object=getattr(module, func_name),
                )

    @staticmethod
    def get_external_benchmark(installed):
        for lib in installed:
            yield lib._replace(time=timeit(
                stmt="func('text', 'testit')",
                setup="from {} import {} as func".format(lib.library, lib.function),
                number=10000,
            ))

    @staticmethod
    def get_internal_benchmark():
        for alg in LIBRARIES:
            yield Lib(
                algorithm=alg,
                library='textdistance',
                function=alg,
                time=timeit(
                    stmt="func('text', 'testit')",
                    setup="from textdistance import {} as func".format(alg),
                    number=10000,
                ),
                object=getattr(textdistance, alg),
            )

    @classmethod
    def run(cls):
        print('# Installed libraries:\n')
        installed = list(cls.get_installed())
        print(tabulate(
            [tuple(i[:-2]) for i in installed],
            headers=['algorithm', 'library', 'function'],
        ))
        print('Total: {} libs.\n\n'.format(len(installed)))

        print('# Benchmarks:\n')
        benchmark = list(cls.get_external_benchmark(installed))
        benchmark += list(cls.get_internal_benchmark())
        print(tabulate(
            [tuple(i[:-1]) for i in benchmark],
            headers=['algorithm', 'library', 'function', 'time'],
        ))
        print('Total: {} libs.\n\n'.format(len(benchmark)))


if __name__ == '__main__':
    Benchmark.run()
