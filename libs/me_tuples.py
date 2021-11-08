#!/usr/bin/env python3
'''Tuples based routines'''

import logging

logger = logging.getLogger('TUPLES')

def me_tuples(args=None):
    logger.info("me_tuples")

    if args:
        print(vars(args))
        logger.info(vars(args))
