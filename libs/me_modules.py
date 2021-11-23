#!/usr/bin/env python3
'''Modules based routines'''

import logging
import libs.modules.me_modules_astral
import libs.modules.me_modules_opencv
import libs.modules.me_modules_inspect

logger = logging.getLogger('MODULES')

def me_modules(args=None):
    logger.info("me_modules")

    libs.modules.me_modules_astral.me_modules_astral(args)
    libs.modules.me_modules_opencv.me_modules_opencv(args)
    me_modules_requests(args)
    me_modules_datetime(args)                                                                                                                                                                                       
    me_modules_collections(args)                                                                                                                                                                                    
    me_modules_heapq(args)                                                                                                                                                                                          
    me_modules_bisect(args)                                                                                                                                                                                         
    me_modules_types(args)                                                                                                                                                                                          
    me_modules_array(args)                                                                                                                                                                                          
    me_modules_copy(args)                                                                                                                                                                                           
    me_modules_pprint(args)                                                                                                                                                                                         
    me_modules_math(args)                                                                                                                                                                                           
    me_modules_random(args)                                                                                                                                                                                         
    me_modules_statistics(args)                                                                                                                                                                                     
    me_modules_itertools(args)                                                                                                                                                                                      
    me_modules_functools(args)                                                                                                                                                                                      
    me_modules_operator(args)                                                                                                                                                                                       
    me_modules_pathlib(args)                                                                                                                                                                                        
    me_modules_os(args)                                                                                                                                                                                             
    me_modules_glob(args)                                                                                                                                                                                           
    me_modules_fnmatch(args)                                                                                                                                                                                        
    me_modules_shutil(args)
    me_modules_sqlite3(args)
    me_modules_csv(args)
    me_modules_json(args)
    me_modules_configparser(args)
    me_modules_io(args)
    me_modules_time(args)
    me_modules_errno(args)
    me_modules_curses(args)
    me_modules_ctypes(args)
    me_modules_threading(args)
    me_modules_multiprocessing(args)
    me_modules_concurrent(args)
    me_modules_subprocess(args)
    me_modules_sched(args)
    me_modules_queue(args)
    me_modules__thread(args)
    me_modules_asyncio(args)
    me_modules_socket(args)
    me_modules_ssl(args)
    me_modules_mmap(args)
    me_modules_signal(args)
    me_modules_urllib(args)
    me_modules_http(args)
    me_modules_socketserver(args)
    me_modules_ipaddress(args)
    me_modules_turtle(args)
    me_modules_cmd(args)
    me_modules_shlex(args)
    me_modules_tkinter(args)
    me_modules_typing(args)
    me_modules_pydoc(args)
    me_modules_pdb(args)
    me_modules_timeit(args)
    me_modules_sys(args)
    me_modules_sysconfig(args)
    me_modules_inspect(args)
    me_modules_importlib(args)





def me_modules_requests(args=None):
    logger.info("libs.me_modules.me_modules_requests")

    if args:
        print(vars(args))
        logger.info(vars(args))



def me_modules_datetime(args=None):
    logger.info("me_modules_datetime")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_collections(args=None):
    logger.info("me_modules_collections")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_heapq(args=None):
    logger.info("me_modules_heapq")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_bisect(args=None):
    logger.info("me_modules_bisect")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_types(args=None):
    logger.info("me_modules_types")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_array(args=None):
    logger.info("me_modules_array")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_copy(args=None):
    logger.info("me_modules_copy")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_pprint(args=None):
    logger.info("me_modules_pprint")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_math(args=None):
    logger.debug("me_modules_math")

    import sys

    import math
    import cmath
    
    logger.info("sys.maxsize: %s", sys.maxsize)
    logger.info("log2(mathsize): %s", math.log(sys.maxsize, 2))
    logger.info("sys.int_info: %s", sys.int_info)
    
    logger.info("math.frexp(): %s", math.frexp(8.066E+67))
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
    hours,remaining_seconds = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remaining_seconds,60)
    logger.info("hours:min:secs (%s:%s:%s)", hours, minutes, seconds)

    hours = total_seconds / 3600
    logger.info("hours: %s", hours)
    logger.info("hours(rounded 10): %s", round(hours,10))
    logger.info("hours(rounded 5): %s", round(hours,5))
    logger.info("hours(rounded 3): %s", round(hours,3))


def me_modules_random(args=None):
    logger.info("me_modules_random")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_statistics(args=None):
    logger.info("me_modules_statistics")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_itertools(args=None):
    logger.info("me_modules_itertools")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_functools(args=None):
    logger.info("me_modules_functools")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_operator(args=None):
    logger.info("me_modules_operator")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_pathlib(args=None):
    logger.info("me_modules_pathlib")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_os(args=None):
    logger.info("me_modules_os")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_glob(args=None):
    logger.info("me_modules_glob")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_fnmatch(args=None):
    logger.info("me_modules_fnmatch")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_shutil(args=None):
    logger.info("me_modules_shutil")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_sqlite3(args=None):
    logger.info("me_modules_sqlite3")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_csv(args=None):
    logger.info("me_modules_csv")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_json(args=None):
    logger.info("me_modules_json")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_configparser(args=None):
    logger.info("me_modules_configparser")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_io(args=None):
    logger.info("me_modules_io")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_time(args=None):
    logger.debug("me_modules_time")
    
    import time

    def gen_timestamp():
        logger.info(time.time())

    def gen_datetime():
        logger.info(time.ctime())

    gen_timestamp()
    gen_datetime()


def me_modules_errno(args=None):
    logger.info("me_modules_errno")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_curses(args=None):
    logger.info("me_modules_curses")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_ctypes(args=None):
    logger.info("me_modules_ctypes")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_threading(args=None):
    logger.info("me_modules_threading")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_multiprocessing(args=None):
    logger.info("me_modules_multiprocessing")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_concurrent(args=None):
    logger.info("me_modules_concurrent")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_subprocess(args=None):
    logger.info("me_modules_subprocess")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_sched(args=None):
    logger.info("me_modules_sched")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_queue(args=None):
    logger.info("me_modules_queue")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules__thread(args=None):
    logger.info("me_modules__thread")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_asyncio(args=None):
    logger.info("me_modules_asyncio")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_socket(args=None):
    logger.info("me_modules_socket")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_ssl(args=None):
    logger.info("me_modules_ssl")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_mmap(args=None):
    logger.info("me_modules_mmap")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_signal(args=None):
    logger.info("me_modules_signal")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_urllib(args=None):
    logger.info("me_modules_urllib")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_http(args=None):
    logger.info("me_modules_http")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_socketserver(args=None):
    logger.info("me_modules_socketserver")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_ipaddress(args=None):
    logger.info("me_modules_ipaddress")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_turtle(args=None):
    logger.info("me_modules_turtle")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_cmd(args=None):
    logger.info("me_modules_cmd")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_shlex(args=None):
    logger.info("me_modules_shlex")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_tkinter(args=None):
    logger.info("me_modules_tkinter")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_typing(args=None):
    logger.info("me_modules_typing")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_pydoc(args=None):
    logger.info("me_modules_pydoc")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_pdb(args=None):
    logger.info("me_modules_pdb")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_timeit(args=None):
    logger.info("me_modules_timeit")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_sys(args=None):
    logger.debug("me_modules_sys")

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
    

    

def me_modules_sysconfig(args=None):
    logger.info("me_modules_sysconfig")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_inspect(args=None):
    logger.info("me_modules_inspect")

    if args:
        print(vars(args))
        logger.info(vars(args))

def me_modules_importlib(args=None):
    logger.info("me_modules_importlib")

    if args:
        print(vars(args))
        logger.info(vars(args))
