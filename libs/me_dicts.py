#!/usr/bin/env python3
'''Dicts based routines'''

import logging

logger = logging.getLogger('DICTS')

def me_dicts(args=None):
    logger.info("me_dicts")

    if args:
        print(vars(args))
        logger.info(vars(args))
