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
        # common
        'abydos',
        'jellyfish',
        'numpy',
        'python-Levenshtein',
        'pyxDamerauLevenshtein',
        # slow
        'distance',
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
        'jellyfish',            # only text
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
    long_description = open('README.md', encoding='utf-8').read()
except TypeError:
    try:
        long_description = open('README.md').read()
    except UnicodeDecodeError:
        long_description = ''


setup(
    name='textdistance',
    version='4.2.2',

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
