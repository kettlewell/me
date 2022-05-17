"""Argument parsing with sub parsers

The general idea will be to create sub parsers for testing various things

main [options] [list|dict|generator|collection] [sub-commands]

original outline consideration: https://docs.python.org/3/library/index.html


Completed (relative term meaning, I'm probably not going to do much more with it):

NOTE to self: This needs to be cleaned up to be made clear.... my intention was one thing
which is not currently being implemented... this should be revised to reflect


Stubbed in:
* lists
* dicts
* re
* scope
* functions
* truthy
* iteratorsa
* lambdas
* generators
* tuples
* strings
* sets
* exceptions
* filedir
* unix
* networking_IPC
* threading
* multiprocessing
* async
* coroutine
* numerics
* comparisons
* compression
* internet


* modules:
  * requests
  * datetime
  * collections
  * heapq
  * bisect
  * types
  * array
  * copy
  * pprint
  * math
  * random
  * statistics
  * itertools
  * functools
  * operator
  * pathlib
  * os
  * glob
  * fnmatch
  * shutil
  * sqlite3
  * csv
  * json
  * configparser
  * io
  * time
  * errno
  * curses
  * ctypes
  * threading
  * multiprocessing
  * subprocess
  * sched
  * queue
  * _thread
  * asyncio
  * socket
  * ssl
  * mmap
  * signal
  * urllib
  * http
  * socketserver
  * ipaddress
  * turtle
  * cmd
  * shlex
  * tkinter
  * typing
  * pydoc
  * pdb
  * timeit
  * sys
  * sysconfig
  * inspect
  * importlib


TODO: # noqa: T101 T000

I put all the calling code into the libs directory...
I think that is incorrect, and should be split out differently


"""
import argparse  # noqa: E402

# import libs
# import libsmodules
# import me.libs.lists

# import scratchpad.practice

# print("scratchpad.practice.__dict__  :")
# print(scratchpad.practice.__dict__)
# print(' ')


def parse():  # noqa: WPS210 WPS213 WPS231 C901 CCR001 CFQ001
    parser = argparse.ArgumentParser(
        description="Demo program that highlights a lot of functionality of the python programming language."
    )

    # general / global arguments
    parser.add_argument(
        "--practice",
        "-p",
        help="practice runs",
        action="store_true",
    )  # example calling a module from arguments
    parser.add_argument(
        "--verbose",
        "-v",
        help="verbose levels",
        action="count",
        default=0,
    )
    parser.add_argument(
        "--log",
        "-l",
        help="log level",
        choices=[
            "debug",
            "info",
            "warning",
            "error",
            "critical",
        ],
        default="info",
    )

    # create first level sub-parser
    subparsers = parser.add_subparsers(
        help="Available Subcommands",
        description="Sub commands for executing specific code blocks",
        dest="sub_parser_name",
    )
    ### Concurrency

    # concurrency .... concurrency based code
    concurrency_parser = subparsers.add_parser("concurrency", help="concurrency commands")

    ### LISTS

    # lists ... lists based code
    lists_parser = subparsers.add_parser("lists", help="lists commands")

    ### DICTS

    # dicts ... dict based code
    dicts_parser = subparsers.add_parser("dicts", help="dicts commands")

    ### DECORATORS

    # decorators ... decorators based code
    decorators_parser = subparsers.add_parser("decorators", help="decorator commands")

    ### RE
    # MOVED TO MODULES
    # re ... regular expressions based code
    # re_parser = subparsers.add_parser("re", help="regex commands")

    # import me.libs.scope
    scope_parser = subparsers.add_parser("scope", help="Scope  commands")

    # import me.libs.functions
    functions_parser = subparsers.add_parser("functions", help="Function (builtin) commands")

    # import me.libs.truthy
    truthy_parser = subparsers.add_parser("truthy", help="Truthy commands")

    # import me.libs.iterators
    iterators_parser = subparsers.add_parser("iterators", help="Iterators commands")

    # import me.libs.lambdas
    lambdas_parser = subparsers.add_parser("lambdas", help="Lambdas commands")

    # import me.libs.generators
    generators_parser = subparsers.add_parser("generators", help="generators commands")

    # import me.libs.tuples
    tuples_parser = subparsers.add_parser("tuples", help="tuples commands")

    # import me.libs.strings
    strings_parser = subparsers.add_parser("strings", help="Strings commands")

    # import me.libs.sets
    sets_parser = subparsers.add_parser("sets", help="sets commands")

    # import me.libs.exceptions
    exceptions_parser = subparsers.add_parser("exceptions", help="Exceptions commands")

    # import me.libs.filedir
    filedir_parser = subparsers.add_parser("filedir", help="File and Directory commands")

    # import me.libs.unix
    unix_parser = subparsers.add_parser("unix", help="Unix commands")

    # import me.libs.networking_IPC
    networking_parser = subparsers.add_parser("networking", help="Networking and IPC commands")

    # import me.libs.threading
    threading_parser = subparsers.add_parser("threading", help="Threading commands")

    # import me.libs.multiprocessing
    multiprocessing_parser = subparsers.add_parser("multiprocessing", help="Multiprocessing commands")

    # import me.libs.async
    async_parser = subparsers.add_parser("async", help="async commands")

    # import me.libs.coroutine
    coroutine_parser = subparsers.add_parser("coroutine", help="coroutine commands")

    # import me.libs.numerics
    numerics_parser = subparsers.add_parser("numerics", help="numerics commands")

    # import me.libs.comparisons
    comparisons_parser = subparsers.add_parser("comparisons", help="comparison commands")

    # import me.libs.compression
    compression_parser = subparsers.add_parser("compression", help="Compression commands")

    # import me.libs.internet
    internet_parser = subparsers.add_parser("internet", help="Internet commands")

    ### PLAY

    # play... playground area to test new ideas quickly and without judgement...
    play_parser = subparsers.add_parser("play", help="Play sub-command help")

    # Create sub-sub parser for play sub-commands
    play_subparser = play_parser.add_subparsers(help="Play sub-sub-command help", dest="play_parser")
    play_subparser_practice = play_subparser.add_parser("practice", help="Play Practice sub-command help")
    play_subparser_weather = play_subparser.add_parser("weather", help="Play weather sub-command help")

    ### Python Cookbook, 3rd ed

    # cookbook
    cookbook_parser = subparsers.add_parser("cookbook", help="Play sub-command help")

    # Create sub-sub parser for cookbook sub-commands
    cookbook_subparser = cookbook_parser.add_subparsers(help="Cookbook sub-sub-command help", dest="cookbook_parser")
    cookbook_subparser_chapter1 = cookbook_subparser.add_parser("chapter1", help="Cookbook Chapter1 sub-command help")
    cookbook_subparser_chapter2 = cookbook_subparser.add_parser("chapter2", help="Cookbook Chapter2 sub-command help")
    cookbook_subparser_chapter3 = cookbook_subparser.add_parser("chapter3", help="Cookbook Chapter3 sub-command help")
    cookbook_subparser_chapter4 = cookbook_subparser.add_parser("chapter4", help="Cookbook Chapter4 sub-command help")
    cookbook_subparser_chapter5 = cookbook_subparser.add_parser("chapter5", help="Cookbook Chapter5 sub-command help")
    cookbook_subparser_chapter6 = cookbook_subparser.add_parser("chapter6", help="Cookbook Chapter6 sub-command help")
    cookbook_subparser_chapter7 = cookbook_subparser.add_parser("chapter7", help="Cookbook Chapter7 sub-command help")
    cookbook_subparser_chapter8 = cookbook_subparser.add_parser("chapter8", help="Cookbook Chapter8 sub-command help")
    cookbook_subparser_chapter9 = cookbook_subparser.add_parser("chapter9", help="Cookbook Chapter9 sub-command help")
    cookbook_subparser_chapter10 = cookbook_subparser.add_parser(
        "chapter10", help="Cookbook Chapter10 sub-command help"
    )
    cookbook_subparser_chapter11 = cookbook_subparser.add_parser(
        "chapter11", help="Cookbook Chapter11 sub-command help"
    )
    cookbook_subparser_chapter12 = cookbook_subparser.add_parser(
        "chapter12", help="Cookbook Chapter12 sub-command help"
    )
    cookbook_subparser_chapter13 = cookbook_subparser.add_parser(
        "chapter13", help="Cookbook Chapter13 sub-command help"
    )
    cookbook_subparser_chapter14 = cookbook_subparser.add_parser(
        "chapter14", help="Cookbook Chapter14 sub-command help"
    )
    cookbook_subparser_chapter15 = cookbook_subparser.add_parser(
        "chapter15", help="Cookbook Chapter15 sub-command help"
    )

    """ These are unused currently, but are an example of how a sub-sub parser would work     # noqa: WPS428 B018
    #
    # # play practice sub-sub commands testing
    # play_subsubparser_practice = play_subparser_practice.add_subparsers(
    #     help="Play sub-sub-command help", dest="play_subparser_practice"
    # )
    # play_subparser_practice_good = play_subsubparser_practice.add_parser(
    #     "good", help="Play Practice good sub-command help"
    # )
    # play_subparser_practice_bad = play_subsubparser_practice.add_parser(
    #     "bad", help="Play Practice bad sub-command help"
    # )
    """
    ### MODULES

    # modules ... code that is based on certain modules ( ie, requests)
    modules_parser = subparsers.add_parser("modules", help="Modules commands")

    # Create sub-sub parser for module sub-commands
    modules_subparser = modules_parser.add_subparsers(help="Modules sub commands", dest="modules_parser")

    # astral module sub-command
    astral_parser = subparsers.add_parser("astral", help="astral module Command")

    # opencv module sub-command
    opencv_parser = subparsers.add_parser("opencv", help="Modules opencv Sub Command")

    # ds ( data science ) module sub-command
    ds_parser = subparsers.add_parser("ds", help="Modules Data Science Sub Command")

    # request module sub-command
    modules_subparser_requests = modules_subparser.add_parser("requests", help="Modules Requests Sub Command")

    #  datetime module sub-command
    modules_subparser_datetime = modules_subparser.add_parser("datetime", help="Modules datetime Sub Command")

    # collections module sub-command
    modules_subparser_collections = modules_subparser.add_parser(
        "collections",
        help="Modules collections Sub Command",
    )

    # heapq  module sub-command
    modules_subparser_heapq = modules_subparser.add_parser("heapq", help="Modules heapq Sub Command")

    # bisect  module sub-command
    modules_subparser_bisect = modules_subparser.add_parser("bisect", help="Modules bisect Sub Command")

    # types  module sub-command
    modules_subparser_types = modules_subparser.add_parser("types", help="Modules types Sub Command")

    # array  module sub-command
    modules_subparser_array = modules_subparser.add_parser("array", help="Modules array Sub Command")

    # copy  module sub-command
    modules_subparser_copy = modules_subparser.add_parser("copy", help="Modules copy Sub Command")

    # pprint  module sub-command
    modules_subparser_pprint = modules_subparser.add_parser("pprint", help="Modules pprint Sub Command")

    # math  module sub-command
    modules_subparser_math = modules_subparser.add_parser("math", help="Modules math Sub Command")

    # random  module sub-command
    modules_subparser_random = modules_subparser.add_parser("random", help="Modules random Sub Command")

    # statistics  module sub-command
    modules_subparser_statistics = modules_subparser.add_parser(
        "statistics",
        help="Modules statistics Sub Command",
    )

    # itertools  module sub-command
    modules_subparser_itertools = modules_subparser.add_parser(
        "itertools",
        help="Modules itertools Sub Command",
    )

    # functools  module sub-command
    modules_subparser_functools = modules_subparser.add_parser(
        "functools",
        help="Modules functools Sub Command",
    )

    # operator  module sub-command
    modules_subparser_operator = modules_subparser.add_parser("operator", help="Modules operator Sub Command")

    # pathlib  module sub-command
    modules_subparser_pathlib = modules_subparser.add_parser("pathlib", help="Modules pathlib Sub Command")

    # os  module sub-command
    modules_subparser_os = modules_subparser.add_parser("os", help="Modules os Sub Command")

    #  glob module sub-command
    modules_subparser_glob = modules_subparser.add_parser("glob", help="Modules glob Sub Command")

    # fnmatch  module sub-command
    modules_subparser_fnmatch = modules_subparser.add_parser("fnmatch", help="Modules fnmatch Sub Command")

    # shutil  module sub-command
    modules_subparser_shutil = modules_subparser.add_parser("shutil", help="Modules shutil Sub Command")

    # sqlite3  module sub-command
    modules_subparser_sqlite3 = modules_subparser.add_parser("sqlite3", help="Modules sqlite3 Sub Command")

    # csv  module sub-command
    modules_subparser_csv = modules_subparser.add_parser("csv", help="Modules csv Sub Command")

    # json  module sub-command
    modules_subparser_json = modules_subparser.add_parser("json", help="Modules json Sub Command")

    # configparser  module sub-command
    modules_subparser_configparser = modules_subparser.add_parser(
        "configparser",
        help="Modules configparser Sub Command",
    )

    # io  module sub-command
    modules_subparser_io = modules_subparser.add_parser("io", help="Modules io Sub Command")

    # time  module sub-command
    modules_subparser_time = modules_subparser.add_parser("time", help="Modules time Sub Command")

    # errno  module sub-command
    modules_subparser_errno = modules_subparser.add_parser("errno", help="Modules errno Sub Command")

    # curses  module sub-command
    modules_subparser_curses = modules_subparser.add_parser("curses", help="Modules curses Sub Command")

    # ctypes  module sub-command
    modules_subparser_ctypes = modules_subparser.add_parser("ctypes", help="Modules ctypes Sub Command")

    # threading  module sub-command
    modules_subparser_threading = modules_subparser.add_parser(
        "threading",
        help="Modules threading Sub Command",
    )

    # multiprocessing  module sub-command
    modules_subparser_multiprocessing = modules_subparser.add_parser(
        "multiprocessing",
        help="Modules multiprocessing Sub Command",
    )

    # subprocess  module sub-command
    modules_subparser_subprocess = modules_subparser.add_parser(
        "subprocess",
        help="Modules subprocess Sub Command",
    )

    # sched  module sub-command
    modules_subparser_sched = modules_subparser.add_parser("sched", help="Modules sched Sub Command")

    # queue  module sub-command
    modules_subparser_queue = modules_subparser.add_parser("queue", help="Modules queue Sub Command")

    # _thread  module sub-command
    modules_subparser__thread = modules_subparser.add_parser(  # noqa: WPS116
        "_thread", help="Modules _thread Sub Command"
    )

    # asyncio  module sub-command
    modules_subparser_asyncio = modules_subparser.add_parser("asyncio", help="Modules asyncio Sub Command")

    # socket  module sub-command
    modules_subparser_socket = modules_subparser.add_parser("socket", help="Modules socket Sub Command")

    # ssl  module sub-command
    modules_subparser_ssl = modules_subparser.add_parser("ssl", help="Modules ssl Sub Command")

    # mmap  module sub-command
    modules_subparser_mmap = modules_subparser.add_parser("mmap", help="Modules mmap Sub Command")

    #  signal module sub-command
    modules_subparser_signal = modules_subparser.add_parser("signal", help="Modules signal Sub Command")

    # urllib  module sub-command
    modules_subparser_urllib = modules_subparser.add_parser("urllib", help="Modules urllib Sub Command")

    # http  module sub-command
    modules_subparser_http = modules_subparser.add_parser("http", help="Modules http Sub Command")

    # socketserver  module sub-command
    modules_subparser_socketserver = modules_subparser.add_parser(
        "socketserver",
        help="Modules socketserver Sub Command",
    )

    #  ipaddress module sub-command
    modules_subparser_ipaddress = modules_subparser.add_parser(
        "ipaddress",
        help="Modules ipaddress Sub Command",
    )

    # turtle  module sub-command
    modules_subparser_turtle = modules_subparser.add_parser("turtle", help="Modules turtle Sub Command")

    # cmd  module sub-command
    modules_subparser_cmd = modules_subparser.add_parser("cmd", help="Modules cmd Sub Command")

    # shlex  module sub-command
    modules_subparser_shlex = modules_subparser.add_parser("shlex", help="Modules shlex Sub Command")

    # tkinter  module sub-command
    modules_subparser_tkinter = modules_subparser.add_parser("tkinter", help="Modules tkinter Sub Command")

    # typing  module sub-command
    modules_subparser_typing = modules_subparser.add_parser("typing", help="Modules typing Sub Command")

    # pydoc  module sub-command
    modules_subparser_pydoc = modules_subparser.add_parser("pydoc", help="Modules pydoc Sub Command")

    # pdb  module sub-command
    modules_subparser_pdb = modules_subparser.add_parser("pdb", help="Modules pdb Sub Command")

    # timeit  module sub-command
    modules_subparser_timeit = modules_subparser.add_parser("timeit", help="Modules timeit Sub Command")

    # sys  module sub-command
    sys_parser = subparsers.add_parser("sys", help="Modules sys Sub Command")

    # re  module sub-command
    re_parser = subparsers.add_parser("re", help="Modules re Sub Command")

    # sysconfig  module sub-command
    modules_subparser_sysconfig = modules_subparser.add_parser(
        "sysconfig",
        help="Modules sysconfig Sub Command",
    )

    # inspect  module sub-command
    inspect_parser = subparsers.add_parser("inspect", help="Modules inspect Sub Command")

    # importlib  module sub-command
    modules_subparser_importlib = modules_subparser.add_parser(
        "importlib",
        help="Modules importlib Sub Command",
    )

    # initial parsing of the args,
    # to determine which modules are need to be loaded below
    args = parser.parse_args()

    # debug messages
    # print(vars(args))

    # set the defaults and selectively import ONLY the modules we're going to need
    if hasattr(args, "sub_parser_name"):
        if args.sub_parser_name == "play":
            if not args.play_parser:
                import scratchpad.practice

                play_parser.set_defaults(module="scratchpad.practice", cmd="play")
            elif args.play_parser == "practice":
                import scratchpad.practice

                play_subparser_practice.set_defaults(
                    func=scratchpad.practice.practice_demo,
                    cmd="practice",
                )
            elif args.play_parser == "weather":
                import scratchpad.practice

                play_subparser_weather.set_defaults(
                    module="scratchpad.practice",
                    cmd="weather",
                )

        elif args.sub_parser_name == "cookbook":

            if args.cookbook_parser == "chapter1":
                import cookbook.chapter1

                cookbook_subparser_chapter1.set_defaults(
                    func=cookbook.chapter1.cookbook_chapter1,
                    cmd="chapter1",
                )
            elif args.cookbook_parser == "chapter2":
                import cookbook.chapter2

                cookbook_subparser_chapter2.set_defaults(
                    func=cookbook.chapter2.cookbook_chapter2,
                    cmd="chapter2",
                )

            elif args.cookbook_parser == "chapter3":
                import cookbook.chapter3

                cookbook_subparser_chapter3.set_defaults(
                    func=cookbook.chapter3.cookbook_chapter3,
                    cmd="chapter3",
                )
            elif args.cookbook_parser == "chapter4":
                import cookbook.chapter4

                cookbook_subparser_chapter4.set_defaults(
                    func=cookbook.chapter4.cookbook_chapter4,
                    cmd="chapter4",
                )
            elif args.cookbook_parser == "chapter5":
                import cookbook.chapter5

                cookbook_subparser_chapter5.set_defaults(
                    func=cookbook.chapter5.cookbook_chapter5,
                    cmd="chapter5",
                )
            elif args.cookbook_parser == "chapter6":
                import cookbook.chapter6

                cookbook_subparser_chapter6.set_defaults(
                    func=cookbook.chapter6.cookbook_chapter6,
                    cmd="chapter6",
                )
            elif args.cookbook_parser == "chapter7":
                import cookbook.chapter7

                cookbook_subparser_chapter7.set_defaults(
                    func=cookbook.chapter7.cookbook_chapter7,
                    cmd="chapter7",
                )
            elif args.cookbook_parser == "chapter8":
                import cookbook.chapter8

                cookbook_subparser_chapter8.set_defaults(
                    func=cookbook.chapter8.cookbook_chapter8,
                    cmd="chapter8",
                )
            elif args.cookbook_parser == "chapter9":
                import cookbook.chapter9

                cookbook_subparser_chapter9.set_defaults(
                    func=cookbook.chapter9.cookbook_chapter9,
                    cmd="chapter9",
                )
            elif args.cookbook_parser == "chapter10":
                import cookbook.chapter10

                cookbook_subparser_chapter10.set_defaults(
                    func=cookbook.chapter10.cookbook_chapter10,
                    cmd="chapter10",
                )
            elif args.cookbook_parser == "chapter11":
                import cookbook.chapter11

                cookbook_subparser_chapter11.set_defaults(
                    func=cookbook.chapter11.cookbook_chapter11,
                    cmd="chapter11",
                )
            elif args.cookbook_parser == "chapter12":
                import cookbook.chapter12

                cookbook_subparser_chapter12.set_defaults(
                    func=cookbook.chapter12.cookbook_chapter12,
                    cmd="chapter12",
                )
            elif args.cookbook_parser == "chapter13":
                import cookbook.chapter13

                cookbook_subparser_chapter13.set_defaults(
                    func=cookbook.chapter13.cookbook_chapter13,
                    cmd="chapter13",
                )
            elif args.cookbook_parser == "chapter14":
                import cookbook.chapter14

                cookbook_subparser_chapter14.set_defaults(
                    func=cookbook.chapter14.cookbook_chapter14,
                    cmd="chapter14",
                )
            elif args.cookbook_parser == "chapter15":
                import cookbook.chapter15

                cookbook_subparser_chapter15.set_defaults(
                    func=cookbook.chapter15.cookbook_chapter15,
                    cmd="chapter15",
                )

        elif args.sub_parser_name == "concurrency":
            import libs.concurrency

            concurrency_parser.set_defaults(func=libs.concurrency.concurrency, cmd="concurrency")

        elif args.sub_parser_name == "lists":
            import me.libs.lists

            lists_parser.set_defaults(func=me.libs.lists.lists, cmd="lists")
        elif args.sub_parser_name == "dicts":
            import me.libs.dicts

            dicts_parser.set_defaults(func=me.libs.dicts.dicts, cmd="dicts")
        elif args.sub_parser_name == "decorators":
            import me.libs.decorators

            decorators_parser.set_defaults(
                func=me.libs.decorators.decorators,
                cmd="decorator",
            )

        elif args.sub_parser_name == "scope":
            import me.libs.scope

            scope_parser.set_defaults(func=me.libs.scope.scope, cmd="scope")
        elif args.sub_parser_name == "functions":
            import me.libs.functions

            functions_parser.set_defaults(
                func=me.libs.functions.functions,
                cmd="functions",
            )
        elif args.sub_parser_name == "truthy":
            import me.libs.truthy

            truthy_parser.set_defaults(func=me.libs.truthy.truthy, cmd="truthy")
        elif args.sub_parser_name == "iterators":
            import me.libs.iterators

            iterators_parser.set_defaults(
                func=me.libs.iterators.iterators,
                cmd="iterators",
            )
        elif args.sub_parser_name == "lambdas":
            import me.libs.lambdas

            lambdas_parser.set_defaults(
                func=me.libs.lambdas.lambdas,
                cmd="lambdas",
            )
        elif args.sub_parser_name == "generators":
            import me.libs.generators

            generators_parser.set_defaults(
                func=me.libs.generators.generators,
                cmd="generators",
            )
        elif args.sub_parser_name == "tuples":
            import me.libs.tuples

            tuples_parser.set_defaults(func=me.libs.tuples.tuples, cmd="tuples")
        elif args.sub_parser_name == "strings":
            import me.libs.strings

            strings_parser.set_defaults(
                func=me.libs.strings.strings,
                cmd="strings",
            )
        elif args.sub_parser_name == "sets":
            import me.libs.sets

            sets_parser.set_defaults(func=me.libs.sets.sets, cmd="sets")
        elif args.sub_parser_name == "exceptions":
            import me.libs.exceptions

            exceptions_parser.set_defaults(
                func=me.libs.exceptions.exceptions,
                cmd="exceptions",
            )
        elif args.sub_parser_name == "filedir":
            import me.libs.filedir

            filedir_parser.set_defaults(
                func=me.libs.filedir.filedir,
                cmd="filedir",
            )
        elif args.sub_parser_name == "unix":
            import me.libs.unix

            unix_parser.set_defaults(func=me.libs.unix.unix, cmd="unix")
        elif args.sub_parser_name == "networking":
            import me.libs.networking_IPC

            networking_parser.set_defaults(
                func=me.libs.networking_IPC.network,
                cmd="networking",
            )
        elif args.sub_parser_name == "threading":
            import me.libs.threading

            threading_parser.set_defaults(
                func=me.libs.threading.threading,
                cmd="threading",
            )
        elif args.sub_parser_name == "multiprocessing":
            import me.libs.multiprocessing

            multiprocessing_parser.set_defaults(
                func=me.libs.multiprocessing.multiprocessing,
                cmd="multiprocessing",
            )
        elif args.sub_parser_name == "async":
            import me.libs.async_

            async_parser.set_defaults(func=me.libs.async_.async_, cmd="async_")
        elif args.sub_parser_name == "coroutine":
            import me.libs.coroutine

            coroutine_parser.set_defaults(
                func=me.libs.coroutine.coroutine,
                cmd="coroutine",
            )
        elif args.sub_parser_name == "numerics":
            import me.libs.numerics

            numerics_parser.set_defaults(
                func=me.libs.numerics.numerics,
                cmd="numerics",
            )
        elif args.sub_parser_name == "comparisons":
            import me.libs.comparisons

            comparisons_parser.set_defaults(
                func=me.libs.comparisons.comparisons,
                cmd="comparisons",
            )
        elif args.sub_parser_name == "compression":
            import me.libs.compression

            compression_parser.set_defaults(
                func=me.libs.compression.compression,
                cmd="compression",
            )
        elif args.sub_parser_name == "internet":
            import me.libs.internet

            internet_parser.set_defaults(
                func=me.libs.internet.internet,
                cmd="internet",
            )
        elif args.sub_parser_name == "astral":
            import libs.astral

            astral_parser.set_defaults(
                func=libs.astral.astral_module,
                cmd="modules.astral",
            )
        elif args.sub_parser_name == "opencv":
            import libs.opencv

            opencv_parser.set_defaults(
                func=libs.opencv.opencv_module,
                cmd="modules.opencv",
            )
        elif args.sub_parser_name == "sys":
            import libs.sys

            sys_parser.set_defaults(
                func=libs.sys.sys_module,
                cmd="modules.sys",
            )
        elif args.sub_parser_name == "re":
            import libs.re

            re_parser.set_defaults(func=libs.re.re_module, cmd="re")

        elif args.sub_parser_name == "ds":
            import libs.ds

            ds_parser.set_defaults(
                func=libs.ds.ds_module,
                cmd="modules.ds",
            )
        elif args.sub_parser_name == "inspect":
            import libs.inspect

            inspect_parser.set_defaults(
                func=libs.inspect.inspect_module,
                cmd="modules.inspect",
            )
        elif args.sub_parser_name == "modules":
            if not args.modules_parser:
                import me.libs.modules as modules

                modules_parser.set_defaults(
                    func=modules.modules,
                    cmd="modules",
                )

            elif args.modules_parser == "requests":
                import me.libs.modules as modules

                modules_subparser_requests.set_defaults(
                    func=modules.modules_requests,
                    cmd="modules.requests",
                )
            elif args.modules_parser == "datetime":
                import me.libs.modules as modules

                modules_subparser_datetime.set_defaults(
                    func=modules.modules_datetime,
                    cmd="modules.datetime",
                )
            elif args.modules_parser == "collections":
                import me.libs.modules as modules

                modules_subparser_collections.set_defaults(
                    func=modules.modules_collections,
                    cmd="modules.collections",
                )
            elif args.modules_parser == "heapq":
                import me.libs.modules as modules

                modules_subparser_heapq.set_defaults(
                    func=modules.modules_heapq,
                    cmd="modules.heapq",
                )
            elif args.modules_parser == "bisect":
                import me.libs.modules as modules

                modules_subparser_bisect.set_defaults(
                    func=modules.modules_bisect,
                    cmd="modules.bisect",
                )
            elif args.modules_parser == "types":
                import me.libs.modules as modules

                modules_subparser_types.set_defaults(
                    func=modules.modules_types,
                    cmd="modules.types",
                )
            elif args.modules_parser == "array":
                import me.libs.modules as modules

                modules_subparser_array.set_defaults(
                    func=modules.modules_array,
                    cmd="modules.array",
                )
            elif args.modules_parser == "copy":
                import me.libs.modules as modules

                modules_subparser_copy.set_defaults(
                    func=modules.modules_copy,
                    cmd="modules.copy",
                )
            elif args.modules_parser == "pprint":
                import me.libs.modules as modules

                modules_subparser_pprint.set_defaults(
                    func=modules.modules_pprint,
                    cmd="modules.pprint",
                )
            elif args.modules_parser == "math":
                import me.libs.modules as modules

                modules_subparser_math.set_defaults(
                    func=modules.modules_math,
                    cmd="modules.math",
                )
            elif args.modules_parser == "random":
                import me.libs.modules as modules

                modules_subparser_random.set_defaults(
                    func=modules.modules_random,
                    cmd="modules.random",
                )
            elif args.modules_parser == "statistics":
                import me.libs.modules as modules

                modules_subparser_statistics.set_defaults(
                    func=modules.modules_statistics,
                    cmd="modules.statistics",
                )
            elif args.modules_parser == "itertools":
                import me.libs.modules as modules

                modules_subparser_itertools.set_defaults(
                    func=modules.modules_itertools,
                    cmd="modules.itertools",
                )
            elif args.modules_parser == "functools":
                import me.libs.modules as modules

                modules_subparser_functools.set_defaults(
                    func=modules.modules_functools,
                    cmd="modules.functools",
                )
            elif args.modules_parser == "operator":
                import me.libs.modules as modules

                modules_subparser_operator.set_defaults(
                    func=modules.modules_operator,
                    cmd="modules.operator",
                )
            elif args.modules_parser == "pathlib":
                import me.libs.modules as modules

                modules_subparser_pathlib.set_defaults(
                    func=modules.modules_pathlib,
                    cmd="modules.pathlib",
                )
            elif args.modules_parser == "os":
                import me.libs.modules as modules

                modules_subparser_os.set_defaults(
                    func=modules.modules_os,
                    cmd="modules.os",
                )
            elif args.modules_parser == "glob":
                import me.libs.modules as modules

                modules_subparser_glob.set_defaults(
                    func=modules.modules_glob,
                    cmd="modules.glob",
                )
            elif args.modules_parser == "fnmatch":
                import me.libs.modules as modules

                modules_subparser_fnmatch.set_defaults(
                    func=modules.modules_fnmatch,
                    cmd="modules.fnmatch",
                )
            elif args.modules_parser == "shutil":
                import me.libs.modules as modules

                modules_subparser_shutil.set_defaults(
                    func=modules.modules_shutil,
                    cmd="modules.shutil",
                )
            elif args.modules_parser == "sqlite3":
                import me.libs.modules as modules

                modules_subparser_sqlite3.set_defaults(
                    func=modules.modules_sqlite3,
                    cmd="modules.sqlite3",
                )
            elif args.modules_parser == "csv":
                import me.libs.modules as modules

                modules_subparser_csv.set_defaults(
                    func=modules.modules_csv,
                    cmd="modules.csv",
                )
            elif args.modules_parser == "json":
                import me.libs.modules as modules

                modules_subparser_json.set_defaults(
                    func=modules.modules_json,
                    cmd="modules.json",
                )
            elif args.modules_parser == "configparser":
                import me.libs.modules as modules

                modules_subparser_configparser.set_defaults(
                    func=modules.modules_configparser,
                    cmd="modules.configparser",
                )
            elif args.modules_parser == "io":
                import me.libs.modules as modules

                modules_subparser_io.set_defaults(
                    func=modules.modules_io,
                    cmd="modules.io",
                )
            elif args.modules_parser == "time":
                import me.libs.modules as modules

                modules_subparser_time.set_defaults(
                    func=modules.modules_time,
                    cmd="modules.time",
                )
            elif args.modules_parser == "errno":
                import me.libs.modules as modules

                modules_subparser_errno.set_defaults(
                    func=modules.modules_errno,
                    cmd="modules.errno",
                )
            elif args.modules_parser == "curses":
                import me.libs.modules as modules

                modules_subparser_curses.set_defaults(
                    func=modules.modules_curses,
                    cmd="modules.curses",
                )
            elif args.modules_parser == "ctypes":
                import me.libs.modules as modules

                modules_subparser_ctypes.set_defaults(
                    func=modules.modules_ctypes,
                    cmd="modules.ctypes",
                )
            elif args.modules_parser == "threading":
                import me.libs.modules as modules

                modules_subparser_threading.set_defaults(
                    func=modules.modules_threading,
                    cmd="modules.threading",
                )
            elif args.modules_parser == "multiprocessing":
                import me.libs.modules as modules

                modules_subparser_multiprocessing.set_defaults(
                    func=modules.modules_multiprocessing,
                    cmd="modules.multiprocessing",
                )
            elif args.modules_parser == "subprocess":
                import me.libs.modules as modules

                modules_subparser_subprocess.set_defaults(
                    func=modules.modules_subprocess,
                    cmd="modules.subprocess",
                )
            elif args.modules_parser == "sched":
                import me.libs.modules as modules

                modules_subparser_sched.set_defaults(
                    func=modules.modules_sched,
                    cmd="modules.sched",
                )
            elif args.modules_parser == "queue":
                import me.libs.modules as modules

                modules_subparser_queue.set_defaults(
                    func=modules.modules_queue,
                    cmd="modules.queue",
                )
            elif args.modules_parser == "_thread":
                import me.libs.modules as modules

                modules_subparser__thread.set_defaults(
                    func=modules.modules__thread,
                    cmd="modules._thread",
                )
            elif args.modules_parser == "asyncio":
                import me.libs.modules as modules

                modules_subparser_asyncio.set_defaults(
                    func=modules.modules_asyncio,
                    cmd="modules.asyncio",
                )
            elif args.modules_parser == "socket":
                import me.libs.modules as modules

                modules_subparser_socket.set_defaults(
                    func=modules.modules_socket,
                    cmd="modules.socket",
                )
            elif args.modules_parser == "ssl":
                import me.libs.modules as modules

                modules_subparser_ssl.set_defaults(
                    func=modules.modules_ssl,
                    cmd="modules.ssl",
                )
            elif args.modules_parser == "mmap":
                import me.libs.modules as modules

                modules_subparser_mmap.set_defaults(
                    func=modules.modules_mmap,
                    cmd="modules.mmap",
                )
            elif args.modules_parser == "signal":
                import me.libs.modules as modules

                modules_subparser_signal.set_defaults(
                    func=modules.modules_signal,
                    cmd="modules.signal",
                )
            elif args.modules_parser == "urllib":
                import me.libs.modules as modules

                modules_subparser_urllib.set_defaults(
                    func=modules.modules_urllib,
                    cmd="modules.urllib",
                )
            elif args.modules_parser == "http":
                import me.libs.modules as modules

                modules_subparser_http.set_defaults(
                    func=modules.modules_http,
                    cmd="modules.http",
                )
            elif args.modules_parser == "socketserver":
                import me.libs.modules as modules

                modules_subparser_socketserver.set_defaults(
                    func=modules.modules_socketserver,
                    cmd="modules.socketserver",
                )
            elif args.modules_parser == "ipaddress":
                import me.libs.modules as modules

                modules_subparser_ipaddress.set_defaults(
                    func=modules.modules_ipaddress,
                    cmd="modules.ipaddress",
                )
            elif args.modules_parser == "turtle":
                import me.libs.modules as modules

                modules_subparser_turtle.set_defaults(
                    func=modules.modules_turtle,
                    cmd="modules.turtle",
                )
            elif args.modules_parser == "cmd":
                import me.libs.modules as modules

                modules_subparser_cmd.set_defaults(
                    func=modules.modules_cmd,
                    cmd="modules.cmd",
                )
            elif args.modules_parser == "shlex":
                import me.libs.modules as modules

                modules_subparser_shlex.set_defaults(
                    func=modules.modules_shlex,
                    cmd="modules.shlex",
                )
            elif args.modules_parser == "tkinter":
                import me.libs.modules as modules

                modules_subparser_tkinter.set_defaults(
                    func=modules.modules_tkinter,
                    cmd="modules.tkinter",
                )
            elif args.modules_parser == "typing":
                import me.libs.modules as modules

                modules_subparser_typing.set_defaults(
                    func=modules.modules_typing,
                    cmd="modules.typing",
                )
            elif args.modules_parser == "pydoc":
                import me.libs.modules as modules

                modules_subparser_pydoc.set_defaults(
                    func=modules.modules_pydoc,
                    cmd="modules.pydoc",
                )
            elif args.modules_parser == "pdb":
                import me.libs.modules as modules

                modules_subparser_pdb.set_defaults(
                    func=modules.modules_pdb,
                    cmd="modules.pdb",
                )
            elif args.modules_parser == "timeit":
                import me.libs.modules as modules

                modules_subparser_timeit.set_defaults(
                    func=modules.modules_timeit,
                    cmd="modules.timeit",
                )

            elif args.modules_parser == "sysconfig":
                import me.libs.modules as modules

                modules_subparser_sysconfig.set_defaults(
                    func=modules.modules_sysconfig,
                    cmd="modules.sysconfig",
                )

            elif args.modules_parser == "importlib":
                import me.libs.modules as modules

                modules_subparser_importlib.set_defaults(
                    func=modules.modules_importlib,
                    cmd="modules.importlib",
                )

    # args = parser.parse_args()

    # # debug messages
    # ##    print("after re parsing args...")
    # ##    print(vars(args))

    # return args

    # return parser.parse_args()
    return parser
