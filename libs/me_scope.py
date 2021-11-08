#!/usr/bin/env python3
'''Scope based routines'''

import logging

logger = logging.getLogger('SCOPE')

def me_scope(args=None):
    logger.info("me_scope")

    if args:
        print(vars(args))
        logger.info(vars(args))
