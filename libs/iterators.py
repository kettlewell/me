#!/usr/bin/env python3
"""Iterators based routines"""

import logging

logger = logging.getLogger("ITERATORS")


def iterators(args=None):
    logger.debug("iterators")

    is_iterable()
    iterate_manually()
    generator_iterator()
    gennie_test()
    test_simple_gen()


def is_iterable():

    from collections.abc import Iterable

    logger.info("Is a list Iterable? %s", isinstance([1, 2, 3, 4, 5], Iterable))
    logger.info("Is a number Iterable? %s", isinstance(5, Iterable))

    print(dir([1, 2, 3, 4, 5]))
    print()
    print(dir(5))


def iterate_manually():
    mylst = [1, 2, 3, 4]
    it = iter(mylst)
    while True:
        try:
            print(next(it))
        except StopIteration:
            print("Stop Iteration")
            break


def generator_iterator():

    my_gennie = (x * x for x in range(10))
    for i in my_gennie:
        print(i)


def yield_test():
    print("first")
    yield 1
    print("second")
    yield 2
    print("third")
    yield 3


def gennie_test():
    my_gennie = yield_test()
    print(type(my_gennie))

    try:
        print(next(my_gennie))
        print(next(my_gennie))
        print(next(my_gennie))
        next(my_gennie)
    except StopIteration:
        print("no more iterations")

    # for x in my_gennie:
    #    print(x)


def simple_gen(a):
    print("-> Started: a = ", a)
    b = yield a
    print("-> Received: b = ", b)
    c = yield a + b
    print("-> Received: c = ", c)


def test_simple_gen():

    gen = simple_gen(14)
    try:
        next(gen)
        gen.send(15)
        gen.send(99)
    except StopIteration:
        print("all done with the generator")
