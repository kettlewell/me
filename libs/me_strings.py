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

    s1 = "thistt"
    s2 = "histt"
    anagram(s1,s2)
    
    rewrite_immutable()
    
    '''
    Builtin Types List:
    str
    int
    float
    complex
    list
    tuple
    range
    dict
    set
    frozenset
    bool
    bytes
    bytearray
    memoryview
    '''
    str_type = str()
    int_type = int()
    float_type = float()
    complex_type = complex()
    lst_type = list()
    tuple_type = tuple()
    range_type = range(0)
    dict_type = dict()
    set_type = set()
    frozenset_type = frozenset()
    bool_type = bool()
    bytes_type = bytes()
    bytearray_type = bytearray()
    memoryview_type = memoryview(bytearray_type)   

    obj_functions(str_type)
    obj_functions(int_type)    
    obj_functions(float_type)

    obj_functions(complex_type)
    obj_functions(lst_type)
    obj_functions(tuple_type)
    obj_functions(range_type)
    obj_functions(dict_type)
    obj_functions(set_type)
    obj_functions(frozenset_type)
    obj_functions(bool_type)
    obj_functions(bytes_type)
    obj_functions(bytearray_type)
    obj_functions(memoryview_type)


    
def obj_functions(obj='str', pub=True, pri=False, dunder=False, gen_func=False):
    """
    Get a list of all the functions/methods available to arbitrary objects
    
    @param obj: object type
    @param pub: public methods
    @param pri: private methods
    @param dunder: dunder methods
    @param gen_func: generate the function def template for the type module test files.
    
    """ 
    import re
    
    obj_type = type(obj).__name__
    logger.debug("Object Type:  %s", obj_type)
    
    if pub:
        pub_pattern = '^[0-9a-zA-Z]'
        pub_funcs = [func for func in dir(obj) if re.search(pub_pattern,func)]
        logger.info(pub_funcs)

        if gen_func:
            for pub_func in pub_funcs:
                print("def {}_{}(): {{ }}".format(obj_type, pub_func))
        
        print()
        
    if dunder:
        dunder_pattern = '^__[0-9a-zA-Z]'
        dunder_funcs = [func for func in dir(obj) if re.search(dunder_pattern,func)]
        logger.info(dunder_funcs)
        if gen_func:
            for dunder_func in dunder_funcs:
                print("def {}_{}(): {{ }}".format(obj_type, dunder_func))
        print()
            
    if pri:
        pri_pattern = '^_[0-9a-zA-Z]'
        pri_funcs = [func for func in dir(obj) if re.search(pri_pattern,func)]
        logger.info(pri_funcs)
        if gen_func:
            for pri_func in pri_funcs:
                print("def {}_{}(): {{ }}".format(obj_type, pri_func))
        print()
    

# we can't really re-write a string
# but we can use recipes to copy the string back to itself
def rewrite_immutable():
    title = "Recipe 5: some immutable string, with, punctuation"
    
    colon_position = title.index(":")

    logger.info("colon_position: %s", colon_position)

    pre_colon, post_colon = title[:colon_position], title[colon_position+1:]

    logger.info("pre_colon: %s", pre_colon)
    logger.info("post_colon: %s", post_colon)

    pre_colon, middle, post_colon = title.partition(':')
    logger.info("pre_colon: %s", pre_colon)
    logger.info("middle: %s", middle)
    
    logger.info("post_colon: %s", post_colon)

    print()
    
def anagram(s1,s2):
    from collections import Counter
    logger.info(Counter(s1))
    logger.info(Counter(s2))
    
    logger.info("anagram") if Counter(s1) == Counter(s2) else logger.info("NOT anagram")
    
    print()
    
def remove_digits(str):
    res = ''.join(list(filter(lambda x: x.isalpha(), str)))
    logger.info("str with no digits: %s", res)
    print()

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

