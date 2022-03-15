#!/usr/bin/env python3
"""UNIX based routines"""
import os
import logging
import json

logger = logging.getLogger("UNIX")


def me_unix(args=None):
    logger.debug("me_unix")

    # os_environ()
    print_env()


def os_environ():
    print(len(list(os.environ)), " total env variables")

    logger.info(sorted(list(os.environ)))


def print_env():
    print(json.dumps({**{}, **os.environ}, indent=4))
