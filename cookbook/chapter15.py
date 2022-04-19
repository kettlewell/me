#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 15"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH15")


def cookbook_chapter15(args=None):
    logger.info("cookbook_chapter15")
    if args:
        pp.pprint(args)
