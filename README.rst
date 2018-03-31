TextDistance
============

.. figure:: logo.png
   :alt: TextDistance logo

   TextDistance logo

|Build Status| |PyPI version| |Status| |Code size| |License|

**TextDistance** -- python library for compare distance between two or
more sequences by many algorithms.

Features:

-  30+ algorithms
-  Pure python implementation
-  Simple usage
-  More than two sequences comparing
-  Some algorithms have more than one implementation in one class.
-  Optional numpy usage for maximum speed.

Algorithms
----------

Edit based
~~~~~~~~~~

+------------------------------------------------------------------------------------------------+--------------------------+------------------------------+
| Algorithm                                                                                      | Class                    | Functions                    |
+================================================================================================+==========================+==============================+
| `Hamming <https://en.wikipedia.org/wiki/Hamming_distance>`__                                   | ``Hamming``              | ``hamming``                  |
+------------------------------------------------------------------------------------------------+--------------------------+------------------------------+
| `MLIPNS <http://www.sial.iias.spb.su/files/386-386-1-PB.pdf>`__                                | ``Mlipns``               | ``mlipns``                   |
+------------------------------------------------------------------------------------------------+--------------------------+------------------------------+
| `Levenshtein <https://en.wikipedia.org/wiki/Levenshtein_distance>`__                           | ``Levenshtein``          | ``levenshtein``              |
+------------------------------------------------------------------------------------------------+--------------------------+------------------------------+
| `Damerau-Levenshtein <https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance>`__   | ``DamerauLevenshtein``   | ``damerau_levenshtein``      |
+------------------------------------------------------------------------------------------------+--------------------------+------------------------------+
| `Jaro-Winkler <https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance>`__                 | ``JaroWinkler``          | ``jaro_winkler``, ``jaro``   |
+------------------------------------------------------------------------------------------------+--------------------------+------------------------------+
| `Strcmp95 <http://cpansearch.perl.org/src/SCW/Text-JaroWinkler-0.1/strcmp95.c>`__              | ``StrCmp95``             | ``strcmp95``                 |
+------------------------------------------------------------------------------------------------+--------------------------+------------------------------+
| `Needleman-Wunsch <https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm>`__        | ``NeedlemanWunsch``      | ``needleman_wunsch``         |
+------------------------------------------------------------------------------------------------+--------------------------+------------------------------+
| `Gotoh <https://www.cs.umd.edu/class/spring2003/cmsc838t/papers/gotoh1982.pdf>`__              | ``Gotoh``                | ``gotoh``                    |
+------------------------------------------------------------------------------------------------+--------------------------+------------------------------+
| `Smith-Waterman <https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm>`__            | ``SmithWaterman``        | ``smith_waterman``           |
+------------------------------------------------------------------------------------------------+--------------------------+------------------------------+

Token based
~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------+
| Algorithm                                                                                                                 | Class            | Functions                                   |
+===========================================================================================================================+==================+=============================================+
| `Jaccard index <https://en.wikipedia.org/wiki/Jaccard_index>`__                                                           | ``Jaccard``      | ``jaccard``                                 |
+---------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------+
| `Sørensen–Dice coefficient <https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient>`__                      | ``Sorensen``     | ``sorensen``, ``sorensen_dice``, ``dice``   |
+---------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------+
| `Tversky index <https://en.wikipedia.org/wiki/Tversky_index>`__                                                           | ``Tversky``      | ``tversky``                                 |
+---------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------+
| `Overlap coefficient <https://en.wikipedia.org/wiki/Overlap_coefficient>`__                                               | ``Overlap``      | ``overlap``                                 |
+---------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------+
| `Tanimoto distance <https://en.wikipedia.org/wiki/Jaccard_index#Tanimoto_similarity_and_distance>`__                      | ``Tanimoto``     | ``tanimoto``                                |
+---------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------+
| `Cosine similarity <https://en.wikipedia.org/wiki/Cosine_similarity>`__                                                   | ``Cosine``       | ``cosine``                                  |
+---------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------+
| `Monge-Elkan <https://www.academia.edu/200314/Generalized_Monge-Elkan_Method_for_Approximate_Text_String_Comparison>`__   | ``MongeElkan``   | ``monge_elkan``                             |
+---------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------+
| `Bag distance <https://github.com/Yomguithereal/talisman/blob/master/src/metrics/distance/bag.js>`__                      | ``Bag``          | ``bag``                                     |
+---------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------+

Sequence based
~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+--------------------------+
| Algorithm                                                                                                                                     | Class                   | Functions                |
+===============================================================================================================================================+=========================+==========================+
| `longest common subsequence similarity <https://en.wikipedia.org/wiki/Longest_common_subsequence_problem>`__                                  | ``LCSSeq``              | ``lcsseq``               |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+--------------------------+
| `longest common substring similarity <https://docs.python.org/2/library/difflib.html#difflib.SequenceMatcher>`__                              | ``LCSStr``              | ``lcsstr``               |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+--------------------------+
| `Ratcliff-Obershelp similarity <http://collaboration.cmc.ec.gc.ca/science/rpn/biblio/ddj/Website/articles/DDJ/1988/8807/8807c/8807c.htm>`__   | ``RatcliffObershelp``   | ``ratcliff_obershelp``   |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+--------------------------+

Compression based
~~~~~~~~~~~~~~~~~

Work in progress. Now all algorithms compare two strings as array of
bits, not by chars.

``NCD`` - normalized compression distance.

Functions:

1. ``bz2_ncd``
2. ``lzma_ncd``
3. ``arith_ncd``
4. ``rle_ncd``
5. ``bwtrle_ncd``
6. ``zlib_ncd``

Phonetic
~~~~~~~~

+-----------------------------------------------------------------------------------+--------------+--------------+
| Algorithm                                                                         | Class        | Functions    |
+===================================================================================+==============+==============+
| `MRA <https://en.wikipedia.org/wiki/Match_rating_approach>`__                     | ``MRA``      | ``mra``      |
+-----------------------------------------------------------------------------------+--------------+--------------+
| `Editex <https://anhaidgroup.github.io/py_stringmatching/v0.3.x/Editex.html>`__   | ``Editex``   | ``editex``   |
+-----------------------------------------------------------------------------------+--------------+--------------+

Simple
~~~~~~

+-----------------------+----------------+----------------+
| Algorithm             | Class          | Functions      |
+=======================+================+================+
| Prefix similarity     | ``Prefix``     | ``prefix``     |
+-----------------------+----------------+----------------+
| Postfix similarity    | ``Postfix``    | ``postfix``    |
+-----------------------+----------------+----------------+
| Length distance       | ``Length``     | ``length``     |
+-----------------------+----------------+----------------+
| Identity similarity   | ``Identity``   | ``identity``   |
+-----------------------+----------------+----------------+
| Matrix similarity     | ``Matrix``     | ``matrix``     |
+-----------------------+----------------+----------------+

Installation
------------

Stable
~~~~~~

Only pure python implementation:

.. code:: bash

    pip install textdistance

With common side libraries for maximum speed:

.. code:: bash

    pip install textdistance[common]

With all libraries (required for `benchmarking <#benchmarks>`__):

.. code:: bash

    pip install textdistance[all]

With extras only for some algorithm:

.. code:: bash

    pip install textdistance[Hamming]

Algorithms with available extras: ``DamerauLevenshtein``, ``Hamming``,
``Jaro``, ``JaroWinkler``, ``Levenshtein``.

Dev
~~~

Via pip:

.. code:: bash

    pip install -e git+https://github.com/orsinium/textdistance.git#egg=textdistance

Or clone repo and install with some extras:

.. code:: bash

    git clone https://github.com/orsinium/textdistance.git
    pip install -e .[all]

Usage
-----

All algorithms have 2 interfaces:

1. Class with algorithm-specific params for customizing.
2. Class instance with default params for quick and simple usage.

All algorithms have some common methods:

1. ``.distance(*sequences)`` -- calculate distance between sequences.
2. ``.similarity(*sequences)`` -- calculate similarity for sequences.
3. ``.maximum(*sequences)`` -- maximum possible value for distance and
   similarity. For any sequence: ``distance + similarity == maximum``.
4. ``.normalized_distance(*sequences)`` -- normalized distance between
   sequences. The return value is a float between 0 and 1, where 0 means
   equal, and 1 totally different.
5. ``.normalized_similarity(*sequences)`` -- normalized similarity for
   sequences. The return value is a float between 0 and 1, where 0 means
   totally different, and 1 equal.

Most common init arguments:

1. ``qval`` -- q-value for split sequences into q-grams. Possible
   values:

   -  1 (default) -- compare sequences by chars.
   -  2 or more -- transform sequences to q-grams.
   -  None -- split sequences by words.

2. ``as_set`` -- for token-based algorithms:

   -  True -- ``t`` and ``ttt`` is equal.
   -  False (default) -- ``t`` and ``ttt`` is different.

Example
-------

For example, `Hamming
distance <https://en.wikipedia.org/wiki/Hamming_distance>`__:

.. code:: python

    import textdistance

    textdistance.hamming('test', 'text')
    # 1

    textdistance.hamming.distance('test', 'text')
    # 1

    textdistance.hamming.similarity('test', 'text')
    # 3

    textdistance.hamming.normalized_distance('test', 'text')
    # 0.25

    textdistance.hamming.normalized_similarity('test', 'text')
    # 0.75

    textdistance.Hamming(qval=2).distance('test', 'text')
    # 2

Any other algorithms have same interface.

Side libraries
--------------

For main algorithms textdistance try to call known external libraries
(fastest first) if available (installed in your system) and possible
(this implementation can compare this sequences).
`Install <#installation>`__ textdistance with common extras for this
feature.

You can disable this by passing ``external=False`` argument on init:

.. code:: python3

    import textdistance
    hamming = textdistance.Hamming(external=False)
    hamming('text', 'testit')
    # 3

Supported libraries:

1. `abydos <https://github.com/chrislit/abydos>`__
2. `Distance <https://github.com/doukremt/distance>`__
3. `jellyfish <https://github.com/jamesturk/jellyfish>`__
4. `py\_stringmatching <https://github.com/anhaidgroup/py_stringmatching>`__
5. `pylev <https://github.com/toastdriven/pylev>`__
6. `python-Levenshtein <https://github.com/ztane/python-Levenshtein>`__
7. `pyxDamerauLevenshtein <https://github.com/gfairchild/pyxDamerauLevenshtein>`__

Benchmarks
----------

For textdistance without extra requirements:

+--------------+------------+-------------+---------+
| algorithm    | library    | function    | time    |
+==============+============+=============+=========+
| DamerauLeven | jellyfish  | damerau\_le | 0.01043 |
| shtein       |            | venshtein\_ | 39      |
|              |            | distance    |         |
+--------------+------------+-------------+---------+
| DamerauLeven | pyxdamerau | damerau\_le | 0.15075 |
| shtein       | levenshtei | venshtein\_ |         |
|              | n          | distance    |         |
+--------------+------------+-------------+---------+
| DamerauLeven | **textdist | DamerauLeve | 0.30708 |
| shtein       | ance**     | nshtein     | 3       |
+--------------+------------+-------------+---------+
| DamerauLeven | pylev      | damerau\_le | 0.76065 |
| shtein       |            | venshtein   | 5       |
+--------------+------------+-------------+---------+
| DamerauLeven | abydos     | damerau\_le | 4.59495 |
| shtein       |            | venshtein   |         |
+--------------+------------+-------------+---------+
| Hamming      | Levenshtei | hamming     | 0.00145 |
|              | n          |             | 914     |
+--------------+------------+-------------+---------+
| Hamming      | jellyfish  | hamming\_di | 0.00230 |
|              |            | stance      | 915     |
+--------------+------------+-------------+---------+
| Hamming      | distance   | hamming     | 0.03575 |
|              |            |             | 62      |
+--------------+------------+-------------+---------+
| Hamming      | abydos     | hamming     | 0.03984 |
|              |            |             | 52      |
+--------------+------------+-------------+---------+
| Hamming      | **textdist | Hamming     | 0.13997 |
|              | ance**     |             |         |
+--------------+------------+-------------+---------+
| Jaro         | Levenshtei | jaro        | 0.00312 |
|              | n          |             | 573     |
+--------------+------------+-------------+---------+
| Jaro         | jellyfish  | jaro\_dista | 0.00522 |
|              |            | nce         | 548     |
+--------------+------------+-------------+---------+
| Jaro         | py\_string | jaro        | 0.17990 |
|              | matching   |             | 1       |
+--------------+------------+-------------+---------+
| Jaro         | **textdist | Jaro        | 0.26922 |
|              | ance**     |             | 9       |
+--------------+------------+-------------+---------+
| JaroWinkler  | Levenshtei | jaro\_winkl | 0.00330 |
|              | n          | er          | 839     |
+--------------+------------+-------------+---------+
| JaroWinkler  | jellyfish  | jaro\_winkl | 0.00537 |
|              |            | er          | 344     |
+--------------+------------+-------------+---------+
| JaroWinkler  | **textdist | JaroWinkler | 0.28676 |
|              | ance**     |             | 3       |
+--------------+------------+-------------+---------+
| Levenshtein  | Levenshtei | distance    | 0.00410 |
|              | n          |             | 18      |
+--------------+------------+-------------+---------+
| Levenshtein  | jellyfish  | levenshtein | 0.00618 |
|              |            | \_distance  | 915     |
+--------------+------------+-------------+---------+
| Levenshtein  | **textdist | Levenshtein | 0.17044 |
|              | ance**     |             | 3       |
+--------------+------------+-------------+---------+
| Levenshtein  | py\_string | levenshtein | 0.25270 |
|              | matching   |             | 9       |
+--------------+------------+-------------+---------+
| Levenshtein  | pylev      | levenshtein | 0.56995 |
|              |            |             | 7       |
+--------------+------------+-------------+---------+
| Levenshtein  | distance   | levenshtein | 1.13711 |
+--------------+------------+-------------+---------+
| Levenshtein  | abydos     | levenshtein | 3.68653 |
+--------------+------------+-------------+---------+

Total: 24 libs.

Textdistance use benchmark's results for algorithm's optimization and
try call fastest external libs first (if possible).

If you want you can run benchmark manually on youre system:

.. code:: bash

    pip install textdistance[all]
    python3 -m textdistance.benchmark

Consequently textdistance show benchmarks results table for your system
and save libraries priorities into
`libraries.json <textdistance/libraries.json>`__ file in textdistance's
folder. This file will be used by textdistance for calling fastest
algorithm implementation first.

Test
----

You can run tests via `tox <https://tox.readthedocs.io/en/latest/>`__:

.. code:: bash

    sudo pip3 install tox
    tox

.. |Build Status| image:: https://travis-ci.org/orsinium/textdistance.svg?branch=master
   :target: https://travis-ci.org/orsinium/textdistance
.. |PyPI version| image:: https://img.shields.io/pypi/v/textdistance.svg
   :target: https://pypi.python.org/pypi/textdistance
.. |Status| image:: https://img.shields.io/pypi/status/textdistance.svg
   :target: https://pypi.python.org/pypi/textdistance
.. |Code size| image:: https://img.shields.io/github/languages/code-size/orsinium/textdistance.svg
   :target: https://github.com/orsinium/textdistance
.. |License| image:: https://img.shields.io/pypi/l/textdistance.svg
   :target: LICENSE
