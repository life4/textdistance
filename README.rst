TextDistance
============

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

+--------------+----------+--------------+
| Algorithm    | Class    | Functions    |
+==============+==========+==============+
| `longest     | ``LCSSeq | ``lcsseq``   |
| common       | ``       |              |
| subsequence  |          |              |
| similarity < |          |              |
| https://en.w |          |              |
| ikipedia.org |          |              |
| /wiki/Longes |          |              |
| t_common_sub |          |              |
| sequence_pro |          |              |
| blem>`__     |          |              |
+--------------+----------+--------------+
| `longest     | ``LCSStr | ``lcsstr``   |
| common       | ``       |              |
| substring    |          |              |
| similarity < |          |              |
| https://docs |          |              |
| .python.org/ |          |              |
| 2/library/di |          |              |
| fflib.html#d |          |              |
| ifflib.Seque |          |              |
| nceMatcher>` |          |              |
| __           |          |              |
+--------------+----------+--------------+
| `Ratcliff-Ob | ``Ratcli | ``ratcliff_o |
| ershelp      | ffObersh | bershelp``   |
| similarity   | elp``    |              |
| similarity < |          |              |
| http://colla |          |              |
| boration.cmc |          |              |
| .ec.gc.ca/sc |          |              |
| ience/rpn/bi |          |              |
| blio/ddj/Web |          |              |
| site/article |          |              |
| s/DDJ/1988/8 |          |              |
| 807/8807c/88 |          |              |
| 07c.htm>`__  |          |              |
+--------------+----------+--------------+

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

Usage
-----

All algorithms have 2 interfaces:

1. Class which can get some algorithm-specific params by init.
2. Class instance with default init params for quick and simple usage.

All algorithms have some common methods:

1. ``.distance(*sequences)`` -- calculate distance between sequences.
2. ``.similarity(*sequences)`` -- calculate similarity for sequences.
3. ``.maximum(*sequences)`` -- maximum possible value for distance and
   similarity. ``distance + similarity == maximum``.
4. ``.normalized_distance(*sequences)`` -- normalized distance between
   sequences. The return value is a float between 0 and 1, where 0 means
   equal, and 1 totally different.
5. ``.normalized_distance(*sequences)`` -- normalized similarity for
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

