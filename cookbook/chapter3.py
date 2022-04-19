#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 3"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH3")


def cookbook_chapter3(args=None):
    logger.info("cookbook_chapter3")
    if args:
        pp.pprint(args)
