#!/usr/bin/env python3
"""Sets based routines"""

from itertools import chain, combinations
from typing import Collection, Iterable, Optional

import logging

logger = logging.getLogger("SETS")


def sets(args=None):
    logger.debug("sets")
    s1 = {0, 1, 2, 3, 4, 0, 3, 2, 1}
    s2 = {11, 22, 33, 44, 33, 22, 11}
    merge_sets(s1, s2)


def merge_sets(s1, s2):
    logger.info(s1)
    s1.update(s2)
    logger.info(s1)
    logger.info(s2)


def from_practice(args):
    fruits = ["apple", "banana", "orange", "mango", "pineapple"]
    fruits_powerset = list(subsets(fruits))
    fruits_subsets_1to3 = list(subsets(fruits, min_size=1, max_size=3))

    print(f"Power set of {fruits}: {fruits_powerset}", end="\n\n")
    print(f"Subsets of {fruits} of size 1 to 3: {fruits_subsets_1to3}")


# https://python.plainenglish.io/a-python-recipe-for-generating-subsets-a4a4e191df3d
# https://en.wikipedia.org/wiki/Power_set
#
def subsets(collection: Collection, min_size: int = 0, max_size: Optional[int] = None) -> Iterable:
    """Produce all the subsets of `collection` with cardinalities between
    `min_size` and `max_size` (inclusive)."""

    min_size = max(0, min_size)
    max_size = max_size if max_size is not None else len(collection)

    return chain(*{map(set, combinations(collection, r)) for r in range(min_size, max_size + 1)})
