#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name     = 'textdistance',
    version  = '2.0.0',

    author       = 'orsinium',
    author_email = 'master_fess@mail.ru',

    description      = 'Compute distance between the two texts.',
    long_description = open('README.rst').read(),
    keywords         = 'distance between text strings sequences iterators',

    packages = ['textdistance'],
    requires = ['python (>= 2.7)'],

    url          = 'https://github.com/orsinium/textdistance',
    download_url = 'https://github.com/orsinium/textdistance/tarball/master',

    license      = 'GNU Lesser General Public License v3.0',
    classifiers  = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    ],
)
