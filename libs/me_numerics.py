#!/usr/bin/env python3
'''Numerics based routines'''

import logging

logger = logging.getLogger('NUMBERICS')

def me_numerics(args=None):
    logger.info("me_numerics")

    if args:
        print(vars(args))
        logger.info(vars(args))
