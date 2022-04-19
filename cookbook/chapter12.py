#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 12"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH12")


def cookbook_chapter12(args=None):
    logger.info("cookbook_chapter12")
    if args:
        pp.pprint(args)
