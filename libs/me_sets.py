#!/usr/bin/env python3
'''Sets based routines'''

import logging

logger = logging.getLogger('SETS')

def me_sets(args=None):
    logger.info("me_sets")

    if args:
        print(vars(args))
        logger.info(vars(args))
