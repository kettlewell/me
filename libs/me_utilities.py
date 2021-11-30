#!/usr/bin/env python3
""" utility functions"""

import logging

logger = logging.getLogger(__name__)


def log_values(expected, actual):
    if cmp_values(expected, actual):
        logger.info("[OK] [ACTUAL] : " + str(actual) + "  [EXPECTED] : " + str(expected))
    else:
        logger.error("[ERROR] [ACTUAL] : " + str(actual) + "  [EXPECTED] : " + str(expected))


def cmp_values(expected, actual):  # noqa: CCR001

    # intialize types not same
    sameType = True

    # string compare
    if isinstance(expected, str) and isinstance(actual, str):
        pass
        # logger.info("expected value is STRING")

    # int compare
    elif isinstance(expected, int) and isinstance(actual, int):
        pass
        # logger.info("expected value is INT")

    # dict compare
    elif isinstance(expected, dict) and isinstance(actual, dict):
        pass
        # logger.info("expected value is DICT")

    # list compare
    elif isinstance(expected, list) and isinstance(actual, list):
        pass
        # logger.info("expected value is LIST")

    # tuple compare
    elif isinstance(expected, tuple) and isinstance(actual, tuple):
        pass
        # logger.info("expected value is TUPLE")

    # float compare
    elif isinstance(expected, float) and isinstance(actual, float):
        pass
        # logger.info("expected value is FLOAT")

    # bool compare
    elif isinstance(expected, bool) and isinstance(actual, bool):
        pass
        # logger.info("expected value is BOOL")

    # unknown
    else:
        logger.error("expected type is unknown or not same")
        sameType = False

    if sameType:
        return actual == expected
    else:
        return False  # noqa: WPS503


def obj_functions(  # noqa: WPS210 WPS213 CCR001
    ob="str", pub=True, pri=False, dunder=False, gen_func=False
):
    """
    Get a list of all the functions/methods available to arbitrary objects

    @param ob: object type
    @param pub: public methods
    @param pri: private methods
    @param dunder: dunder methods
    @param gen_func: generate the function def template for the type module test files.

    """
    import re

    ob_type = type(ob).__name__
    logger.debug("Object Type:  %s", ob_type)

    if pub:
        pub_pattern = "^[0-9a-zA-Z]"
        pub_funcs = [func for func in dir(ob) if re.search(pub_pattern, func)]
        logger.info(pub_funcs)

        if gen_func:
            for pub_func in pub_funcs:
                print("def {}_{}(): \n    pass\n\n".format(ob_type, pub_func))

            for pub_func in pub_funcs:
                print("{}_{}()".format(ob_type, pub_func))
        print()

    if dunder:
        dunder_pattern = "^__[0-9a-zA-Z]"
        dunder_funcs = [func for func in dir(ob) if re.search(dunder_pattern, func)]
        logger.info(dunder_funcs)
        if gen_func:
            for dunder_func in dunder_funcs:
                print("def {}_{}(): {{ }}".format(ob_type, dunder_func))
        print()

    if pri:
        pri_pattern = "^_[0-9a-zA-Z]"
        pri_funcs = [func for func in dir(ob) if re.search(pri_pattern, func)]
        logger.info(pri_funcs)
        if gen_func:
            for pri_func in pri_funcs:
                print("def {}_{}(): {{ }}".format(ob_type, pri_func))
        print()
