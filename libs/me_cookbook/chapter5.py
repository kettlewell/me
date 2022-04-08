#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 5"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH5")


def me_cookbook_chapter5(args=None):
    logger.info("me_cookbook_chapter5")
    if args:
        pp.pprint(args)
