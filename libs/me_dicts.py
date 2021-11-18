#!/usr/bin/env python3
'''Dicts based routines'''

import logging
import pprint as pp

logger = logging.getLogger('DICTS')

def me_dicts(args=None):
    logger.debug("me_dicts")

    d1 = {'name': 'tony', 'age': 23}
    d2 = {'city': 'paris'}
    merge_dicts(d1,d2)


def merge_dicts(d1,d2):
    logger.info(d1)
    d1.update(d2)
    logger.info(d1)
    logger.info(d2)

def from_practice(args):
    logger.info("Relation to Leia :  " + relation_to_luke('Leia'))
    logger.info("Relation to Vader:  " + relation_to_luke("Darth Vader"))
    logger.info("Relation to Han  :  " + relation_to_luke("Han"))
    logger.info("Relation to R2D2 :  " + relation_to_luke("R2D2"))


    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    #pp.pprint(sorted(basket))

    a = {x for x in 'abracadabra' if x not in 'abc'}
    #pp.pprint(sorted(a))

    sq = {x: 2**x for x in range(1,21)}

    pp.pprint(sq)
    for k in sq.values():
        print(k)


    for i,v in enumerate(sq.items()):
        print(i,v)    


# DICT
# relationship mapping
def relation_to_luke(name):
    relationships = {
        "Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "droid"
        }
    return relationships[name]
