#!/usr/bin/env python3
'''Regex based routines'''

import logging
import re

logger = logging.getLogger('RE')

def me_re(args=None):
    logger.info("me_re")

    if args:
        print(vars(args))
        logger.info(vars(args))

    regex = re.compile(r'abc.*123')
    str1 = "ABCabcwhoami123DEF"
    str2 = "abcwhoami123456"
    str3 = "1abcwhoami123"
    str4 = "abc123whoami123"
    str5 = "abc123"

    matchme(regex,str1)
    matchme(regex,str2)
    matchme(regex,str3)
    matchme(regex,str4)
    matchme(regex,str5)

    p1 = re.compile(r'\W+')
    p2 = re.compile(r'(\W+)')
    splitstr = 'This...is a semi-long test of the something system'
    p1_res = p1.split(splitstr)
    p2_res = p2.split(splitstr)

    logger.info(type(p1_res))
    logger.info(type(p2_res))
    logger.info(p1_res)
    logger.info(p2_res)


def matchme(regex, str):
    #print(str)
    m = regex.search(str)
    if m:
        msg = "we have a match"
    else:
        msg = "sorry... no matchy"
    logger.info('{0:<25s} : {1:>30}'.format(msg,str))

    s = regex.split(str)
    logger.info(s)

    if m:
        logger.info("{}:{}\n".format(m.span(),s))
    else:
        logger.info("{}\n".format(s))