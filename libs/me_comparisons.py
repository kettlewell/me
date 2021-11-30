#!/usr/bin/env python3
'''Comparison based routines'''

import logging

logger = logging.getLogger('COMPARE')

def me_comparisons(args=None):
    logger.info("me_comparisons")

    if args:
        print(vars(args))
        logger.info(vars(args))
