#!/usr/bin/env python3
'''Lists based routines'''

import logging
import pprint as pp

from libs.me_utilities import log_values as lv
from libs.me_utilities import cmp_values as cv

logger = logging.getLogger('LISTS')

def me_lists(args=None):
    logger.info("me_lists")

    if args:
        print(vars(args))
        logger.info(vars(args))

    # initialize lists
    squares = [1, 4, 9, 16, 25]    

    # list indexing
    logger.info(squares[0])
    lv(1,squares[0])
    logger.info(cv(1,squares[0]))

    # list slicing


    # unpacking lists
    first, *rest = [1,2,3,4,5,6]
    logger.info("first: {}  rest: {}({})".format(first, rest, type(rest)))

    first, *l, last = [1,2,3,4,5,6]
    logger.info("first: {}  l: {} ({})  last: {} ({})".format(first, l, type(l), last, type(last)))


    # Sorting
    somelist = [1,10,99,98,101,-10,11]
    logger.info(somelist)
    somelist.sort()
    logger.info(sorted(somelist))

    logger.info(somelist)

    # list comprehension
    squares1 = [x**2 for x in range(0,10)]
    #pp.pprint(squares1)

    rval = [x for x in range(4)]
    #pp.pprint(rval)

    # List Zipping
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    #for q, a in zip(questions, answers):
    #    print('What is your {0}?  It is {1}.'.format(q, a))    
