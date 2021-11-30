#!/usr/bin/env python3
'''Lambdas based routines'''

import logging

logger = logging.getLogger('LAMBDAS')

def me_lambdas(args=None):
    logger.debug("me_lambdas")

    list_filter()

def list_filter():
    lst = [x for x in range(50)]
    res = list(filter(lambda x: x%2 == 0, lst))
    logger.info(res)
