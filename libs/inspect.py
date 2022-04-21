#!/usr/bin/env python3
"""inspect module tests"""
import os
import inspect
import pprint as pp

import logging

logger = logging.getLogger("INSPECT")


def inspect_module(args=None):
    logger.debug("modules_inspect")

    inspect_testing(args)


def inspect_testing(args):

    module_path3 = inspect.getfile(inspect.currentframe())
    module_path4 = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    logger.info("module_path3: " + module_path3)
    logger.info("module_path4: " + module_path4)

    # filename at top of stack
    pp.pprint(inspect.stack()[0][1])

    # filename at bottom of stack
    pp.pprint(inspect.stack()[-1][1])


#    pp.pprint(inspect.stack())
