#!/usr/bin/env python3
'''Builtin Functions based routines'''

import logging

logger = logging.getLogger('FUNCTIONS')

def me_functions(args=None):
    logger.info("me_functions")

    if args:
        print(vars(args))
        logger.info(vars(args))
