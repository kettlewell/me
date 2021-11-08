#!/usr/bin/env python3
'''File and Directory based routines'''

import logging

logger = logging.getLogger('FILEDIR')

def me_filedir(args=None):
    logger.info("me_filedir")

    if args:
        print(vars(args))
        logger.info(vars(args))
