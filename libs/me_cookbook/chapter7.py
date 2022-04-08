#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 7"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH7")


def me_cookbook_chapter7(args=None):
    logger.info("me_cookbook_chapter7")
    if args:
        pp.pprint(args)
