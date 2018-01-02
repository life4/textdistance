## Algorithms

### Edit based

| Algorithm                                                                                 | Class                | Functions              |
|-------------------------------------------------------------------------------------------|----------------------|------------------------|
| [Hamming](https://en.wikipedia.org/wiki/Hamming_distance)                                 | `Hamming`            | `hamming`              |
| [MLIPNS](http://www.sial.iias.spb.su/files/386-386-1-PB.pdf)                              | `Mlipns`             | `mlipns`               |
| [Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance)                         | `Levenshtein`        | `levenshtein`          |
| [Damerau-Levenshtein](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance) | `DamerauLevenshtein` | `damerau_levenshtein`  |
| [Jaro-Winkler](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance)               | `JaroWinkler`        | `jaro_winkler`, `jaro` |
| [Strcmp95](http://cpansearch.perl.org/src/SCW/Text-JaroWinkler-0.1/strcmp95.c)            | `Strcmp95`           | `strcmp95`             |
| [Needleman-Wunsch](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm)      | `NeedlemanWunsch`    | `needleman_wunsch`     |
| [Gotoh](https://www.cs.umd.edu/class/spring2003/cmsc838t/papers/gotoh1982.pdf)            | `Gotoh`              | `gotoh`                |
| [Smith-Waterman](https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm)          | `SmithWaterman`      | `smith_waterman`       |

### Token based

1. `jaccard`
2. `sorensen`, `sorensen_dice`, `dice`
3. `tversky`
4. `overlap`
5. `tanimoto`
6. `cosine`
7. `monge_elkan`
8. `bag`

### Sequence based

1. `lcsseq`
2. `lcsstr`
3. `ratcliff_obershelp`

### Compression based

1. `bz2_ncd`
2. `lzma_ncd`
3. `arith_ncd`
4. `rle_ncd`
5. `bwtrle_ncd`
6. `zlib_ncd`

### Phonetic

| Algorithm                                                                    | Class    | Functions |
| [MRA](https://en.wikipedia.org/wiki/Match_rating_approach)                   | `MRA`    | `mra`     |
| [Editex](https://anhaidgroup.github.io/py_stringmatching/v0.3.x/Editex.html) | `Editex` | `editex`  |

### Simple

1. `prefix`
2. `postfix`
3. `length`
4. `identity`


## Usage

All algorithms have 2 interfaces:

1. Class which can get some algorithm-specific params by init.
2. Class instance with default init params for quick and simple usage.

All algorithms have some common methods:

1. `.distance(*sequences)` -- calculate distance between sequences.
2. `.similarity(*sequences)` -- calculate similarity for sequences.
3. `.maximum(*sequences)` -- maximum possible value for distance and similarity. `distance + similarity == maximum`.
4. `.normalized_distance(*sequences)` -- normalized distance between sequences. The return value is a float between 0 and 1, where 0 means equal, and 1 totally different.
5. `.normalized_distance(*sequences)` -- normalized similarity for sequences. The return value is a float between 0 and 1, where 0 means totally different, and 1 equal.


Most common init arguments:

1. `qval` -- q-value for split sequences into q-grams. Possible values:
    * 1 (default) -- compare sequences by chars.
    * 2 or more -- transform sequences to q-grams.
    * None -- split sequences by words.
2. `as_set` -- for token-based algorithms:
    * True -- `t` and `ttt` is equal.
    * False (default) -- `t` and `ttt` is different.

