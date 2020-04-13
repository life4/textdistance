TextDistance
============

.. figure:: logo.png
   :alt: TextDistance logo

   TextDistance logo

`Build Status <https://travis-ci.org/life4/textdistance>`__ `PyPI
version <https://pypi.python.org/pypi/textdistance>`__
`Status <https://pypi.python.org/pypi/textdistance>`__ `Code
size <https://github.com/life4/textdistance>`__ `License <LICENSE>`__

**TextDistance** – python library for comparing distance between two or
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

+-----------------------+-----------------------+-----------------------+
| Algorithm             | Class                 | Functions             |
+=======================+=======================+=======================+
| `Hamming <https://en. | ``Hamming``           | ``hamming``           |
| wikipedia.org/wiki/Ha |                       |                       |
| mming_distance>`__    |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `MLIPNS <http://www.s | ``Mlipns``            | ``mlipns``            |
| ial.iias.spb.su/files |                       |                       |
| /386-386-1-PB.pdf>`__ |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Levenshtein <https:/ | ``Levenshtein``       | ``levenshtein``       |
| /en.wikipedia.org/wik |                       |                       |
| i/Levenshtein_distanc |                       |                       |
| e>`__                 |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Damerau-Levenshtein  | ``DamerauLevenshtein` | ``damerau_levenshtein |
| <https://en.wikipedia | `                     | ``                    |
| .org/wiki/Damerau%E2% |                       |                       |
| 80%93Levenshtein_dist |                       |                       |
| ance>`__              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Jaro-Winkler <https: | ``JaroWinkler``       | ``jaro_winkler``,     |
| //en.wikipedia.org/wi |                       | ``jaro``              |
| ki/Jaro%E2%80%93Winkl |                       |                       |
| er_distance>`__       |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Strcmp95 <http://cpa | ``StrCmp95``          | ``strcmp95``          |
| nsearch.perl.org/src/ |                       |                       |
| SCW/Text-JaroWinkler- |                       |                       |
| 0.1/strcmp95.c>`__    |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Needleman-Wunsch <ht | ``NeedlemanWunsch``   | ``needleman_wunsch``  |
| tps://en.wikipedia.or |                       |                       |
| g/wiki/Needleman%E2%8 |                       |                       |
| 0%93Wunsch_algorithm> |                       |                       |
| `__                   |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Gotoh <https://www.c | ``Gotoh``             | ``gotoh``             |
| s.umd.edu/class/sprin |                       |                       |
| g2003/cmsc838t/papers |                       |                       |
| /gotoh1982.pdf>`__    |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Smith-Waterman <http | ``SmithWaterman``     | ``smith_waterman``    |
| s://en.wikipedia.org/ |                       |                       |
| wiki/Smith%E2%80%93Wa |                       |                       |
| terman_algorithm>`__  |                       |                       |
+-----------------------+-----------------------+-----------------------+

Token based
~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Algorithm             | Class                 | Functions             |
+=======================+=======================+=======================+
| `Jaccard              | ``Jaccard``           | ``jaccard``           |
| index <https://en.wik |                       |                       |
| ipedia.org/wiki/Jacca |                       |                       |
| rd_index>`__          |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Sørensen–Dice        | ``Sorensen``          | ``sorensen``,         |
| coefficient <https:// |                       | ``sorensen_dice``,    |
| en.wikipedia.org/wiki |                       | ``dice``              |
| /S%C3%B8rensen%E2%80% |                       |                       |
| 93Dice_coefficient>`_ |                       |                       |
| _                     |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Tversky              | ``Tversky``           | ``tversky``           |
| index <https://en.wik |                       |                       |
| ipedia.org/wiki/Tvers |                       |                       |
| ky_index>`__          |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Overlap              | ``Overlap``           | ``overlap``           |
| coefficient <https:// |                       |                       |
| en.wikipedia.org/wiki |                       |                       |
| /Overlap_coefficient> |                       |                       |
| `__                   |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Tanimoto             | ``Tanimoto``          | ``tanimoto``          |
| distance <https://en. |                       |                       |
| wikipedia.org/wiki/Ja |                       |                       |
| ccard_index#Tanimoto_ |                       |                       |
| similarity_and_distan |                       |                       |
| ce>`__                |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Cosine               | ``Cosine``            | ``cosine``            |
| similarity <https://e |                       |                       |
| n.wikipedia.org/wiki/ |                       |                       |
| Cosine_similarity>`__ |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Monge-Elkan <https:/ | ``MongeElkan``        | ``monge_elkan``       |
| /www.academia.edu/200 |                       |                       |
| 314/Generalized_Monge |                       |                       |
| -Elkan_Method_for_App |                       |                       |
| roximate_Text_String_ |                       |                       |
| Comparison>`__        |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Bag                  | ``Bag``               | ``bag``               |
| distance <https://git |                       |                       |
| hub.com/Yomguithereal |                       |                       |
| /talisman/blob/master |                       |                       |
| /src/metrics/distance |                       |                       |
| /bag.js>`__           |                       |                       |
+-----------------------+-----------------------+-----------------------+

Sequence based
~~~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Algorithm             | Class                 | Functions             |
+=======================+=======================+=======================+
| `longest common       | ``LCSSeq``            | ``lcsseq``            |
| subsequence           |                       |                       |
| similarity <https://e |                       |                       |
| n.wikipedia.org/wiki/ |                       |                       |
| Longest_common_subseq |                       |                       |
| uence_problem>`__     |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `longest common       | ``LCSStr``            | ``lcsstr``            |
| substring             |                       |                       |
| similarity <https://d |                       |                       |
| ocs.python.org/2/libr |                       |                       |
| ary/difflib.html#diff |                       |                       |
| lib.SequenceMatcher>` |                       |                       |
| __                    |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Ratcliff-Obershelp   | ``RatcliffObershelp`` | ``ratcliff_obershelp` |
| similarity <https://e |                       | `                     |
| n.wikipedia.org/wiki/ |                       |                       |
| Gestalt_Pattern_Match |                       |                       |
| ing>`__               |                       |                       |
+-----------------------+-----------------------+-----------------------+

Compression based
~~~~~~~~~~~~~~~~~

`Normalized compression
distance <https://en.wikipedia.org/wiki/Normalized_compression_distance#Normalized_compression_distance>`__
with different compression algorithms.

Classic compression algorithms:

+-----------------------+-----------------------+-----------------------+
| Algorithm             | Class                 | Function              |
+=======================+=======================+=======================+
| `Arithmetic           | ``ArithNCD``          | ``arith_ncd``         |
| coding <https://en.wi |                       |                       |
| kipedia.org/wiki/Arit |                       |                       |
| hmetic_coding>`__     |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `RLE <https://en.wiki | ``RLENCD``            | ``rle_ncd``           |
| pedia.org/wiki/Run-le |                       |                       |
| ngth_encoding>`__     |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `BWT                  | ``BWTRLENCD``         | ``bwtrle_ncd``        |
| RLE <https://en.wikip |                       |                       |
| edia.org/wiki/Burrows |                       |                       |
| %E2%80%93Wheeler_tran |                       |                       |
| sform>`__             |                       |                       |
+-----------------------+-----------------------+-----------------------+

Normal compression algorithms:

+-----------------------+-----------------------+-----------------------+
| Algorithm             | Class                 | Function              |
+=======================+=======================+=======================+
| Square Root           | ``SqrtNCD``           | ``sqrt_ncd``          |
+-----------------------+-----------------------+-----------------------+
| `Entropy <https://en. | ``EntropyNCD``        | ``entropy_ncd``       |
| wikipedia.org/wiki/En |                       |                       |
| tropy_(information_th |                       |                       |
| eory)>`__             |                       |                       |
+-----------------------+-----------------------+-----------------------+

Work in progress algorithms that compare two strings as array of bits:

+-----------------------------------------------+-------------+--------------+
| Algorithm                                     | Class       | Function     |
+===============================================+=============+==============+
| `BZ2 <https://en.wikipedia.org/wiki/Bzip2>`__ | ``BZ2NCD``  | ``bz2_ncd``  |
+-----------------------------------------------+-------------+--------------+
| `LZMA <https://en.wikipedia.org/wiki/LZMA>`__ | ``LZMANCD`` | ``lzma_ncd`` |
+-----------------------------------------------+-------------+--------------+
| `ZLib <https://en.wikipedia.org/wiki/Zlib>`__ | ``ZLIBNCD`` | ``zlib_ncd`` |
+-----------------------------------------------+-------------+--------------+

See `blog post <https://articles.life4web.ru/other/ncd/>`__ for more
details about NCD.

Phonetic
~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Algorithm             | Class                 | Functions             |
+=======================+=======================+=======================+
| `MRA <https://en.wiki | ``MRA``               | ``mra``               |
| pedia.org/wiki/Match_ |                       |                       |
| rating_approach>`__   |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Editex <https://anha | ``Editex``            | ``editex``            |
| idgroup.github.io/py_ |                       |                       |
| stringmatching/v0.3.x |                       |                       |
| /Editex.html>`__      |                       |                       |
+-----------------------+-----------------------+-----------------------+

Simple
~~~~~~

+---------------------+--------------+--------------+
| Algorithm           | Class        | Functions    |
+=====================+==============+==============+
| Prefix similarity   | ``Prefix``   | ``prefix``   |
+---------------------+--------------+--------------+
| Postfix similarity  | ``Postfix``  | ``postfix``  |
+---------------------+--------------+--------------+
| Length distance     | ``Length``   | ``length``   |
+---------------------+--------------+--------------+
| Identity similarity | ``Identity`` | ``identity`` |
+---------------------+--------------+--------------+
| Matrix similarity   | ``Matrix``   | ``matrix``   |
+---------------------+--------------+--------------+

Installation
------------

Stable
~~~~~~

Only pure python implementation:

.. code:: bash

   pip install textdistance

With extra libraries for maximum speed:

.. code:: bash

   pip install "textdistance[extras]"

With all libraries (required for `benchmarking <#benchmarks>`__ and
`testing <#test>`__):

.. code:: bash

   pip install "textdistance[benchmark]"

With algorithm specific extras:

.. code:: bash

   pip install "textdistance[Hamming]"

Algorithms with available extras: ``DamerauLevenshtein``, ``Hamming``,
``Jaro``, ``JaroWinkler``, ``Levenshtein``.

Dev
~~~

Via pip:

.. code:: bash

   pip install -e git+https://github.com/life4/textdistance.git#egg=textdistance

Or clone repo and install with some extras:

.. code:: bash

   git clone https://github.com/life4/textdistance.git
   pip install -e ".[benchmark]"

Usage
-----

All algorithms have 2 interfaces:

1. Class with algorithm-specific params for customizing.
2. Class instance with default params for quick and simple usage.

All algorithms have some common methods:

1. ``.distance(*sequences)`` – calculate distance between sequences.
2. ``.similarity(*sequences)`` – calculate similarity for sequences.
3. ``.maximum(*sequences)`` – maximum possible value for distance and
   similarity. For any sequence: ``distance + similarity == maximum``.
4. ``.normalized_distance(*sequences)`` – normalized distance between
   sequences. The return value is a float between 0 and 1, where 0 means
   equal, and 1 totally different.
5. ``.normalized_similarity(*sequences)`` – normalized similarity for
   sequences. The return value is a float between 0 and 1, where 0 means
   totally different, and 1 equal.

Most common init arguments:

1. ``qval`` – q-value for split sequences into q-grams. Possible values:

   -  1 (default) – compare sequences by chars.
   -  2 or more – transform sequences to q-grams.
   -  None – split sequences by words.

2. ``as_set`` – for token-based algorithms:

   -  True – ``t`` and ``ttt`` is equal.
   -  False (default) – ``t`` and ``ttt`` is different.

Examples
--------

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

Articles
--------

A few articles with examples how to use textdistance in the real world:

-  `Guide to Fuzzy Matching with
   Python <http://theautomatic.net/2019/11/13/guide-to-fuzzy-matching-with-python/>`__
-  `String similarity — the basic know your algorithms
   guide! <https://itnext.io/string-similarity-the-basic-know-your-algorithms-guide-3de3d7346227>`__
-  `Normalized compression
   distance <https://articles.life4web.ru/other/ncd/>`__

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
4. `py_stringmatching <https://github.com/anhaidgroup/py_stringmatching>`__
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

+---------------------+-----------------+-------------------+-----------+
| algorithm           | library         | function          | time      |
+=====================+=================+===================+===========+
| DamerauLevenshtein  | jellyfish       | damerau_levenshte | 0.0096529 |
|                     |                 | in_distance       | 4         |
+---------------------+-----------------+-------------------+-----------+
| DamerauLevenshtein  | pyxdamerauleven | damerau_levenshte | 0.151378  |
|                     | shtein          | in_distance       |           |
+---------------------+-----------------+-------------------+-----------+
| DamerauLevenshtein  | pylev           | damerau_levenshte | 0.766461  |
|                     |                 | in                |           |
+---------------------+-----------------+-------------------+-----------+
| DamerauLevenshtein  | **textdistance* | DamerauLevenshtei | 4.13463   |
|                     | *               | n                 |           |
+---------------------+-----------------+-------------------+-----------+
| DamerauLevenshtein  | abydos          | damerau_levenshte | 4.3831    |
|                     |                 | in                |           |
+---------------------+-----------------+-------------------+-----------+
| Hamming             | Levenshtein     | hamming           | 0.0014428 |
+---------------------+-----------------+-------------------+-----------+
| Hamming             | jellyfish       | hamming_distance  | 0.0024026 |
|                     |                 |                   | 2         |
+---------------------+-----------------+-------------------+-----------+
| Hamming             | distance        | hamming           | 0.036253  |
+---------------------+-----------------+-------------------+-----------+
| Hamming             | abydos          | hamming           | 0.0383933 |
+---------------------+-----------------+-------------------+-----------+
| Hamming             | **textdistance* | Hamming           | 0.176781  |
|                     | *               |                   |           |
+---------------------+-----------------+-------------------+-----------+
| Jaro                | Levenshtein     | jaro              | 0.0031356 |
|                     |                 |                   | 1         |
+---------------------+-----------------+-------------------+-----------+
| Jaro                | jellyfish       | jaro_distance     | 0.0051885 |
+---------------------+-----------------+-------------------+-----------+
| Jaro                | py_stringmatchi | jaro              | 0.180628  |
|                     | ng              |                   |           |
+---------------------+-----------------+-------------------+-----------+
| Jaro                | **textdistance* | Jaro              | 0.278917  |
|                     | *               |                   |           |
+---------------------+-----------------+-------------------+-----------+
| JaroWinkler         | Levenshtein     | jaro_winkler      | 0.0031973 |
|                     |                 |                   | 5         |
+---------------------+-----------------+-------------------+-----------+
| JaroWinkler         | jellyfish       | jaro_winkler      | 0.0054044 |
|                     |                 |                   | 3         |
+---------------------+-----------------+-------------------+-----------+
| JaroWinkler         | **textdistance* | JaroWinkler       | 0.289626  |
|                     | *               |                   |           |
+---------------------+-----------------+-------------------+-----------+
| Levenshtein         | Levenshtein     | distance          | 0.0041440 |
|                     |                 |                   | 4         |
+---------------------+-----------------+-------------------+-----------+
| Levenshtein         | jellyfish       | levenshtein_dista | 0.0060164 |
|                     |                 | nce               | 7         |
+---------------------+-----------------+-------------------+-----------+
| Levenshtein         | py_stringmatchi | levenshtein       | 0.252901  |
|                     | ng              |                   |           |
+---------------------+-----------------+-------------------+-----------+
| Levenshtein         | pylev           | levenshtein       | 0.569182  |
+---------------------+-----------------+-------------------+-----------+
| Levenshtein         | distance        | levenshtein       | 1.15726   |
+---------------------+-----------------+-------------------+-----------+
| Levenshtein         | abydos          | levenshtein       | 3.68451   |
+---------------------+-----------------+-------------------+-----------+
| Levenshtein         | **textdistance* | Levenshtein       | 8.63674   |
|                     | *               |                   |           |
+---------------------+-----------------+-------------------+-----------+

Total: 24 libs.

Yeah, so slow. Use TextDistance on production only with extras.

Textdistance use benchmark’s results for algorithm’s optimization and
try to call fastest external lib first (if possible).

You can run benchmark manually on your system:

.. code:: bash

   pip install textdistance[benchmark]
   python3 -m textdistance.benchmark

TextDistance show benchmarks results table for your system and save
libraries priorities into ``libraries.json`` file in TextDistance’s
folder. This file will be used by textdistance for calling fastest
algorithm implementation. Default
`libraries.json <textdistance/libraries.json>`__ already included in
package.

Running tests
-------------

You can run tests via `dephell <https://github.com/dephell/dephell>`__:

.. code:: bash

   curl -L dephell.org/install | python3
   dephell venv create --env=pytest-external
   dephell deps install --env=pytest-external
   dephell venv run --env=pytest-external

Contributing
------------

PRs are welcome!

-  Found a bug? Fix it!
-  Want to add more algorithms? Sure! Just make it with the same
   interface as other algorithms in the lib and add some tests.
-  Can make something faster? Great! Just avoid external dependencies
   and remember that everything should work not only with strings.
-  Something else that do you think is good? Do it! Just make sure that
   CI passes and everything from the README is still applicable
   (interface, features, and so on).
-  Have no time to code? Tell your friends and subscribers about
   ``textdistance``. More users, more contributions, more amazing
   features.

Thank you :heart:
