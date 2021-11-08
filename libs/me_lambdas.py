#!/usr/bin/env python3
'''Lambdas based routines'''

import logging

logger = logging.getLogger('LAMBDAS')

def me_lambdas(args=None):
    logger.info("me_lambdas")

    if args:
        print(vars(args))
        logger.info(vars(args))
