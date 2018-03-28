from importlib import import_module
from collections import namedtuple, defaultdict
from timeit import timeit
import json

from tabulate import tabulate

from . import algorithms as textdistance
from .constants import LIBRARIES_FILE
from .libraries import LIBRARIES


# python3 -m textdistance.benchmark


Lib = namedtuple('Lib', ['algorithm', 'library', 'function', 'time', 'object'])


class Benchmark(object):
    @staticmethod
    def get_installed():
        for alg, paths in LIBRARIES.items():
            for path in paths:
                module_name, _, func_name = path.rpartition('.')
                try:
                    module = import_module(module_name)
                except ImportError:
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

    @staticmethod
    def filter_benchmark(external, internal):
        limits = {i.algorithm: i.time for i in internal}
        return filter(lambda x: x.time < limits[x.algorithm], external)

    @staticmethod
    def get_table(data):
        table = tabulate(
            [tuple(i[:-1]) for i in data],
            headers=['algorithm', 'library', 'function', 'time'],
        )
        table += '\nTotal: {} libs.\n\n'.format(len(data))
        return table

    @staticmethod
    def save(libs):
        data = defaultdict(list)
        for lib in libs:
            data[lib.algorithm].append('{}.{}'.format(lib.library, lib.function))
        with open(LIBRARIES_FILE, 'w') as f:
            json.dump(obj=data, fp=f, indent=2, sort_keys=True)

    @classmethod
    def run(cls):
        print('# Installed libraries:\n')
        installed = list(cls.get_installed())
        print(cls.get_table(installed))

        print('# Benchmarks (with textdistance):\n')
        benchmark = list(cls.get_external_benchmark(installed))
        benchmark_internal = list(cls.get_internal_benchmark())
        benchmark += benchmark_internal
        benchmark.sort(key=lambda x: (x.algorithm, x.time))
        print(cls.get_table(benchmark))

        print('# Faster than textdistance:\n')
        benchmark = list(cls.filter_benchmark(benchmark, benchmark_internal))
        print(cls.get_table(benchmark))

        cls.save(benchmark)


if __name__ == '__main__':
    Benchmark.run()
