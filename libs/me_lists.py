#!/usr/bin/env python3
"""Lists based routines"""

import logging

from libs.me_utilities import log_values as lv
from libs.me_utilities import cmp_values as cv

logger = logging.getLogger("LISTS")


def me_lists(args=None):
    logger.debug("me_lists")

    int_list = [1000, 7, 8, 9, -56, 4, 6, 3, -99]
    str_int_list = ["1000", "9", "9", "7", "8", "9", "-56", "4", "3", "6", "3", "7", "-99"]

    l1 = [1, 2, 3, 4]
    l2 = ["batman"]
    merge_lists(l1, l2)

    freq_list = [9, 9, 9, 9, 9, 5, 4, 3, 2, 56, 3, 2, 4]
    most_frequent_elem(freq_list)

    nested_list()

    dupe_list = [9, 9, 7, 8, 9, 56, 4, 3, 6, 3, 7]
    de_dupe_list(dupe_list)

    asc_sort_list(int_list)
    desc_sort_list(int_list)

    map_str_int_list(str_int_list)

    rotate_list(int_list, n=1)
    rotate_list(int_list, n=2)
    rotate_list(int_list, n=-1)
    rotate_list(int_list, n=-2)

    mat_list = [[1, 2, 3], [3, 4, 6], [5, 6, 7], [8, 9, 10]]
    matrix_transform(mat_list)

    list_subset_selection()

    unpack_list(int_list)

    operator_star_copy()

    my_list = append_to(12)
    logger.info("my_list: %s", my_list)
    my_other_list = append_to(42)
    logger.info("my_other_list: %s", my_other_list)

    are_they_same()


def are_they_same():

    a = "blah"
    b = "blah"
    logger.info("id(a): %s", id(a))
    logger.info("id(b): %s", id(b))

    if a is b:
        logger.info("A is B")
    else:
        logger.info("A NOT B")

    a = "left"
    b = "right"

    logger.info("id(a): %s", hex(id(a)))
    logger.info("id(b): %s", hex(id(b)))

    if a is b:
        logger.info("A is B")
    else:
        logger.info("A NOT B")


# https://ep2020.europython.eu/media/conference/slides/DLWTgr3-object-internals.pdf
def append_to(elem, to=None):
    if not to:
        to = []

    logger.info("id(to): %s", id(to))
    to.append(elem)
    return to


def operator_star_copy():

    L = [[0] * 3] * 3
    logger.info(L)
    logger.info("id(L): %s", id(L))
    L[0][0] = 1

    logger.info(id(L))

    logger.info(id(L[0]))
    logger.info(id(L[1]))

    logger.info(id(L[0][0]))
    logger.info(id(L[1][0]))


def unpack_list(lst):
    first, *middle, last = lst
    logger.info(lst)
    logger.info(first)
    logger.info(middle)
    logger.info(last)


def list_subset_selection():
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    pos_list = [n for n in mylist if n > 0]
    logger.info(pos_list)
    neg_list = [n for n in mylist if n < 0]
    logger.info(neg_list)


def matrix_transform(mat):
    res1 = list(list(x) for x in zip(*mat))  # noqa: C400
    res2 = [list(x) for x in zip(*mat)]
    res3 = [x for x in zip(*mat)]  # noqa C416

    logger.info("input matrix: %s", mat)
    logger.info(zip(*mat))
    logger.info("transformed matrix: %s", res1)
    logger.info("transformed matrix: %s", res2)
    logger.info("transformed matrix: %s", res3)


def rotate_list(li, n=1):

    rotate = "right"
    if n < 0:
        rotate = "left"

    res1 = li[n:] + li[:n]

    logger.info("list: %s  rotation: %s  N: %s", li, rotate, n)
    logger.info("res1 %s", res1)


def map_str_int_list(lst):
    res = list(map(int, lst))
    logger.info("mapping str to int:  %s", res)


def asc_sort_list(lst):
    res = sorted(lst)
    logger.info("asc sorted list: %s", res)


def desc_sort_list(lst):
    res = sorted(lst, reverse=True)
    logger.info("asc sorted list: %s", res)


def de_dupe_list(lst):
    res = list(set(lst))
    logger.info("de-duped list:  %s", res)


def nested_list():
    nums = [[num] for num in range(0, 9)]
    logger.info(nums)


def most_frequent_elem(lst):
    most_frequent = max(set(lst), key=lst.count)
    logger.info(most_frequent)


# in-place list merge of l2 into l1
def merge_lists(l1, l2):
    logger.info(l1)
    l1.extend(l2)
    logger.info(l1)
    logger.info(l2)


def from_practice(args):
    # initialize lists
    squares = [1, 4, 9, 16, 25]

    # list indexing
    logger.info(squares[0])
    lv(1, squares[0])
    logger.info(cv(1, squares[0]))

    # list slicing

    # unpacking lists
    first, *rest = [1, 2, 3, 4, 5, 6]
    logger.info("first: {}  rest: {}({})".format(first, rest, type(rest)))

    first, *l, last = [1, 2, 3, 4, 5, 6]
    logger.info("first: {}  l: {} ({})  last: {} ({})".format(first, l, type(l), last, type(last)))

    # Sorting
    somelist = [1, 10, 99, 98, 101, -10, 11]
    logger.info(somelist)
    somelist.sort()
    logger.info(sorted(somelist))

    logger.info(somelist)

    # list comprehension
    # squares1 = [x ** 2 for x in range(0, 10)]
    # pp.pprint(squares1)

    # rval = [x for x in range(4)]  # noqa: C416
    # pp.pprint(rval)

    # List Zipping
    # questions = ["name", "quest", "favorite color"]
    # answers = ["lancelot", "the holy grail", "blue"]
    # for q, a in zip(questions, answers):
    #    print('What is your {0}?  It is {1}.'.format(q, a))
