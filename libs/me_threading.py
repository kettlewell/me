#!/usr/bin/env python3
'''Threading based routines'''

import logging

logger = logging.getLogger('THREADING')

def me_threading(args=None):
    logger.info("me_threading")

    if args:
        print(vars(args))
        logger.info(vars(args))
