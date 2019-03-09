TextDistance
============

.. figure:: logo.png
   :alt: TextDistance logo

   TextDistance logo

|Build Status| |PyPI version| |Status| |Code size| |License|

**TextDistance** -- python library for comparing distance between two or
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

`Normalized compression
distance <https://en.wikipedia.org/wiki/Normalized_compression_distance#Normalized_compression_distance>`__
with different compression algorithms.

Classic compression algorithms:

+---------------------------------------------------------------------------------+-----------------+------------------+
| Algorithm                                                                       | Class           | Function         |
+=================================================================================+=================+==================+
| `Arithmetic coding <https://en.wikipedia.org/wiki/Arithmetic_coding>`__         | ``ArithNCD``    | ``arith_ncd``    |
+---------------------------------------------------------------------------------+-----------------+------------------+
| `RLE <https://en.wikipedia.org/wiki/Run-length_encoding>`__                     | ``RLENCD``      | ``rle_ncd``      |
+---------------------------------------------------------------------------------+-----------------+------------------+
| `BWT RLE <https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform>`__   | ``BWTRLENCD``   | ``bwtrle_ncd``   |
+---------------------------------------------------------------------------------+-----------------+------------------+

Normal compression algorithms:

+----------------------------------------------------------------------------+------------------+-------------------+
| Algorithm                                                                  | Class            | Function          |
+============================================================================+==================+===================+
| Square Root                                                                | ``SqrtNCD``      | ``sqrt_ncd``      |
+----------------------------------------------------------------------------+------------------+-------------------+
| `Entropy <https://en.wikipedia.org/wiki/Entropy_(information_theory)>`__   | ``EntropyNCD``   | ``entropy_ncd``   |
+----------------------------------------------------------------------------+------------------+-------------------+

Work in progress algorithms that compare two strings as array of bits:

+-------------------------------------------------+---------------+----------------+
| Algorithm                                       | Class         | Function       |
+=================================================+===============+================+
| `BZ2 <https://en.wikipedia.org/wiki/Bzip2>`__   | ``BZ2NCD``    | ``bz2_ncd``    |
+-------------------------------------------------+---------------+----------------+
| `LZMA <https://en.wikipedia.org/wiki/LZMA>`__   | ``LZMANCD``   | ``lzma_ncd``   |
+-------------------------------------------------+---------------+----------------+
| `ZLib <https://en.wikipedia.org/wiki/Zlib>`__   | ``ZLIBNCD``   | ``zlib_ncd``   |
+-------------------------------------------------+---------------+----------------+

See `blog post <https://articles.life4web.ru/eng/ncd/>`__ for more
details about NCD.

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

With extra libraries for maximum speed:

.. code:: bash

    pip install textdistance[extras]

With all libraries (required for `benchmarking <#benchmarks>`__ and
`testing <#test>`__):

.. code:: bash

    pip install textdistance[benchmark]

With algorithm specific extras:

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
    pip install -e .[benchmark]

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

Extra libraries
---------------

For main algorithms textdistance try to call known external libraries
(fastest first) if available (installed in your system) and possible
(this implementation can compare this type of sequences).
`Install <#installation>`__ textdistance with extras for this feature.

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

Algorithms:

1. DamerauLevenshtein
2. Hamming
3. Jaro
4. JaroWinkler
5. Levenshtein

Benchmarks
----------

Without extras installation:

+--------------+------------+-------------+---------+
| algorithm    | library    | function    | time    |
+==============+============+=============+=========+
| DamerauLeven | jellyfish  | damerau\_le | 0.00965 |
| shtein       |            | venshtein\_ | 294     |
|              |            | distance    |         |
+--------------+------------+-------------+---------+
| DamerauLeven | pyxdamerau | damerau\_le | 0.15137 |
| shtein       | levenshtei | venshtein\_ | 8       |
|              | n          | distance    |         |
+--------------+------------+-------------+---------+
| DamerauLeven | pylev      | damerau\_le | 0.76646 |
| shtein       |            | venshtein   | 1       |
+--------------+------------+-------------+---------+
| DamerauLeven | **textdist | DamerauLeve | 4.13463 |
| shtein       | ance**     | nshtein     |         |
+--------------+------------+-------------+---------+
| DamerauLeven | abydos     | damerau\_le | 4.3831  |
| shtein       |            | venshtein   |         |
+--------------+------------+-------------+---------+
| Hamming      | Levenshtei | hamming     | 0.00144 |
|              | n          |             | 28      |
+--------------+------------+-------------+---------+
| Hamming      | jellyfish  | hamming\_di | 0.00240 |
|              |            | stance      | 262     |
+--------------+------------+-------------+---------+
| Hamming      | distance   | hamming     | 0.03625 |
|              |            |             | 3       |
+--------------+------------+-------------+---------+
| Hamming      | abydos     | hamming     | 0.03839 |
|              |            |             | 33      |
+--------------+------------+-------------+---------+
| Hamming      | **textdist | Hamming     | 0.17678 |
|              | ance**     |             | 1       |
+--------------+------------+-------------+---------+
| Jaro         | Levenshtei | jaro        | 0.00313 |
|              | n          |             | 561     |
+--------------+------------+-------------+---------+
| Jaro         | jellyfish  | jaro\_dista | 0.00518 |
|              |            | nce         | 85      |
+--------------+------------+-------------+---------+
| Jaro         | py\_string | jaro        | 0.18062 |
|              | matching   |             | 8       |
+--------------+------------+-------------+---------+
| Jaro         | **textdist | Jaro        | 0.27891 |
|              | ance**     |             | 7       |
+--------------+------------+-------------+---------+
| JaroWinkler  | Levenshtei | jaro\_winkl | 0.00319 |
|              | n          | er          | 735     |
+--------------+------------+-------------+---------+
| JaroWinkler  | jellyfish  | jaro\_winkl | 0.00540 |
|              |            | er          | 443     |
+--------------+------------+-------------+---------+
| JaroWinkler  | **textdist | JaroWinkler | 0.28962 |
|              | ance**     |             | 6       |
+--------------+------------+-------------+---------+
| Levenshtein  | Levenshtei | distance    | 0.00414 |
|              | n          |             | 404     |
+--------------+------------+-------------+---------+
| Levenshtein  | jellyfish  | levenshtein | 0.00601 |
|              |            | \_distance  | 647     |
+--------------+------------+-------------+---------+
| Levenshtein  | py\_string | levenshtein | 0.25290 |
|              | matching   |             | 1       |
+--------------+------------+-------------+---------+
| Levenshtein  | pylev      | levenshtein | 0.56918 |
|              |            |             | 2       |
+--------------+------------+-------------+---------+
| Levenshtein  | distance   | levenshtein | 1.15726 |
+--------------+------------+-------------+---------+
| Levenshtein  | abydos     | levenshtein | 3.68451 |
+--------------+------------+-------------+---------+
| Levenshtein  | **textdist | Levenshtein | 8.63674 |
|              | ance**     |             |         |
+--------------+------------+-------------+---------+

Total: 24 libs.

Yeah, so slow. Use TextDistance on production only with extras.

Textdistance use benchmark's results for algorithm's optimization and
try to call fastest external lib first (if possible).

You can run benchmark manually on your system:

.. code:: bash

    pip install textdistance[benchmark]
    python3 -m textdistance.benchmark

TextDistance show benchmarks results table for your system and save
libraries priorities into ``libraries.json`` file in TextDistance's
folder. This file will be used by textdistance for calling fastest
algorithm implementation. Default
`libraries.json <textdistance/libraries.json>`__ already included in
package.

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
