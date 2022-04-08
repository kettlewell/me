#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 4"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH4")


def me_cookbook_chapter4(args=None):
    logger.info("me_cookbook_chapter4")
    if args:
        pp.pprint(args)
