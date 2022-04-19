#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 4"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH4")


def cookbook_chapter4(args=None):
    logger.info("cookbook_chapter4")
    if args:
        pp.pprint(args)
