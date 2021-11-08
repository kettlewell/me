#!/usr/bin/env python3
'''UNIC based routines'''

import logging

logger = logging.getLogger('UNIX')

def me_unix(args=None):
    logger.info("me_unix")

    if args:
        print(vars(args))
        logger.info(vars(args))
