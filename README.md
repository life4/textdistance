# TextDistance

![TextDistance logo](logo.png)

[![Build Status](https://travis-ci.org/orsinium/textdistance.svg?branch=master)](https://travis-ci.org/orsinium/textdistance) [![PyPI version](https://img.shields.io/pypi/v/textdistance.svg)](https://pypi.python.org/pypi/textdistance) [![Status](https://img.shields.io/pypi/status/textdistance.svg)](https://pypi.python.org/pypi/textdistance) [![Code size](https://img.shields.io/github/languages/code-size/orsinium/textdistance.svg)](https://github.com/orsinium/textdistance) [![License](https://img.shields.io/pypi/l/textdistance.svg)](LICENSE)

**TextDistance** -- python library for comparing distance between two or more sequences by many algorithms.

Features:

* 30+ algorithms
* Pure python implementation
* Simple usage
* More than two sequences comparing
* Some algorithms have more than one implementation in one class.
* Optional numpy usage for maximum speed.

## Algorithms

### Edit based

| Algorithm                                                                                 | Class                | Functions              |
|-------------------------------------------------------------------------------------------|----------------------|------------------------|
| [Hamming](https://en.wikipedia.org/wiki/Hamming_distance)                                 | `Hamming`            | `hamming`              |
| [MLIPNS](http://www.sial.iias.spb.su/files/386-386-1-PB.pdf)                              | `Mlipns`             | `mlipns`               |
| [Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance)                         | `Levenshtein`        | `levenshtein`          |
| [Damerau-Levenshtein](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance) | `DamerauLevenshtein` | `damerau_levenshtein`  |
| [Jaro-Winkler](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance)               | `JaroWinkler`        | `jaro_winkler`, `jaro` |
| [Strcmp95](http://cpansearch.perl.org/src/SCW/Text-JaroWinkler-0.1/strcmp95.c)            | `StrCmp95`           | `strcmp95`             |
| [Needleman-Wunsch](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm)      | `NeedlemanWunsch`    | `needleman_wunsch`     |
| [Gotoh](https://www.cs.umd.edu/class/spring2003/cmsc838t/papers/gotoh1982.pdf)            | `Gotoh`              | `gotoh`                |
| [Smith-Waterman](https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm)          | `SmithWaterman`      | `smith_waterman`       |

### Token based

| Algorithm                                                                                 | Class                | Functions     |
|-------------------------------------------------------------------------------------------|----------------------|---------------|
| [Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index)                              | `Jaccard`            | `jaccard`     |
| [Sørensen–Dice coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient) | `Sorensen`   | `sorensen`, `sorensen_dice`, `dice` |
| [Tversky index](https://en.wikipedia.org/wiki/Tversky_index)                              | `Tversky`            | `tversky`    |
| [Overlap coefficient](https://en.wikipedia.org/wiki/Overlap_coefficient)                  | `Overlap`            | `overlap`    |
| [Tanimoto distance](https://en.wikipedia.org/wiki/Jaccard_index#Tanimoto_similarity_and_distance) | `Tanimoto`   | `tanimoto`   |
| [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity)                      | `Cosine`             | `cosine`     |
| [Monge-Elkan](https://www.academia.edu/200314/Generalized_Monge-Elkan_Method_for_Approximate_Text_String_Comparison) | `MongeElkan` | `monge_elkan` |
| [Bag distance](https://github.com/Yomguithereal/talisman/blob/master/src/metrics/distance/bag.js) | `Bag`        | `bag`        |

### Sequence based

| Algorithm | Class | Functions |
|-----------|-------|-----------|
| [longest common subsequence similarity](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)          | `LCSSeq` | `lcsseq` |
| [longest common substring similarity](https://docs.python.org/2/library/difflib.html#difflib.SequenceMatcher)      | `LCSStr` | `lcsstr` |
| [Ratcliff-Obershelp similarity](http://collaboration.cmc.ec.gc.ca/science/rpn/biblio/ddj/Website/articles/DDJ/1988/8807/8807c/8807c.htm) | `RatcliffObershelp` | `ratcliff_obershelp` |

### Compression based

[Normalized compression distance](https://en.wikipedia.org/wiki/Normalized_compression_distance#Normalized_compression_distance) with different compression algorithms.

Classic compression algorithms:

| Algorithm                                                                  | Class       | Function     |
|----------------------------------------------------------------------------|-------------|--------------|
| [Arithmetic coding](https://en.wikipedia.org/wiki/Arithmetic_coding)       | `ArithNCD`  | `arith_ncd`  |
| [RLE](https://en.wikipedia.org/wiki/Run-length_encoding)                   | `RLENCD`    | `rle_ncd`    |
| [BWT RLE](https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform) | `BWTRLENCD` | `bwtrle_ncd` |

Normal compression algorithms:

| Algorithm                                                                  | Class        | Function      |
|----------------------------------------------------------------------------|--------------|---------------|
| Square Root                                                                | `SqrtNCD`    | `sqrt_ncd`    |
| [Entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory))      | `EntropyNCD` | `entropy_ncd` |

Work in progress algorithms that compare two strings as array of bits:

| Algorithm                                  | Class     | Function   |
|--------------------------------------------|-----------|------------|
| [BZ2](https://en.wikipedia.org/wiki/Bzip2) | `BZ2NCD`  | `bz2_ncd`  |
| [LZMA](https://en.wikipedia.org/wiki/LZMA) | `LZMANCD` | `lzma_ncd` |
| [ZLib](https://en.wikipedia.org/wiki/Zlib) | `ZLIBNCD` | `zlib_ncd` |

See [blog post](https://articles.life4web.ru/eng/ncd/) for more details about NCD.

### Phonetic

| Algorithm                                                                    | Class    | Functions |
|------------------------------------------------------------------------------|----------|-----------|
| [MRA](https://en.wikipedia.org/wiki/Match_rating_approach)                   | `MRA`    | `mra`     |
| [Editex](https://anhaidgroup.github.io/py_stringmatching/v0.3.x/Editex.html) | `Editex` | `editex`  |

### Simple

| Algorithm           | Class      | Functions  |
|---------------------|------------|------------|
| Prefix similarity   | `Prefix`   | `prefix`   |
| Postfix similarity  | `Postfix`  | `postfix`  |
| Length distance     | `Length`   | `length`   |
| Identity similarity | `Identity` | `identity` |
| Matrix similarity   | `Matrix`   | `matrix`   |


## Installation

### Stable

Only pure python implementation:

```bash
pip install textdistance
```

With extra libraries for maximum speed:

```bash
pip install textdistance[extras]
```

With all libraries (required for [benchmarking](#benchmarks) and [testing](#test)):

```bash
pip install textdistance[benchmark]
```

With algorithm specific extras:

```bash
pip install textdistance[Hamming]
```

Algorithms with available extras: `DamerauLevenshtein`, `Hamming`, `Jaro`, `JaroWinkler`, `Levenshtein`.

### Dev

Via pip:

```bash
pip install -e git+https://github.com/orsinium/textdistance.git#egg=textdistance
```

Or clone repo and install with some extras:

```bash
git clone https://github.com/orsinium/textdistance.git
pip install -e .[benchmark]
```


## Usage

All algorithms have 2 interfaces:

1. Class with algorithm-specific params for customizing.
2. Class instance with default params for quick and simple usage.

All algorithms have some common methods:

1. `.distance(*sequences)` -- calculate distance between sequences.
2. `.similarity(*sequences)` -- calculate similarity for sequences.
3. `.maximum(*sequences)` -- maximum possible value for distance and similarity. For any sequence: `distance + similarity == maximum`.
4. `.normalized_distance(*sequences)` -- normalized distance between sequences. The return value is a float between 0 and 1, where 0 means equal, and 1 totally different.
5. `.normalized_similarity(*sequences)` -- normalized similarity for sequences. The return value is a float between 0 and 1, where 0 means totally different, and 1 equal.


Most common init arguments:

1. `qval` -- q-value for split sequences into q-grams. Possible values:
    * 1 (default) -- compare sequences by chars.
    * 2 or more -- transform sequences to q-grams.
    * None -- split sequences by words.
2. `as_set` -- for token-based algorithms:
    * True -- `t` and `ttt` is equal.
    * False (default) -- `t` and `ttt` is different.

## Example

For example, [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance):

```python
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

```

Any other algorithms have same interface.


## Extra libraries

For main algorithms textdistance try to call known external libraries (fastest first) if available (installed in your system) and possible (this implementation can compare this type of sequences). [Install](#installation) textdistance with extras for this feature.

You can disable this by passing `external=False` argument on init:

```python3
import textdistance
hamming = textdistance.Hamming(external=False)
hamming('text', 'testit')
# 3
```

Supported libraries:

1. [abydos](https://github.com/chrislit/abydos)
1. [Distance](https://github.com/doukremt/distance)
1. [jellyfish](https://github.com/jamesturk/jellyfish)
1. [py_stringmatching](https://github.com/anhaidgroup/py_stringmatching)
1. [pylev](https://github.com/toastdriven/pylev)
1. [python-Levenshtein](https://github.com/ztane/python-Levenshtein)
1. [pyxDamerauLevenshtein](https://github.com/gfairchild/pyxDamerauLevenshtein)

Algorithms:

1. DamerauLevenshtein
1. Hamming
1. Jaro
1. JaroWinkler
1. Levenshtein


## Benchmarks

Without extras installation:

| algorithm | library | function | time |
|-----------|---------|----------|------|
| DamerauLevenshtein | jellyfish | damerau_levenshtein_distance | 0.00965294 |
| DamerauLevenshtein | pyxdameraulevenshtein | damerau_levenshtein_distance | 0.151378 |
| DamerauLevenshtein | pylev | damerau_levenshtein | 0.766461 |
| DamerauLevenshtein | **textdistance** | DamerauLevenshtein | 4.13463 |
| DamerauLevenshtein | abydos | damerau_levenshtein | 4.3831 |
| Hamming | Levenshtein | hamming | 0.0014428 |
| Hamming | jellyfish | hamming_distance | 0.00240262 |
| Hamming | distance | hamming | 0.036253 |
| Hamming | abydos | hamming | 0.0383933 |
| Hamming | **textdistance** | Hamming | 0.176781 |
| Jaro | Levenshtein | jaro | 0.00313561 |
| Jaro | jellyfish | jaro_distance | 0.0051885 |
| Jaro | py_stringmatching | jaro | 0.180628 |
| Jaro | **textdistance** | Jaro | 0.278917 |
| JaroWinkler | Levenshtein | jaro_winkler | 0.00319735 |
| JaroWinkler | jellyfish | jaro_winkler | 0.00540443 |
| JaroWinkler | **textdistance** | JaroWinkler | 0.289626 |
| Levenshtein | Levenshtein | distance | 0.00414404 |
| Levenshtein | jellyfish | levenshtein_distance | 0.00601647 |
| Levenshtein | py_stringmatching | levenshtein | 0.252901 |
| Levenshtein | pylev | levenshtein | 0.569182 |
| Levenshtein | distance | levenshtein | 1.15726 |
| Levenshtein | abydos | levenshtein | 3.68451 |
| Levenshtein | **textdistance** | Levenshtein | 8.63674 |

Total: 24 libs.

Yeah, so slow. Use TextDistance on production only with extras.

Textdistance use benchmark's results for algorithm's optimization and try to call fastest external lib first (if possible).

You can run benchmark manually on your system:

```bash
pip install textdistance[benchmark]
python3 -m textdistance.benchmark
```

TextDistance show benchmarks results table for your system and save libraries priorities into `libraries.json` file in TextDistance's folder. This file will be used by textdistance for calling fastest algorithm implementation. Default [libraries.json](textdistance/libraries.json) already included in package.


## Test

You can run tests via [tox](https://tox.readthedocs.io/en/latest/):

```bash
sudo pip3 install tox
tox
```
