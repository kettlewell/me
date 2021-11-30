#!/usr/bin/env python3
'''Internet based routines'''

import logging

logger = logging.getLogger('INTERNET')

def me_internet(args=None):
    logger.info("me_internet")

    if args:
        print(vars(args))
        logger.info(vars(args))
