LIBRARIES = {
    'DamerauLevenshtein': (
        'jellyfish.damerau_levenshtein_distance',
        'pyxdameraulevenshtein.damerau_levenshtein_distance',
        'abydos.distance.levenshtein',
    ),
    'Levenshtein': (
        'jellyfish.levenshtein_distance',
        'abydos.distance.levenshtein',
        'py_stringmatching.similarity_measure.levenshtein.levenshtein',
    ),
    'JaroWinkler': (
        'jellyfish.jaro_winkler',
    ),
    'Hamming': (
        'jellyfish.hamming_distance',
        'abydos.distance.hamming',
    ),
}
