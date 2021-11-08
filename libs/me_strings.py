#!/usr/bin/env python3
'''Strings based routines'''

import logging

logger = logging.getLogger('STRINGS')

def me_strings(args=None):
    logger.info("me_strings")

    if args:
        print(vars(args))
        logger.info(vars(args))

    logger.info("hello as a stutter :  " + stutter('hello'))


# STRING
# create a stuttering type string response
def stutter(word):
    return word[:2] + '...' + word[:2] + '...' + word + '?'

#print(stutter("Hello"))
