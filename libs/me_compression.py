#!/usr/bin/env python3
'''Compression based routines'''

import logging

logger = logging.getLogger('COMPRESS')

def me_compression(args=None):
    logger.info("me_compression")

    if args:
        print(vars(args))
        logger.info(vars(args))
