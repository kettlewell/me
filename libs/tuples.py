#!/usr/bin/env python3
"""Tuples based routines"""

import logging

logger = logging.getLogger("TUPLES")


def tuples(args=None):
    logger.info("tuples")

    if args:
        print(vars(args))
        logger.info(vars(args))

    data1 = [("red", 1), ("blue", 1), ("red", 2), ("blue", 2)]
    # pp.pprint(data1)
    # pp.pprint(sorted(data1))
    # pp.pprint(sorted(data1,key=itemgetter(1,0)))

    student_tuples = [("john", "A", 15), ("jane", "B", 12), ("dave", "B", 10)]

    # print(sorted(student_tuples, key=lambda student: student[1] ))
