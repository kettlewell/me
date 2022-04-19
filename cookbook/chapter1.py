#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 1
Author's Partial Code Implemenation:
https://github.com/dabeaz/python-cookbook/tree/master/src/1
"""


import logging
import pprint as pp

logger = logging.getLogger("COOKBOOK-CH1")


def cookbook_chapter1(args=None):
    logger.info("cookbook_chapter1")

    if args:
        pp.pprint(args)

    chapter1_1()
    chapter1_2()

    chapter1_3()
    chapter1_4()
    chapter1_5()
    chapter1_6()
    chapter1_7()
    chapter1_8()
    chapter1_9()
    chapter1_10()
    chapter1_11()
    chapter1_12()
    chapter1_13()
    chapter1_14()
    chapter1_15()
    chapter1_16()
    chapter1_17()
    chapter1_18()
    chapter1_19()
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

    print()

    def drop_first_last(grades):
        first, *middle, last = grades
        # return avg(middle) # unknown name 'avg'
        return middle

    gradelist = [4, 3, 4, 2, 3, 4, 2]
    gradeavg = drop_first_last(gradelist)
    logger.info("gradeavg: {}".format(gradeavg))

    print()

    user_record = ("Dave", "dave@example.com", "773-555-1212", "847-555-1212")
    name, email, *phone_numbers = user_record
    logger.info("name: {}".format(name))
    logger.info("email: {}".format(email))
    logger.info("phone numbers: {}".format(phone_numbers))

    print()
    user_record2 = ("Dave", "dave@example.com", "773-555-1212")
    name2, email2, *phone_numbers2 = user_record2
    logger.info("phone numbers: {}".format(phone_numbers2))
    print()
    user_record3 = ("Dave", "dave@example.com")
    name3, email3, *phone_numbers3 = user_record3
    logger.info("phone numbers: {}".format(phone_numbers3))
    print()

    *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
    logger.info("trailing: {}".format(trailing))
    logger.info("current: {}".format(current))
    print()

    records = [
        ("foo", 1, 2),
        ("bar", "hello"),
        ("foo", 3, 4),
    ]

    def do_foo(x, y):
        logger.info("do_foo: {} and {}".format(x, y))

    def do_bar(s):
        logger.info("do_bar: {}".format(s))

    for tag, *args in records:
        if tag == "foo":
            do_foo(*args)
        elif tag == "bar":
            do_bar(*args)

    print()

    line = "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false"
    uname, *fields, homedir, sh = line.split(":")
    logger.info("uname: {}".format(uname))
    logger.info("homedir: {}".format(homedir))
    logger.info("sh: {}".format(sh))

    print()

    record = ("ACME", 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record

    logger.info("name: {}".format(name))
    logger.info("year: {}".format(year))

    print()

    items = [1, 10, 7, 4, 5, 9]
    head, *tail = items

    logger.info("head: {}".format(head))
    logger.info("tail: {}".format(tail))

    def sum(items):
        head, *tail = items
        return head + sum(tail) if tail else head

    sum_items = sum(items)
    logger.info("sum_items: {}".format(sum_items))

    print()


def chapter1_3():
    return
    logger.info("chapter1_3")
    logger.info("Keeping the Last N Items")
    print()


def chapter1_4():
    return
    logger.info("chapter1_4")
    logger.info("")


def chapter1_5():
    return
    logger.info("chapter1_5")
    logger.info("")


def chapter1_6():
    return
    logger.info("chapter1_6")
    logger.info("")


def chapter1_7():
    return
    logger.info("chapter1_7")
    logger.info("")


def chapter1_8():
    return
    logger.info("chapter1_8")
    logger.info("")


def chapter1_9():
    return
    logger.info("chapter1_9")
    logger.info("")


def chapter1_10():
    return
    logger.info("chapter1_10")
    logger.info("")


def chapter1_11():
    return
    logger.info("chapter1_11")
    logger.info("")


def chapter1_12():
    return
    logger.info("chapter1_12")
    logger.info("")


def chapter1_13():
    return
    logger.info("chapter1_13")
    logger.info("")


def chapter1_14():
    return
    logger.info("chapter1_14")
    logger.info("")


def chapter1_15():
    return
    logger.info("chapter1_15")
    logger.info("")


def chapter1_16():
    return
    logger.info("chapter1_16")
    logger.info("")


def chapter1_17():
    return
    logger.info("chapter1_17")
    logger.info("")


def chapter1_18():
    return
    logger.info("chapter1_18")
    logger.info("")


def chapter1_19():
    return
    logger.info("chapter1_19")
    logger.info("")


def chapter1_20():
    return
    logger.info("chapter1_20")
    logger.info("")
