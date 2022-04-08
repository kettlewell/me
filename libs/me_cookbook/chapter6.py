#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 6"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH6")


def me_cookbook_chapter6(args=None):
    logger.info("me_cookbook_chapter6")
    if args:
        pp.pprint(args)
