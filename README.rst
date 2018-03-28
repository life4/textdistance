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

Stable:

.. code:: bash

    pip install textdistance

Dev:

.. code:: bash

    pip install -e git+https://github.com/orsinium/textdistance.git#egg=textdistance

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
