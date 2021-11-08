#!/usr/bin/env python3
'''Dicts based routines'''

import logging

logger = logging.getLogger('DICTS')

def me_dicts(args=None):
    logger.info("me_dicts")

    if args:
        print(vars(args))
        logger.info(vars(args))

    logger.info("Relation to Leia :  " + relation_to_luke('Leia'))
    logger.info("Relation to Vader:  " + relation_to_luke("Darth Vader"))
    logger.info("Relation to Han  :  " + relation_to_luke("Han"))
    logger.info("Relation to R2D2 :  " + relation_to_luke("R2D2"))

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
