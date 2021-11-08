#!/usr/bin/env python3
'''Lists based routines'''

import logging

logger = logging.getLogger('LISTS')

def me_lists(args=None):
    logger.info("me_lists")

    if args:
        print(vars(args))
        logger.info(vars(args))
