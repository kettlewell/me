#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 6"""

import logging
from collections import namedtuple

import pprint as pp
import csv
import json
from re import S
from struct import unpack
from urllib.request import urlopen
import sqlite3
import binascii
import base64
import struct
import itertools

from config import PROJECT_PATH
from libs.decorators import log_calls

logger = logging.getLogger("COOKBOOK-CH6")


input_path = PROJECT_PATH / "input"
output_path = PROJECT_PATH / "output"


def cookbook_chapter6(args=None):
    logger.info("cookbook_chapter6")
    if args:
        pp.pprint(args)

    # chapter6_1()
    # chapter6_2()
    # chapter6_8()
    # chapter6_9()
    # chapter6_10()
    # chapter6_11()
    chapter6_12()


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


def chapter6_2():
    data = {"name": "ACME", "shares": 100, "price": 542.23}
    json_str = json.dumps(data)
    logger.info(json_str)

    data2 = json.loads(json_str)
    logger.info(data2)

    # note that this file appears to be a list at the top level
    with open(input_path / "census-record-1920.json") as f:
        data = json.load(f)

    # logger.info(type(data))
    # logger.info(data[0])

    d_in = {"a": True, "b": "Hello", "c": None}
    d_out = json.dumps(d_in)
    logger.info(d_out)

    # defunct URL from the book
    #    u = urlopen("http://search.twitter.com/search.json?q=python&rpp=5")

    # u = urlopen("https://api.github.com/gists")
    # resp = json.loads(u.read().decode("utf-8"))
    # pp.pprint(resp[0])

    s = '{"name": "ACME", "shares": 50, "price": 490.1}'
    from collections import OrderedDict

    data = json.loads(s, object_pairs_hook=OrderedDict)
    pp.pprint(data)

    class JSONObject:
        def __init__(self, d):
            self.__dict__ = d

    data = json.loads(s, object_hook=JSONObject)
    pp.pprint(data.name)

    # resp_obj = json.loads(resp[0], object_hook=JSONObject)
    # pp.pprint(resp_obj)

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    classes = {"Point": Point}

    def serialize(obj):
        d = {"__classname__": type(obj).__name__}
        d.update(vars(obj))
        return d

    def unserialize(d):
        clsname = d.pop("__classname__", None)
        if clsname:
            cls = classes[clsname]
            obj = cls.__new__(cls)
            for key, value in d.items():
                setattr(obj, key, value)
                return obj
        else:
            return d

    p = Point(2, 3)
    pp.pprint(p.x)
    pp.pprint(p.y)

    s = json.dumps(p, default=serialize)
    pp.pprint(s)

    a = json.loads(s, object_hook=unserialize)
    pp.pprint(a)
    pp.pprint(a.x)
    pp.pprint(a)
    pp.pprint(a.y)


#    pp.pprint(a.y)


def chapter6_8():
    logger.info("Interacting with Relational Database")
    stocks = [
        ("GOOG", 100, 490.1),
        ("AAPL", 50, 545.75),
        ("FB", 150, 7.45),
        ("HPQ", 75, 33.2),
    ]

    db = sqlite3.connect("database.db")
    c = db.cursor()
    c.execute("create table if not exists portfolio (symbol text, shares integer, price real)")

    db.commit()

    c.executemany("insert into portfolio values (?,?,?)", stocks)
    db.commit()

    for row in db.execute("select * from portfolio"):
        print(row)
    print()

    min_price = 100
    for row in db.execute("select * from portfolio where price >= ?", (min_price,)):
        print(row)


def chapter6_9():
    s = b"hello"

    h = binascii.b2a_hex(s)
    pp.pprint(h)

    a = binascii.a2b_hex(h)
    pp.pprint(a)

    h = base64.b16encode(s)
    pp.pprint(h)

    a = base64.b16decode(h)
    pp.pprint(a)


def chapter6_10():

    s = b"hello"

    a = base64.b64encode(s)
    pp.pprint(a)

    b = base64.b64encode(s).decode("ascii")
    pp.pprint(b)

    c = base64.b64decode(a)
    pp.pprint(c)

    d = base64.b64decode(b).decode("ascii")
    pp.pprint(d)


def chapter6_11():
    from struct import Struct

    def write_records(records, format, f):
        """
        Write a sequence of tuples to a binary file of structures.
        """
        record_struct = Struct(format)
        for r in records:
            f.write(record_struct.pack(*r))

    records = [(1, 2.3, 4.5), (6, 7.8, 9.0), (12, 13.4, 56.7)]

    with open(output_path / "data.b", "wb") as f:
        write_records(records, "<idd", f)

    def read_records(format, f):
        record_struct = Struct(format)
        chunks = iter(lambda: f.read(record_struct.size), b"")
        return (record_struct.unpack(chunk) for chunk in chunks)

    with open(output_path / "data.b", "rb") as f:
        for rec in read_records("<idd", f):
            pp.pprint(rec)

    def unpack_records(format, data):
        record_struct = Struct(format)
        return (record_struct.unpack_from(data, offset) for offset in range(0, len(data), record_struct.size))

    with open(output_path / "data.b", "rb") as f:
        data = f.read()

        for rec in unpack_records("<idd", data):
            pp.pprint(rec)


def chapter6_12():
    polys = [
        [(1.0, 2.5), (3.5, 4.0), (2.5, 1.5)],
        [(7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0)],
        [(3.4, 6.3), (1.2, 0.5), (4.6, 9.2)],
    ]

    def write_polys(filename, polys):
        # Determine bounding box
        flattened = list(itertools.chain(*polys))
        min_x = min(x for x, y in flattened)
        max_x = max(x for x, y in flattened)
        min_y = min(y for x, y in flattened)
        max_y = max(y for x, y in flattened)

        with open(output_path / filename, "wb") as f:
            f.write(struct.pack("<iddddi", 0x1234, min_x, min_y, max_x, max_y, len(polys)))

            for poly in polys:
                size = len(poly) * struct.calcsize("<dd")
                f.write(struct.pack("<i", size + 4))
                for pt in poly:
                    f.write(struct.pack("<dd", *pt))

    def read_polys(filename):
        with open(output_path / filename, "rb") as f:
            # Read the header
            header = f.read(40)
            file_code, min_x, min_y, max_x, max_y, num_polys = struct.unpack("<iddddi", header)
            polys = []
            for n in range(num_polys):
                (pbytes,) = struct.unpack("<i", f.read(4))
                poly = []
            for m in range(pbytes // 16):
                pt = struct.unpack("<dd", f.read(16))
                poly.append(pt)
            polys.append(poly)
        return polys

    write_polys("polys.bin", polys)
    out_poly = read_polys("polys.bin")
    pp.pprint(out_poly)
