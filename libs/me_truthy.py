#!/usr/bin/env python3
'''Truthy based routines'''

import logging

logger = logging.getLogger('TRUTHY')

def me_truthy(args=None):
    logger.info("me_truthy")

    if args:
        print(vars(args))
        logger.info(vars(args))
