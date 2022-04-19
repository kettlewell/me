#!/usr/bin/env python3
"""Comparison based routines"""

import logging

logger = logging.getLogger("COMPARE")


def comparisons(args=None):
    logger.info("comparisons")

    if args:
        print(vars(args))
        logger.info(vars(args))
