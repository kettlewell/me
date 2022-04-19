#!/usr/bin/env python3
"""Exceptions based routines"""

import sys
import logging

logger = logging.getLogger("EXCEPTIONS")


def exceptions(args=None):
    logger.debug("exceptions")

    # # #
    # these need to be commented out one by one
    #
    ### exception_divide_by_zero()
    ### exception_bad_catch()
    ## exception_no_catch()

    # exceptions_raises()

    exceptions_multiple_catch()


def exceptions_multiple_catch():
    try:
        raise ValueError("value issues again")
    except (ValueError, KeyError, ArithmeticError) as e:
        print("Execution Caught: ", e)
        raise ArithmeticError("reraising cain")
        print("after raising...")


def exceptions_raises():

    raise Exception("uh oh")
    try:
        raise ValueError("value issues again")
    except ValueError:
        raise


def exception_no_catch():
    try:
        raise Exception("general exceptions not caught by specific handling")
    except ValueError as e:
        print("we will not catch exception: Exception {}".format(str(e)))
        raise


def exception_bad_catch():
    try:
        raise ValueError("Represents a hidden bug, do not catch this")
        raise Exception("This is the exception you expect to handle")
    except Exception as error:  # noqa: B902
        print("Caught this error: " + repr(error))
        raise
    except:  # noqa: E722 B001
        print("catch-all except")
        print(sys.exc_info())
        raise


def exception_divide_by_zero():

    try:
        0 / 0
    except (KeyError, ValueError, ZeroDivisionError) as exc_inst:
        logger.error("DIV by ZERO: {}".format(str(exc_inst)))

        raise exc_inst
