#!/usr/bin/env python3
"""Compression based routines"""

import logging

logger = logging.getLogger("COMPRESS")


def compression(args=None):
    logger.info("compression")

    if args:
        print(vars(args))
        logger.info(vars(args))
