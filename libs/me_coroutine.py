#!/usr/bin/env python3
'''Regex based routines'''

import logging

logger = logging.getLogger('COROUTINE')

def me_coroutine(args=None):
    logger.info("me_coroutine")

    if args:
        print(vars(args))
        logger.info(vars(args))
