#!/usr/bin/env python3
"""Python Cookbook, 3rd Edition -- Chapter 5"""

import os

# import sys
from config import PROJECT_PATH
import logging
import pprint as pp

# from pathlib import Path

logger = logging.getLogger("COOKBOOK-CH5")

input_path = PROJECT_PATH / "input"
output_path = PROJECT_PATH / "output"


def cookbook_chapter5(args=None):
    logger.info("cookbook_chapter5")
    if args:
        pp.pprint(args)

    logger.info("project_path: {}".format(PROJECT_PATH))
    logger.info("input_path: {}".format(input_path))
    logger.info("output_path: {}".format(output_path))

    chapter5_1()
    chapter5_3()
    chapter5_4()
    chapter5_5()
    chapter5_9()
    chapter5_13()


def chapter5_1():

    infile = input_path / "somefile.txt"
    outfile = output_path / "someoutfile.txt"

    # Read the entire file as a single string
    with open(infile, "rt") as f:
        data = f.read()
        print(data)

    # Iterate over the lines of the file
    with open(infile, "rt", newline="") as f:
        for line in f:
            print("[boo]{}".format(line))

    # Write chunks of text data
    with open(outfile, "wt") as f:
        f.write(data)

    # Append chunks of text data
    with open(outfile, "at") as f:
        f.write(data)

    # Redirected print statement
    with open(outfile, "at") as f:
        print("print redirect 1", file=f)
        print("print redirect 2", file=f)

    # Read the entire file as a single string
    with open(infile, "rt", encoding="ascii", newline="") as f:
        data = f.read()
        print(data)


def chapter5_3():
    print("string here", 10, ["a", "b", "c"])
    print("string here", 10, ["a", "b", "c"], sep=":")
    print("string here", 10, ["a", "b", "c"], sep=":", end=" BOO!  \n")

    for i in range(5):
        print(i)

    for i in range(5):
        print(i, end=" ", flush=True)

    print()
    logger.info("end of chapter5_3")

    row_str = ("ACME", "50", "91.5")
    row_mixed = ("ACME", 50, 91.5)

    print(",".join(row_str))
    try:
        print(",".join(row_mixed))
    except TypeError:
        print("unable mix types")
    print(",".join(str(x) for x in row_mixed))

    print(*row_mixed, sep=",")


def chapter5_4():

    infile = input_path / "chapter5_4_in.bin"
    outfile = output_path / "chapter5_4_out.bin"

    infile2 = input_path / "chapter5_4_2_in.bin"
    outfile2 = output_path / "chapter5_4_2_out.bin"

    databin_1 = output_path / "databin_1_out.bin"

    # Write binary data to a file
    with open(outfile, "wb") as f:
        f.write(b"Hello World")

    # Read the entire file as a single byte string
    with open(infile, "rb") as f:
        data = f.read()
        print(data)

    with open(infile2, "rb") as f:
        data = f.read(16)
        text = data.decode("utf-8")
        print(text)

    with open(outfile2, "wb") as f:
        text = "Hello World"
        f.write(text.encode("utf-8"))

    import array

    nums = array.array("i", [1, 2, 3, 4])
    a = array.array("i", [0, 0, 0, 0, 0, 0, 0, 0])

    with open(databin_1, "wb") as f:
        f.write(nums)

    with open(databin_1, "rb") as f:
        data = f.readinto(a)
        print(data)
        print(a)


def chapter5_5():
    infile = input_path / "somefile.txt"

    if not os.path.exists(infile):
        print("file not exist... we should create one")
    else:
        print("File already exists... move along")


def chapter5_9():

    import os.path

    def read_into_buffer(filename):
        buf = bytearray(os.path.getsize(filename))
        with open(filename, "rb") as f:
            f.readinto(buf)
        return buf

    # write a sample file:
    databin_2 = output_path / "databin_2_out.bin"
    with open(databin_2, "wb") as f:
        f.write(b"Hello World Again")

    buf = read_into_buffer(databin_2)
    print(buf)


def chapter5_13():
    all_names = os.listdir(output_path)
    logger.info(sorted(all_names))

    file_names = [name for name in all_names if os.path.isfile(os.path.join(output_path, name))]
    logger.info(sorted(file_names))

    dir_names = [name for name in all_names if os.path.isdir(os.path.join(output_path, name))]
    logger.info(sorted(dir_names))

    pyfiles = [name for name in os.listdir(input_path) if name.endswith(".csv")]
    logger.info(sorted(pyfiles))

    # TODO: get this to work with pathlib
    # import glob
    # pyfiles2 = glob.glob(input_path / "*.csv")
    pyfiles2_tmp = sorted(input_path.glob("**/*.csv"))
    pyfiles2 = []
    for f in pyfiles2_tmp:
        #        logger.info(f.name)
        pyfiles2.append(f.name)
    #    logger.info(pyfiles2_tmp)
    logger.info(pyfiles2)

    from fnmatch import fnmatch

    pyfiles3 = [name for name in os.listdir(input_path) if fnmatch(name, "*.csv")]
    logger.info(sorted(pyfiles3))

    # Get file sizes and modification dates
    name_sz_date = [(name, os.path.getsize(input_path / name), os.path.getmtime(input_path / name)) for name in pyfiles]

    for name, size, mtime in name_sz_date:
        print(name, size, mtime)

    # Alternative: Get file metadata
    file_metadata = [(name, os.stat(input_path / name)) for name in pyfiles]

    for name, meta in file_metadata:
        print(name, meta.st_size, meta.st_mtime)
