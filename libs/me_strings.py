#!/usr/bin/env python3
'''Strings based routines'''
from functools import lru_cache
import os
import builtins
import logging
import libs.me_decorators

import string

logger = logging.getLogger('STRINGS')

def me_strings(args=None):
    logger.debug("me_strings")

    lc_alphabet()
    uc_alphabet()
    str_digits()
    str_with_digits = 'ABC123DEF456GHI789JKL'
    remove_digits(str_with_digits)

def remove_digits(str):
    res = ''.join(list(filter(lambda x: x.isalpha(), str)))
    logger.info("str with no digits: %s", res)

def lc_alphabet():
    logger.info(string.ascii_lowercase)

def uc_alphabet():
    logger.info(string.ascii_uppercase)

def str_digits():
    logger.info(string.digits)


def from_practice(args):
    logger.info("hello as a stutter :  " + stutter('hello'))

    #search_help('builtins')
    #logger.info(help(builtins.dict))

    #somestring = "1\n\n,2,\n3,4,5,6\n\n\n\n"
    #sstring = somestring.split(',')
    #logger.info(type(sstring))
    #logger.info(sstring)

    #somestring = '1,2,3,4,5,6\n\n\n\n'
    #sstring = somestring.splitlines()
    #logger.info(type(sstring))
    #logger.info(sstring)

    #sstring = somestring
    #sstring = somestring.strip('\n')
    #logger.info(type(sstring))
    #logger.info(sstring)

    join_objects_as_strings(lst)


def join_objects_as_strings(lst):
    # Join objects as strings
    # https://blog.finxter.com/how-to-use-pythons-join-function-on-a-list-of-objects-rather-than-strings/

    join_method_1(lst)
    join_method_2(lst)
    join_method_3(lst)
    join_method_4(lst)
    join_method_5(lst)
    join_method_6(lst)


@libs.me_decorators.timer
def join_method_1(lst):
    # Method 1 - list comprehension with join
    logger.info(''.join([str(x) for x in lst]))
    #''.join([str(x) for x in lst])
    
    # 0124
@libs.me_decorators.timer
def join_method_2(lst):
    # Method 2 - generator expression 
    logger.info(''.join(str(x) for x in lst))
    #''.join(str(x) for x in lst)
    
    # 0124
@libs.me_decorators.timer
def join_method_3(lst):
    # Method 3 - generator expression with custom string repr
    logger.info(''.join(str(x.val) for x in lst))
    #''.join(str(x.val) for x in lst)
    # 0124

@libs.me_decorators.timer
def join_method_4(lst):
    # Method 4 - lambda + str
    logger.info(''.join(map(lambda x: str(x), lst)))
    #''.join(map(lambda x: str(x), lst))
    # 0124

@libs.me_decorators.timer
def join_method_5(lst):
    # Method 5 - map + str
    logger.info(''.join(map(str, lst)))
    #''.join(map(str, lst))
    # 0124

@libs.me_decorators.timer
def join_method_6(lst):
    # Method 6 - naive loop
    s = ''
    for x in lst:
        s += str(x)
    logger.info(s)
    # 0124
class Obj:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

#lst = [Obj(0), Obj(1), Obj(2), Obj(4)]

lst = [Obj(x) for x in range(0,10)]

# STRING
# create a stuttering type string response
def stutter(word):
    return word[:2] + '...' + word[:2] + '...' + word + '?'


def search_help(keyword):
    os.system('pydoc -k {}'.format(keyword))

