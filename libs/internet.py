#!/usr/bin/env python3
"""Internet based routines"""

import logging

logger = logging.getLogger("INTERNET")


def internet(args=None):
    logger.info("internet")

    if args:
        print(vars(args))
        logger.info(vars(args))
