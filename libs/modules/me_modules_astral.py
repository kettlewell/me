#!/usr/bin/env python3
'''Astral module tests'''
import logging
logger = logging.getLogger('ASTRAL')

def me_modules_astral(args=None):
    logger.info("me_modules_astral")

    if args:
        print(vars(args))
        logger.info(vars(args))

