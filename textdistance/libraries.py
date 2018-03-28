LIBRARIES = {
    'DamerauLevenshtein': (
        'jellyfish.damerau_levenshtein_distance',
        'pyxdameraulevenshtein.damerau_levenshtein_distance',
        'abydos.distance.dist_damerau',
    ),
    'Levenshtein': (
        'jellyfish.levenshtein_distance',
        'abydos.distance.dist_levenshtein',
        'py_stringmatching.simfunctions.levenshtein',
    ),
    'JaroWinkler': (
        'jellyfish.jaro_winkler',
        'py_stringmatching.simfunctions.jaro_winkler',
    ),
    'Hamming': (
        'jellyfish.hamming_distance',
        'abydos.distance.dist_hamming',
        'py_stringmatching.simfunctions.hamming_distance',
    ),
    'Tversky': (
        'abydos.distance.dist_tversky',
    ),
    'NeedlemanWunsch': (
        'py_stringmatching.simfunctions.needleman_wunsch',
    ),
    'SmithWaterman': (
        'py_stringmatching.simfunctions.smith_waterman',
    ),
}
