#!/usr/bin/env python3
"""Generators based routines"""

import logging

logger = logging.getLogger("GENERATOR")


def me_generators(args=None):
    logger.debug("me_generators")

    c = {x for x in "abracadabra" if x not in "abc"}
    logger.info(c)
