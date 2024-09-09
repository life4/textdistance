#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# external
from setuptools import setup


extras = {
    # enough for simple usage
    'extras': [
        'jellyfish',                # for DamerauLevenshtein
        'numpy',                    # for SmithWaterman and other
        'Levenshtein',              # for Jaro and Levenshtein
        'pyxDamerauLevenshtein',    # for DamerauLevenshtein
        'rapidfuzz>=2.6.0',         # for Jaro, Levenshtein and other
    ],

    # needed for benchmarking, optimization and testing
    'benchmark': [
        # common
        'jellyfish',
        'numpy',
        'Levenshtein',
        'pyxDamerauLevenshtein',
        'rapidfuzz>=2.6.0',
        # slow
        'pylev',
        'py_stringmatching',
        # other
        'tabulate',     # to draw the table with results
    ],
    'test': [
        'hypothesis',
        'isort',
        'numpy',
        'pytest',
    ],
    'lint': [
        'twine',
        'mypy',
        'isort',
        'flake8',
        'types-tabulate',

        # flake8 plugins
        'flake8-blind-except',
        'flake8-bugbear',
        'flake8-commas',
        'flake8-logging-format',
        'flake8-mutable',
        'flake8-pep3101',
        'flake8-quotes',
        'flake8-string-format',
        'flake8-tidy-imports',
        'pep8-naming',
    ],

    # for algos, from fastest to slowest, only faster than textdistance:
    'DamerauLevenshtein': [
        'rapidfuzz>=2.6.0',         # any iterators of hashable elements
        'jellyfish',                # only for text
        'pyxDamerauLevenshtein',    # for any iterators
    ],
    'Hamming': [
        'Levenshtein',          # only same length and strings
        'rapidfuzz>=2.6.0',     # only same length, any iterators of hashable elements
        'jellyfish',            # only strings, any length
    ],
    'Jaro': [
        'rapidfuzz>=2.6.0',     # any iterators of hashable elements
        'Levenshtein',          # only text
    ],
    'JaroWinkler': [
        'rapidfuzz>=2.6.0',     # any iterators of hashable elements
        'jellyfish',            # only text
    ],
    'Levenshtein': [
        'rapidfuzz>=2.6.0',     # any iterators of hashable elements
        'Levenshtein',          # only text
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
    long_description = open('README.md', encoding='utf-8').read()
except TypeError:
    try:
        long_description = open('README.md').read()
    except UnicodeDecodeError:
        long_description = ''


setup(
    name='textdistance',
    version='4.6.3',

    author='orsinium',
    author_email='gram@orsinium.dev',

    description='Compute distance between the two texts.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='distance between text strings sequences iterators',

    packages=['textdistance', 'textdistance.algorithms'],
    package_data={'': ['*.json']},
    python_requires='>=3.5',
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
