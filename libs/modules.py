#!/usr/bin/env python3
"""Modules based routines"""

import logging
import me.libs.modules.modules_astral
import me.libs.modules.modules_opencv
import me.libs.modules.modules_inspect

logger = logging.getLogger("MODULES")


def modules(args=None):
    logger.info("modules")

    me.libs.modules.modules_astral.modules_astral(args)
    me.libs.modules.modules_opencv.modules_opencv(args)
    modules_requests(args)
    modules_datetime(args)
    modules_collections(args)
    modules_heapq(args)
    modules_bisect(args)
    modules_types(args)
    modules_array(args)
    modules_copy(args)
    modules_pprint(args)
    modules_math(args)
    modules_random(args)
    modules_statistics(args)
    modules_itertools(args)
    modules_functools(args)
    modules_operator(args)
    modules_pathlib(args)
    modules_os(args)
    modules_glob(args)
    modules_fnmatch(args)
    modules_shutil(args)
    modules_sqlite3(args)
    modules_csv(args)
    modules_json(args)
    modules_configparser(args)
    modules_io(args)
    modules_time(args)
    modules_errno(args)
    modules_curses(args)
    modules_ctypes(args)
    modules_threading(args)
    modules_multiprocessing(args)
    modules_concurrent(args)
    modules_subprocess(args)
    modules_sched(args)
    modules_queue(args)
    modules__thread(args)
    modules_asyncio(args)
    modules_socket(args)
    modules_ssl(args)
    modules_mmap(args)
    modules_signal(args)
    modules_urllib(args)
    modules_http(args)
    modules_socketserver(args)
    modules_ipaddress(args)
    modules_turtle(args)
    modules_cmd(args)
    modules_shlex(args)
    modules_tkinter(args)
    modules_typing(args)
    modules_pydoc(args)
    modules_pdb(args)
    modules_timeit(args)
    modules_sys(args)
    modules_sysconfig(args)
    modules_inspect(args)
    modules_importlib(args)


def modules_requests(args=None):
    logger.info("libs.modules.modules_requests")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_datetime(args=None):
    logger.info("modules_datetime")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_collections(args=None):
    logger.info("modules_collections")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_heapq(args=None):
    logger.info("modules_heapq")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_bisect(args=None):
    logger.info("modules_bisect")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_types(args=None):
    logger.info("modules_types")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_array(args=None):
    logger.info("modules_array")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_copy(args=None):
    logger.info("modules_copy")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_pprint(args=None):
    logger.info("modules_pprint")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_math(args=None):
    logger.debug("modules_math")

    import sys

    import math
    import cmath

    logger.info("sys.maxsize: %s", sys.maxsize)
    logger.info("log2(mathsize): %s", math.log(sys.maxsize, 2))
    logger.info("sys.int_info: %s", sys.int_info)

    logger.info("math.frexp(): %s", math.frexp(8.066e67))
    try:
        logger.info(math.sqrt(-2))
    except:
        logger.error("unable to compute sqrt of -2")
    logger.info(cmath.sqrt(-2))

    # using floor div and modulo to compute H:M:S from given seconds
    total_seconds = 7385
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    logger.info("hours:min:secs (%s:%s:%s)", hours, minutes, seconds)

    # alternate form, using divmod()
    hours, remaining_seconds = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remaining_seconds, 60)
    logger.info("hours:min:secs (%s:%s:%s)", hours, minutes, seconds)

    hours = total_seconds / 3600
    logger.info("hours: %s", hours)
    logger.info("hours(rounded 10): %s", round(hours, 10))
    logger.info("hours(rounded 5): %s", round(hours, 5))
    logger.info("hours(rounded 3): %s", round(hours, 3))


def modules_random(args=None):
    logger.info("modules_random")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_statistics(args=None):
    logger.info("modules_statistics")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_itertools(args=None):
    logger.info("modules_itertools")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_functools(args=None):
    logger.info("modules_functools")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_operator(args=None):
    logger.info("modules_operator")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_pathlib(args=None):
    logger.info("modules_pathlib")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_os(args=None):
    logger.info("modules_os")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_glob(args=None):
    logger.info("modules_glob")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_fnmatch(args=None):
    logger.info("modules_fnmatch")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_shutil(args=None):
    logger.info("modules_shutil")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_sqlite3(args=None):
    logger.info("modules_sqlite3")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_csv(args=None):
    logger.info("modules_csv")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_json(args=None):
    logger.info("modules_json")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_configparser(args=None):
    logger.info("modules_configparser")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_io(args=None):
    logger.info("modules_io")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_time(args=None):
    logger.debug("modules_time")

    import time

    def gen_timestamp():
        logger.info(time.time())

    def gen_datetime():
        logger.info(time.ctime())

    gen_timestamp()
    gen_datetime()


def modules_errno(args=None):
    logger.info("modules_errno")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_curses(args=None):
    logger.info("modules_curses")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_ctypes(args=None):
    logger.info("modules_ctypes")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_threading(args=None):
    logger.info("modules_threading")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_multiprocessing(args=None):
    logger.info("modules_multiprocessing")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_concurrent(args=None):
    logger.info("modules_concurrent")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_subprocess(args=None):
    logger.info("modules_subprocess")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_sched(args=None):
    logger.info("modules_sched")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_queue(args=None):
    logger.info("modules_queue")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules__thread(args=None):
    logger.info("modules__thread")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_asyncio(args=None):
    logger.info("modules_asyncio")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_socket(args=None):
    logger.info("modules_socket")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_ssl(args=None):
    logger.info("modules_ssl")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_mmap(args=None):
    logger.info("modules_mmap")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_signal(args=None):
    logger.info("modules_signal")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_urllib(args=None):
    logger.info("modules_urllib")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_http(args=None):
    logger.info("modules_http")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_socketserver(args=None):
    logger.info("modules_socketserver")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_ipaddress(args=None):
    logger.info("modules_ipaddress")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_turtle(args=None):
    logger.info("modules_turtle")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_cmd(args=None):
    logger.info("modules_cmd")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_shlex(args=None):
    logger.info("modules_shlex")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_tkinter(args=None):
    logger.info("modules_tkinter")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_typing(args=None):
    logger.info("modules_typing")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_pydoc(args=None):
    logger.info("modules_pydoc")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_pdb(args=None):
    logger.info("modules_pdb")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_timeit(args=None):
    logger.info("modules_timeit")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_sys(args=None):
    logger.debug("modules_sys")

    import sys

    logger.info(sys.builtin_module_names)

    a = "life is beautiful"
    b = "life is beautiful"
    logger.info("id(a): %s", id(a))
    logger.info("id(b): %s", id(b))

    a = sys.intern("life is beautiful")
    b = sys.intern("life is beautiful")

    logger.info("id(a): %s", id(a))
    logger.info("id(b): %s", id(b))


def modules_sysconfig(args=None):
    logger.info("modules_sysconfig")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_inspect(args=None):
    logger.info("modules_inspect")

    if args:
        print(vars(args))
        logger.info(vars(args))


def modules_importlib(args=None):
    logger.info("modules_importlib")

    if args:
        print(vars(args))
        logger.info(vars(args))
