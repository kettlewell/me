#!/usr/bin/env python3
'''Generators based routines'''

import logging

logger = logging.getLogger('GENERATOR')

def me_generators(args=None):
    logger.info("me_generators")

    if args:
        print(vars(args))
        logger.info(vars(args))
