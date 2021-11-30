#!/usr/bin/env python3
'''Builtin Functions based routines'''

import pprint as pp
import logging

logger = logging.getLogger('FUNCTIONS')

def me_functions(args=None):
    logger.info("me_functions")

    if args:
        print(vars(args))
        logger.info(vars(args))

    logger.info(help(foo))

    foo(1,2,3,4,e=5,f=6,g=7)

    logger.info('empty')

    bar(100)

    logger.info(pp.pprint(locals()))
    logger.info(pp.pprint(globals()))
    logger.info(pp.pprint(dir()))


    # Define a list for demonstration purposes
    myList    = ["Left", "Right", "Up", "Down"]

    # Define a dictionary for demonstration purposes
    myDict    = {"Wubba": "lubba", "Dub": "dub"}

    # Define a dictionary to feed y
    myArgDict = {'y': "Why?", 'y0': "Why not?", "q": "Here is a cue!"}

    # The 1st elem of myList feeds y
    ff("myEx", *myList, **myDict)
    ff('myEx', **myArgDict)
    ff('myEx', *myArgDict)
    ff('myEx', 4, 42, 420, *myList, *myDict, **myDict)
    ff(myList, myDict)


    # augmented assignment operator

some_value = 5

some_value **= 2

#print(some_value)


#print(type("hi hellow there 24"))


def foo(a, b=10, *args, **kwargs):
    '''
    this function takes required argument a, not required keyword argument b
    and any number of unknown positional arguments and keyword arguments after
    '''
    logger.info('a is a required argument, and its value is {0}'.format(a))
    logger.info('b not required, its default value is 10, actual value: {0}'.format(b))
    # we can inspect the unknown arguments we were passed:
    #  - args:
    logger.info('args is of type {0} and length {1}'.format(type(args), len(args)))
    for arg in args:
        logger.info('unknown arg: {0}'.format(arg))
    #  - kwargs:
    logger.info('kwargs is of type {0} and length {1}'.format(type(kwargs),
                                                        len(kwargs)))
    for kw, arg in kwargs.items():
        logger.info('unknown kwarg - kw: {0}, arg: {1}'.format(kw, arg))
    # But we don't have to know anything about them 
    # to pass them to other functions.
    logger.info('Args or kwargs can be passed without knowing what they are.')
    # max can take two or more positional args: max(a, b, c...)
    logger.info('e.g. max(a, b, *args) \n{0}'.format(
      max(a, b, *args))) 
    kweg = 'dict({0})'.format( # named args same as unknown kwargs
      ', '.join('{k}={v}'.format(k=k, v=v) 
                             for k, v in sorted(kwargs.items())))
    logger.info('e.g. dict(**kwargs) (same as {kweg}) returns: \n{0}'.format(
      dict(**kwargs), kweg=kweg))


def bar(a):
    b,c,d,e,f = 2,3,4,5,6
    foo(**locals())


def ff(x, y, *myArgs, **myKW):
    logger.info("# x      = {}".format(x))
    logger.info("# y      = {}".format(y))
    logger.info("# myArgs = {}".format(myArgs))
    logger.info("# myKW   = {}".format(myKW))
    logger.info("# ----------------------------------------------------------------------")
