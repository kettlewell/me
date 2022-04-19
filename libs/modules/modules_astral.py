#!/usr/bin/env python3
"""Astral module tests"""
import logging

logger = logging.getLogger("ASTRAL")


def modules_astral(args=None):
    logger.info("modules_astral")

    if args:
        print(vars(args))
        logger.info(vars(args))
