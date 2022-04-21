#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 6"""

import logging
from collections import namedtuple

import pprint as pp
import csv
import json


from config import PROJECT_PATH
from libs.decorators import log_calls

logger = logging.getLogger("COOKBOOK-CH6")


input_path = PROJECT_PATH / "input"
output_path = PROJECT_PATH / "output"


def cookbook_chapter6(args=None):
    logger.info("cookbook_chapter6")
    if args:
        pp.pprint(args)

    chapter6_1()


@log_calls(logger, "STACK_TRACE:")
def chapter6_1():
    logger.info("Reading and Writing CSV Data")

    # with open(input_path / "iris.csv") as f:
    #     f_csv = csv.reader(f)
    #     headers = next(f_csv)
    #     # print(headers)
    #     for row in f_csv:
    #         # print(row)
    #         pass

    col_types = [float, float, float, float, str]

    with open(input_path / "iris.csv", newline="") as f:
        f_csv = csv.reader(f)
        Row = namedtuple("Row", next(f_csv))
        for r in f_csv:
            row = Row(*r)

            # Process row
            print(row.sepallength)
            row = tuple(convert(value) for convert, value in zip(col_types, row))
            print(row)
            print(row[0])

    with open(input_path / "iris.csv", newline="") as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:

            # TODO: get this to work with dict
            # print(type(row), "    ", row)
            # row = tuple(convert(value) for convert, value in zip(col_types, row))
            # print(type(row), "    ", row)
            # print("    ", row)
            # print("    ", row["sepallength"])
            pass
