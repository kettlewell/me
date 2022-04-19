#!/usr/bin/env python3
"""Multi Processing based routines"""

import logging

logger = logging.getLogger("MP")


def multiprocessing(args=None):
    logger.info("multiprocessing")

    if args:
        print(vars(args))
        logger.info(vars(args))
