#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 13"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH13")


def me_cookbook_chapter13(args=None):
    logger.info("me_cookbook_chapter13")
    if args:
        pp.pprint(args)
