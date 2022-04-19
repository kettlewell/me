#!/usr/bin/env python3
"""Dicts based routines"""

import logging
import pprint as pp

logger = logging.getLogger("DICTS")


def dicts(args=None):
    logger.debug("dicts")

    d1 = {"name": "tony", "age": 23}
    d2 = {"city": "paris"}
    merge_dicts(d1, d2)

    key_dict = {"one": 1, "four": 4, "eight": 8}
    val_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

    sort_by_key(key_dict)
    sort_by_val(val_dict)
    sorted_keys(key_dict)
    sorted_keys(val_dict)
    extract_dict_subset()


# python cookbook 1.17 - extracting a subset of a dictionary
def extract_dict_subset():
    prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.67, "HPQ": 37.20, "FB": 10.75}

    p1 = {key: val for key, val in prices.items() if val > 40}

    tech_names = {"AAPL", "IBM", "HPQ", "MSFT"}
    p2 = {key: val for key, val in prices.items() if key in tech_names}

    logger.info(p1)
    logger.info(p2)


def sorted_keys(d):
    res1 = sorted(d.keys(), reverse=False)
    res2 = sorted(d.keys(), reverse=True)
    logger.info("sorted keys %s", res1)
    logger.info("reverse sorted keys %s", res2)


def sort_by_key(d):
    res = {key: d[key] for key in sorted(d.keys())}
    logger.info("sort dict by key %s", res)


def sort_by_val(d):
    res = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    logger.info("sort dict by key %s", res)


def merge_dicts(d1, d2):
    # logger.info(d1)
    d1.update(d2)
    logger.info("merged dicts: %s", d1)
    # logger.info(d2)


def from_practice(args):
    logger.info("Relation to Leia :  " + relation_to_luke("Leia"))
    logger.info("Relation to Vader:  " + relation_to_luke("Darth Vader"))
    logger.info("Relation to Han  :  " + relation_to_luke("Han"))
    logger.info("Relation to R2D2 :  " + relation_to_luke("R2D2"))

    basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
    # pp.pprint(sorted(basket))

    a = {x for x in "abracadabra" if x not in "abc"}
    # pp.pprint(sorted(a))

    sq = {x: 2**x for x in range(1, 21)}

    pp.pprint(sq)
    for k in sq.values():
        print(k)

    for i, v in enumerate(sq.items()):
        print(i, v)


# DICT
# relationship mapping
def relation_to_luke(name):
    relationships = {"Darth Vader": "father", "Leia": "sister", "Han": "brother in law", "R2D2": "droid"}
    return relationships[name]
