#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 9"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH9")


def me_cookbook_chapter9(args=None):
    logger.info("me_cookbook_chapter9")
    if args:
        pp.pprint(args)
