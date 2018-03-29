#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup
import os
import os.path
import json
import sys


def get_extras():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    libs_file = os.path.join(current_dir, 'textdistance', 'libraries.json')
    with open(libs_file, 'r') as f:
        data = json.load(f)
    # get only fastest lib for all algorithms
    return {k: [v[0][0]] for k, v in data.items()}


if 'show_extras' in sys.argv:
    print(json.dumps(get_extras(), indent=2))
    exit()


setup(
    name='textdistance',
    version='2.0.3',

    author='orsinium',
    author_email='master_fess@mail.ru',

    description='Compute distance between the two texts.',
    long_description=open('README.rst').read(),
    keywords='distance between text strings sequences iterators',

    packages=['textdistance', 'textdistance.algorithms'],
    requires=['python (>= 2.7)'],
    extras_require=get_extras(),

    url='https://github.com/orsinium/textdistance',
    download_url='https://github.com/orsinium/textdistance/tarball/master',

    license='GNU Lesser General Public License v3.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    ],
)
