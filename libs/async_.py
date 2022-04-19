#!/usr/bin/env python3
"""async based routines"""

import logging

logger = logging.getLogger("ASYNC_")


def async_(args=None):
    logger.info("async_")

    if args:
        print(vars(args))
        logger.info(vars(args))
