#!/usr/bin/env python3
"""Scope based routines"""

import logging
import math
import libs.me_decorators

logger = logging.getLogger("SCOPE")

# global variable
g_size = 10


def me_scope(args=None):
    logger.debug("me_scope")

    # according to a medium article I read, the loop that uses the global
    # variable runs slower... but when I tested the two different approaches,
    # I found them to run nearly identically - could be a python version difference
    global_loops()
    local_loops()

    # the premise here, is that the dot notation causes excess dict calls
    # slowing down progress, and that using functors remedies this
    # verdict: with millions of lines, I see a small difference ( 10s vs 16s)
    # I do appreciate the clean look, so I'm not opposed to using it,
    # but this does fall into the "premature optimization" category
    no_dots()
    with_dots()

    scope_understanding_variables()


def scope_understanding_variables():
    """
    http://foobarnbaz.com/2012/07/08/understanding-python-variables/
    https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/
    """
    list = [0]
    lid = id(list)
    logger.info(f"initial List ID: {lid}")
    logger.info(f"initial list:  {list}")

    scope_do_nothing(list)
    lid = id(list)
    logger.info(f"after scope_do_nothing List ID: {lid}")
    logger.info(f"scope_do_nothing: {list}")

    scope_reassign(list)
    lid = id(list)
    logger.info(f"after scope_reassign List ID: {lid}")
    logger.info(f"scope_reassign: {list}")

    scope_append(list)
    lid = id(list)
    logger.info(f"after scope_append List ID: {lid}")
    logger.info(f"scope_append: {list}")

    logger.info("")

    lstA = [100000]
    lid = id(lstA)
    logger.info(f"lstA List ID: {lid}")
    logger.info(f"lstA: {lstA}")

    lstB = lstA
    lid = id(lstB)
    logger.info(f"lstB List ID: {lid}")
    logger.info(f"lstB: {lstB}")

    lstB.append(1)
    lid = id(lstB)
    logger.info(f"lstB List ID: {lid}")
    logger.info(f"lstA: {lstA}")
    logger.info(f"lstB: {lstB}")

    logger.info("")

    # interning... where shorter / common items refer to the same memory object
    # in python 3.10, I can't get interning to let loose, even with over 1024 character strings...
    # figured it out with the help of:
    # http://guilload.com/python-string-interning/

    s1 = "hello"
    s2 = "hello"
    s3 = 1000 * "hello wonderful world"
    s4 = 1000 * "hello wonderful world"

    i1 = 5
    i2 = 5
    i3 = 10000 ** 20
    i4 = 10000 ** 20

    si1 = int("257")
    si2 = int("257")

    lid_s1 = id(s1)
    lid_s2 = id(s2)
    lid_s3 = id(s3)
    lid_s4 = id(s4)
    lid_i1 = id(i1)
    lid_i2 = id(i2)
    lid_i3 = id(i3)
    lid_i4 = id(i4)
    lid_si1 = id(si1)
    lid_si2 = id(si2)

    logger.info(f"List ID S1: {lid_s1}")
    logger.info(f"List ID S2: {lid_s2}")
    logger.info(f"List ID S3: {lid_s3}")
    logger.info(f"List ID S4: {lid_s4}")
    logger.info(f"List ID I1: {lid_i1}")
    logger.info(f"List ID I2: {lid_i2}")
    logger.info(f"List ID I3: {lid_i3}")
    logger.info(f"List ID I4: {lid_i4}")

    logger.info(f"List ID SI1: {lid_si1}")
    logger.info(f"List ID SI2: {lid_si2}")

    if s1 is s2:
        logger.info("S1 is S2")
    else:
        logger.info("S1 is not S2")

    if s1 == s2:
        logger.info("S1 == S2")
    else:
        logger.info("S1 not == S2")

    if s3 is s4:
        logger.info("S3 is S4")
    else:
        logger.info("S3 is not S4")

    if s3 == s4:
        logger.info("S3 == S4")
    else:
        logger.info("S3 not == S4")

    if i1 is i2:
        logger.info("I1 is I2")
    else:
        logger.info("I1 is not I2")

    if i1 == i2:
        logger.info("I1 == I2")
    else:
        logger.info("I1 not == I2")

    if i3 is i4:
        logger.info("I3 is I4")
    else:
        logger.info("I3 is not I4")

    if i3 == i4:
        logger.info("I3 == I4")
    else:
        logger.info("I3 not == I4")

    if si1 is si2:
        logger.info("SI1 is SI2")
    else:
        logger.info("SI1 is not SI2")

    if si1 == si2:
        logger.info("SI1 == SI2")
    else:
        logger.info("SI1 not == SI2")

    class Foo:
        pass

    bar = Foo
    baz = Foo
    logger.info(id(bar))
    logger.info(id(baz))

    bar = Foo()
    baz = Foo()
    logger.info(id(bar))
    logger.info(id(baz))

    # '*' operator always copies references:
    # ie, the memory address will always be the same
    #
    x = [Foo()] * 5
    logger.info([id(e) for e in x])

    # the '+' operator also copies by reference
    # hence all the memory locations are identical at startup
    foo = Foo()
    data = [foo]
    new_data = data + data + data

    logger.info([id(e) for e in new_data])

    # this seems to be a contrived way to create different instances
    new_foos = [Foo() for _ in range(5)]
    logger.info([id(e) for e in new_foos])


def scope_do_nothing(list):
    list
    lid = id(list)
    logger.info(f"scope_do_nothing List ID: {lid}")


def scope_reassign(list):
    list = [0, 1]
    lid = id(list)
    logger.info(f"scope_reassign List ID: {lid}")


def scope_append(list):
    list.append(1)
    lid = id(list)
    logger.info(f"scope_append List ID: {lid}")


@libs.me_decorators.timer
def no_dots():
    l_size = 1000
    result = []
    append = result.append
    sqrt = math.sqrt
    for x in range(l_size):
        append(sqrt(x))
    # logger.info("sqrt without dots is: %s", result)


@libs.me_decorators.timer
def with_dots():
    l_size = 1000
    result = []
    for x in range(l_size):
        result.append(math.sqrt(x))
    # logger.info("sqrt with dots is: %s", result)


@libs.me_decorators.timer
def global_loops():
    for x in range(g_size):
        for y in range(g_size):
            z = math.sqrt(x) + math.sqrt(y)  # noqa: F841


@libs.me_decorators.timer
def local_loops():
    l_size = 10
    for x in range(l_size):
        for y in range(l_size):
            z = math.sqrt(x) + math.sqrt(y)  # noqa: F841
