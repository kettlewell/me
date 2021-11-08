#!/usr/bin/env python3
'''Iterators based routines'''

import logging

logger = logging.getLogger('ITERATORS')

def me_iterators(args=None):
    logger.info("me_iterators")

    if args:
        print(vars(args))
        logger.info(vars(args))




# ITERABLES
# first value of an iterable
def get_first_value(arr):
    return arr[0]
