#!/usr/bin/env python3
"""Astral module tests"""
import logging
import astral

logger = logging.getLogger("ASTRAL")


def astral_module(args=None):
    logger.info("astral")

    if args:
        print(vars(args))
        logger.info(vars(args))
