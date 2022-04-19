#!/usr/bin/env python3
"""Threading based routines"""

import logging
import me.libs.decorators

logger = logging.getLogger("THREADING")


def threading(args=None):
    logger.debug("threading")

    basic_python_loop(10000000)


# https://towardsdatascience.com/which-is-faster-python-threads-or-processes-some-insightful-examples-26074e90848f
@me.libs.decorators.timer
def basic_python_loop(n):
    """Runs a simple native python loop which is memory light and involves no data input or output

    Args:
        n (int): count of number of loops
    """
    mydict = {}
    for i in range(n):
        mydict[i % 10] = i
    return None
