#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 8"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH8")


def me_cookbook_chapter8(args=None):
    logger.info("me_cookbook_chapter8")
    if args:
        pp.pprint(args)
