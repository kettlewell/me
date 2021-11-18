#!/usr/bin/env python3
'''Lists based routines'''

import logging
import pprint as pp

from libs.me_utilities import log_values as lv
from libs.me_utilities import cmp_values as cv

logger = logging.getLogger('LISTS')

def me_lists(args=None):
    logger.debug("me_lists")

    l1 = [1,2,3,4]
    l2 = ['batman']
    merge_lists(l1,l2)

    freq_list = [9,9,9,9,9,5,4,3,2,56,3,2,4]
    most_frequent_elem(freq_list)

    nested_list()
    
    dupe_list = [9,9,7,8,9,56,4,3,6,3,7]
    de_dupe_list(dupe_list)


def de_dupe_list(lst):
    res = list(set(lst))
    logger.info("de-duped list:  %s", res)

def nested_list():
    nums = [[num] for num in range(0,9)]
    logger.info(nums)

def most_frequent_elem(lst):
    most_frequent = max(set(lst), key=lst.count)
    logger.info(most_frequent)

# in-place list merge of l2 into l1
def merge_lists(l1,l2):
    logger.info(l1)
    l1.extend(l2)
    logger.info(l1)
    logger.info(l2)
    
def from_practice(args):
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
