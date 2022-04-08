#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 14"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH14")


def me_cookbook_chapter14(args=None):
    logger.info("me_cookbook_chapter14")
    if args:
        pp.pprint(args)
