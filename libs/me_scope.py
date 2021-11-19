#!/usr/bin/env python3
'''Scope based routines'''

import logging
import math
import libs.me_decorators

logger = logging.getLogger('SCOPE')

# global variable
g_size = 10

def me_scope(args=None):
    logger.debug("me_scope")

    # according to a medium article I read, the loop that uses the global
    # variable runs slower... but when I tested the two different approaches, 
    # I found them to run nearly identically - could be a python version difference
##    global_loops()
##    local_loops()

    # the premise here, is that the dot notation causes excess dict calls
    # slowing down progress, and that using functors remedies this
    # verdict: with millions of lines, I see a small difference ( 10s vs 16s)
    # I do appreciate the clean look, so I'm not opposed to using it,
    # but this does fall into the "premature optimization" category
    no_dots()
    with_dots()


@libs.me_decorators.timer
def no_dots():
    l_size = 100000000
    result = []
    append = result.append
    sqrt = math.sqrt
    for x in range(l_size):
        append(sqrt(x))
    #logger.info("sqrt without dots is: %s", result)

@libs.me_decorators.timer
def with_dots():
    l_size = 100000000
    result = []
    for x in range(l_size):
        result.append(math.sqrt(x))
    #logger.info("sqrt with dots is: %s", result)

@libs.me_decorators.timer
def global_loops():
    for x in range(g_size):
        for y in range(g_size):
            z = math.sqrt(x) + math.sqrt(y)

@libs.me_decorators.timer
def local_loops():
    l_size = 10000
    for x in range(l_size):
        for y in range(l_size):
            z = math.sqrt(x) + math.sqrt(y)
