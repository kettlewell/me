#!/usr/bin/env python3
'''Regex based routines'''

import logging

logger = logging.getLogger('RE')

def me_re(args=None):
    logger.info("me_re")

    if args:
        print(vars(args))
        logger.info(vars(args))
