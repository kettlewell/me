#!/usr/bin/env python3
'''Exceptions based routines'''

import logging

logger = logging.getLogger('EXCEPTIONS')

def me_exceptions(args=None):
    logger.info("me_exceptions")

    if args:
        print(vars(args))
        logger.info(vars(args))
