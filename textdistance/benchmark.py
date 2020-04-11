# built-in
import json
from collections import defaultdict, namedtuple
from timeit import timeit

# external
from tabulate import tabulate

# app
from .libraries import LIBRARIES_FILE, prototype


# python3 -m textdistance.benchmark


libraries = prototype.clone()
Lib = namedtuple('Lib', ['algorithm', 'library', 'function', 'time', 'presets'])


EXTERNAL_SETUP = """
from {library} import {function} as func
presets = {presets}
if presets:
    func = func(presets)
"""

INTERNAL_SETUP = """
from textdistance import {} as cls
func = cls(external=False)
"""

STMT = """
func('text', 'test')
func('qwer', 'asdf')
func('a' * 15, 'b' * 15)
"""

RUNS = 2000


class Benchmark:
    @staticmethod
    def get_installed():
        for alg in libraries.get_algorithms():
            for lib in libraries.get_libs(alg):
                # try load function
                if not lib.get_function():
                    continue
                # return library info
                yield Lib(
                    algorithm=alg,
                    library=lib.module_name,
                    function=lib.func_name,
                    time=float('Inf'),
                    presets=lib.presets,
                )

    @staticmethod
    def get_external_benchmark(installed):
        for lib in installed:
            yield lib._replace(time=timeit(
                stmt=STMT,
                setup=EXTERNAL_SETUP.format(**lib._asdict()),
                number=RUNS,
            ))

    @staticmethod
    def get_internal_benchmark():
        for alg in libraries.get_algorithms():
            yield Lib(
                algorithm=alg,
                library='**textdistance**',
                function=alg,
                time=timeit(
                    stmt=STMT,
                    setup=INTERNAL_SETUP.format(alg),
                    number=RUNS,
                ),
                presets=None,
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
            tablefmt='orgtbl',
        )
        table += '\nTotal: {} libs.\n\n'.format(len(data))
        return table

    @staticmethod
    def save(libs):
        data = defaultdict(list)
        for lib in libs:
            data[lib.algorithm].append([lib.library, lib.function])
        with open(LIBRARIES_FILE, 'w') as f:
            json.dump(obj=data, fp=f, indent=2, sort_keys=True)

    @classmethod
    def run(cls):
        print('# Installed libraries:\n')
        installed = list(cls.get_installed())
        installed.sort()
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
