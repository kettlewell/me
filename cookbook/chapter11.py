#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 11"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH11")


def cookbook_chapter11(args=None):
    logger.info("cookbook_chapter11")
    if args:
        pp.pprint(args)
