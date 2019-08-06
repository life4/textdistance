#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# external
from setuptools import setup


extras = {
    # enough for simple usage
    'extras': [
        'abydos',
        'jellyfish',                # for DamerauLevenshtein
        'numpy',                    # for SmithWaterman and other
        'python-Levenshtein',       # for Jaro and Levenshtein
        'pyxDamerauLevenshtein',    # for DamerauLevenshtein
    ],
    # needed for benchmarking, optimization and testing
    'benchmark': [
        'abydos',                   # from common
        'jellyfish',                # from common
        'numpy',                    # from common
        'py_stringmatching',        # maybe will be faster on your system :)
        'python-Levenshtein',       # from common
        'pyxDamerauLevenshtein',    # from common
        'tabulate',                 # for benchmark's tables
    ],
    # for algos, from fastest to slowest, only faster than textdistance:
    'DamerauLevenshtein': [
        'jellyfish',                # only for text
        'pyxDamerauLevenshtein',    # for any iterators
    ],
    'Hamming': [
        'python-Levenshtein',   # only same length and strings
        'jellyfish',            # only strings, any length
        'distance',             # only same length, any iterators
        'abydos',               # any iterators
    ],
    'Jaro': [
        'python-Levenshtein',   # only text
    ],
    'JaroWinkler': [
        'python-Levenshtein',   # only text
    ],
    'Levenshtein': [
        'python-Levenshtein',   # only text
        # yeah, other libs slower than textdistance
    ],
}

# backward compatibility
extras['common'] = extras['extras']
extras['all'] = extras['benchmark']

# correct possible misspelling
extras['extra'] = extras['extras']
extras['benchmarks'] = extras['benchmark']


try:
    long_description = open('README.rst', encoding='utf-8').read()
except TypeError:
    try:
        long_description = open('README.rst').read()
    except UnicodeDecodeError:
        long_description = ''


setup(
    name='textdistance',
    version='4.1.4',

    author='orsinium',
    author_email='master_fess@mail.ru',

    description='Compute distance between the two texts.',
    long_description=long_description,
    keywords='distance between text strings sequences iterators',

    packages=['textdistance', 'textdistance.algorithms'],
    package_data={'': ['*.json']},
    python_requires='>=2.7',
    extras_require=extras,

    url='https://github.com/orsinium/textdistance',
    download_url='https://github.com/orsinium/textdistance/tarball/master',

    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    ],
)
