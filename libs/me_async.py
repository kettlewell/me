#!/usr/bin/env python3
'''async based routines'''

import logging

logger = logging.getLogger('ASYNC')

def me_async(args=None):
    logger.info("me_async")

    if args:
        print(vars(args))
        logger.info(vars(args))
