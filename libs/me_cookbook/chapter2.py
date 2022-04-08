#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 2"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH2")


def me_cookbook_chapter2(args=None):
    logger.info("me_cookbook_chapter2")
    if args:
        pp.pprint(args)
