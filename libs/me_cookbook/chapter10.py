#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 10"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH10")


def me_cookbook_chapter10(args=None):
    logger.info("me_cookbook_chapter10")
    if args:
        pp.pprint(args)
