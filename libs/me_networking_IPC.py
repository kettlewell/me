#!/usr/bin/env python3
'''Network and IPC based routines'''

import logging

logger = logging.getLogger('NET_IPC')

def me_network(args=None):
    logger.info("me_network")

    if args:
        print(vars(args))
        logger.info(vars(args))
