#!/usr/bin/env python3
'''Scope based routines'''

import logging
import math
import libs.me_decorators

logger = logging.getLogger('SCOPE')

# global variable
g_size = 10000

def me_scope(args=None):
    logger.debug("me_scope")

    # according to a medium article I read, the loop that uses the global
    # variable runs slower... but when I tested the two different approaches, 
    # I found them to run nearly identically - could be a python version difference
    global_loops()
    local_loops()

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
