import itertools
import sys
from collections import defaultdict
from typing import List, Dict, Type

import atheris

from fuzz_helpers import EnhancedFuzzedDataProvider
from dataclasses import dataclass, field

with atheris.instrument_imports():
    import textdistance


@dataclass
class InitializationConstraints:
    """
    Tracks if a given class has the qval and external construction parameters
    """
    HAS_QVAL: bool = field(default=True)
    HAS_EXTERNAL: bool = field(default=True)


@dataclass
class FuzzTarget:
    """
    Defines a class and method that is a possible fuzz candidate
    """
    algo_cls: type
    fuzz_func_name: str


ALGORITHMS = [textdistance.Hamming, textdistance.Bag, textdistance.Gotoh, textdistance.MLIPNS, textdistance.Levenshtein,
              textdistance.DamerauLevenshtein, textdistance.Jaro, textdistance.JaroWinkler, textdistance.StrCmp95,
              textdistance.NeedlemanWunsch,
              textdistance.SmithWaterman, textdistance.Jaccard, textdistance.Sorensen,
              textdistance.Tversky, textdistance.Overlap, textdistance.Cosine, textdistance.Tanimoto,
              textdistance.MongeElkan,
              textdistance.LCSSeq, textdistance.LCSStr, textdistance.RatcliffObershelp, textdistance.ArithNCD,
              textdistance.RLENCD,
              textdistance.BWTRLENCD, textdistance.SqrtNCD, textdistance.BZ2NCD, textdistance.LZMANCD,
              textdistance.ZLIBNCD, textdistance.MRA, textdistance.Editex, textdistance.Prefix, textdistance.Length,
              textdistance.Identity,
              textdistance.Matrix]

FUZZ_METHODS = ["__call__", "distance", "similarity", "normalized_distance", "normalized_similarity"]

FUZZ_TARGETS: List[FuzzTarget] = []

CONSTRAINT_MEMORY: Dict[Type, InitializationConstraints] = defaultdict(InitializationConstraints)


def initialize_fuzz_options():
    """
    Initializes a cross-product of valid fuzzing targets and methods
    """
    global FUZZ_TARGETS

    FUZZ_TARGETS = [FuzzTarget(algo, func) for algo, func in itertools.product(ALGORITHMS, FUZZ_METHODS) if
                    hasattr(algo, func)]


def pick_qval(fdp: EnhancedFuzzedDataProvider):
    """
    Let atheris pick a qval to use for this current iteration (None, 1, or 2+)
    """
    if fdp.ConsumeBool():
        return fdp.ConsumeIntInRange(1, 100)
    else:
        return None


def TestOneInput(data):
    fdp = EnhancedFuzzedDataProvider(data)

    # Pick a target
    fuzz_target: FuzzTarget = fdp.PickValueInList(FUZZ_TARGETS)
    constraints = CONSTRAINT_MEMORY[fuzz_target.algo_cls]

    try:
        if constraints.HAS_QVAL and constraints.HAS_EXTERNAL:
            algo = fuzz_target.algo_cls(qval=pick_qval(fdp), external=False)
        elif constraints.HAS_QVAL:
            algo = fuzz_target.algo_cls(qval=pick_qval(fdp))
        elif constraints.HAS_EXTERNAL:
            algo = fuzz_target.algo_cls(external=False)
        else:
            algo = fuzz_target.algo_cls()
    except TypeError as e:
        # Update our memory on if a given parameter is invalid
        if 'qval' in str(e):
            constraints.HAS_QVAL = False
        elif 'external' in str(e):
            constraints.HAS_EXTERNAL = False
        return -1

    try:
        getattr(algo, fuzz_target.fuzz_func_name)(fdp.ConsumeRandomString(), fdp.ConsumeRandomString())
    except AttributeError as e:
        # Pops too often, just catch and ignore
        if 'split' in str(e):
            return -1
    except ImportError:
        # Remove this algorithm from the list, since we don't have pre-reqs to use it
        FUZZ_TARGETS.remove(fuzz_target)
        return -1


def main():
    initialize_fuzz_options()
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
