#!/usr/bin/env python3
'''Multi Processing based routines'''

import logging

logger = logging.getLogger('MP')

def me_multiprocessing(args=None):
    logger.info("me_multiprocessing")

    if args:
        print(vars(args))
        logger.info(vars(args))
