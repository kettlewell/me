#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 1"""

import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH1")


def me_cookbook_chapter1(args=None):
    logger.info("me_cookbook_chapter1")
    print("")
    chapter1_1()

    print("")
    chapter1_2()

    print("")
    chapter1_3()

    print("")
    chapter1_4()

    print("")
    chapter1_5()

    print("")
    chapter1_6()

    print("")
    chapter1_7()

    print("")
    chapter1_8()

    print("")
    chapter1_9()

    print("")
    chapter1_10()

    print("")
    chapter1_11()

    print("")
    chapter1_12()

    print("")
    chapter1_13()

    print("")
    chapter1_14()

    print("")
    chapter1_15()

    print("")
    chapter1_16()

    print("")
    chapter1_17()

    print("")
    chapter1_18()

    print("")
    chapter1_19()

    print("")
    chapter1_20()


# Unpacking a sequence into separate variables
def chapter1_1():
    logger.info("chapter1_1")
    logger.info("Unpacking a sequence into separate variables")
    print("")

    p = (4, 5)
    x, y = p
    logger.info("x: {}".format(x))
    logger.info("y: {}".format(y))
    print("")

    data = ["ACME", 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    logger.info("name: {}".format(name))
    logger.info("shares: {}".format(shares))
    logger.info("price: {}".format(price))
    logger.info("date: {}".format(date))
    print("")

    name, shares, price, (year, mon, day) = data
    logger.info("name: {}".format(name))
    logger.info("shares: {}".format(shares))
    logger.info("price: {}".format(price))
    logger.info("year: {}".format(year))
    logger.info("month: {}".format(mon))
    logger.info("day: {}".format(day))
    print("")

    s = "hello"
    a, b, c, d, e = s
    logger.info("a: {}".format(a))
    logger.info("b: {}".format(b))
    logger.info("c: {}".format(c))
    logger.info("d: {}".format(d))
    logger.info("e: {}".format(e))
    print("")

    _, shares2, price2, _ = data
    logger.info("shares2: {}".format(shares2))
    logger.info("price2: {}".format(price2))
    print("")


# unpacking elements from iterables of arbitrary length
def chapter1_2():
    logger.info("chapter1_2")
    logger.info("unpacking elements from iterables of arbitrary length")


def chapter1_3():
    logger.info("chapter1_3")
    logger.info("")


def chapter1_4():
    logger.info("chapter1_4")
    logger.info("")


def chapter1_5():
    logger.info("chapter1_5")
    logger.info("")


def chapter1_6():
    logger.info("chapter1_6")
    logger.info("")


def chapter1_7():
    logger.info("chapter1_7")
    logger.info("")


def chapter1_8():
    logger.info("chapter1_8")
    logger.info("")


def chapter1_9():
    logger.info("chapter1_9")
    logger.info("")


def chapter1_10():
    logger.info("chapter1_10")
    logger.info("")


def chapter1_11():
    logger.info("chapter1_11")
    logger.info("")


def chapter1_12():
    logger.info("chapter1_12")
    logger.info("")


def chapter1_13():
    logger.info("chapter1_13")
    logger.info("")


def chapter1_14():
    logger.info("chapter1_14")
    logger.info("")


def chapter1_15():
    logger.info("chapter1_15")
    logger.info("")


def chapter1_16():
    logger.info("chapter1_16")
    logger.info("")


def chapter1_17():
    logger.info("chapter1_17")
    logger.info("")


def chapter1_18():
    logger.info("chapter1_18")
    logger.info("")


def chapter1_19():
    logger.info("chapter1_19")
    logger.info("")


def chapter1_20():
    logger.info("chapter1_20")
    logger.info("")
