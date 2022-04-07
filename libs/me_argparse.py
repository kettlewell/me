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
  * concurrent
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

I put all the calling code into the libs directory... I think that is incorrect, and should be split out differently


"""
import argparse  # noqa: E402

# import libs
# import libs.me_modules
# import libs.me_lists

# import scratchpad.practice

# print("scratchpad.practice.__dict__  :")
# print(scratchpad.practice.__dict__)
# print(' ')


def me_parse():  # noqa: WPS210 WPS213 WPS231 C901 CCR001 CFQ001
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

    # import libs.me_scope
    scope_parser = subparsers.add_parser("scope", help="Scope  commands")

    # import libs.me_functions
    functions_parser = subparsers.add_parser("functions", help="Function (builtin) commands")

    # import libs.me_truthy
    truthy_parser = subparsers.add_parser("truthy", help="Truthy commands")

    # import libs.me_iterators
    iterators_parser = subparsers.add_parser("iterators", help="Iterators commands")

    # import libs.me_lambdas
    lambdas_parser = subparsers.add_parser("lambdas", help="Lambdas commands")

    # import libs.me_generators
    generators_parser = subparsers.add_parser("generators", help="generators commands")

    # import libs.me_tuples
    tuples_parser = subparsers.add_parser("tuples", help="tuples commands")

    # import libs.me_strings
    strings_parser = subparsers.add_parser("strings", help="Strings commands")

    # import libs.me_sets
    sets_parser = subparsers.add_parser("sets", help="sets commands")

    # import libs.me_exceptions
    exceptions_parser = subparsers.add_parser("exceptions", help="Exceptions commands")

    # import libs.me_filedir
    filedir_parser = subparsers.add_parser("filedir", help="File and Directory commands")

    # import libs.me_unix
    unix_parser = subparsers.add_parser("unix", help="Unix commands")

    # import libs.me_networking_IPC
    networking_parser = subparsers.add_parser("networking", help="Networking and IPC commands")

    # import libs.me_threading
    threading_parser = subparsers.add_parser("threading", help="Threading commands")

    # import libs.me_multiprocessing
    multiprocessing_parser = subparsers.add_parser("multiprocessing", help="Multiprocessing commands")

    # import libs.me_async
    async_parser = subparsers.add_parser("async", help="async commands")

    # import libs.me_coroutine
    coroutine_parser = subparsers.add_parser("coroutine", help="coroutine commands")

    # import libs.me_numerics
    numerics_parser = subparsers.add_parser("numerics", help="numerics commands")

    # import libs.me_comparisons
    comparisons_parser = subparsers.add_parser("comparisons", help="comparison commands")

    # import libs.me_compression
    compression_parser = subparsers.add_parser("compression", help="Compression commands")

    # import libs.me_internet
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
    modules_subparser_astral = modules_subparser.add_parser("astral", help="Modules astral Sub Command")

    # opencv module sub-command
    modules_subparser_opencv = modules_subparser.add_parser("opencv", help="Modules opencv Sub Command")

    # ds ( data science ) module sub-command
    modules_subparser_ds = modules_subparser.add_parser("ds", help="Modules Data Science Sub Command")

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

    # concurrent module sub-command
    modules_subparser_concurrent = modules_subparser.add_parser(
        "concurrent",
        help="Modules concurrent Sub Command",
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
    modules_subparser_sys = modules_subparser.add_parser("sys", help="Modules sys Sub Command")

    # re  module sub-command
    modules_subparser_re = modules_subparser.add_parser("re", help="Modules re Sub Command")

    # sysconfig  module sub-command
    modules_subparser_sysconfig = modules_subparser.add_parser(
        "sysconfig",
        help="Modules sysconfig Sub Command",
    )

    # inspect  module sub-command
    modules_subparser_inspect = modules_subparser.add_parser("inspect", help="Modules inspect Sub Command")

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
                import libs.me_cookbook.chapter1

                cookbook_subparser_chapter1.set_defaults(
                    func=libs.me_cookbook.chapter1.me_cookbook_chapter1,
                    cmd="chapter1",
                )
            elif args.cookbook_parser == "chapter2":
                import libs.me_cookbook.chapter2

                cookbook_subparser_chapter2.set_defaults(
                    func=libs.me_cookbook.chapter2.me_cookbook_chapter2,
                    cmd="chapter2",
                )

        elif args.sub_parser_name == "lists":
            import libs.me_lists

            lists_parser.set_defaults(func=libs.me_lists.me_lists, cmd="lists")
        elif args.sub_parser_name == "dicts":
            import libs.me_dicts

            dicts_parser.set_defaults(func=libs.me_dicts.me_dicts, cmd="dicts")
        elif args.sub_parser_name == "decorators":
            import libs.me_decorators

            decorators_parser.set_defaults(
                func=libs.me_decorators.me_decorators,
                cmd="decorator",
            )

        elif args.sub_parser_name == "scope":
            import libs.me_scope

            scope_parser.set_defaults(func=libs.me_scope.me_scope, cmd="scope")
        elif args.sub_parser_name == "functions":
            import libs.me_functions

            functions_parser.set_defaults(
                func=libs.me_functions.me_functions,
                cmd="functions",
            )
        elif args.sub_parser_name == "truthy":
            import libs.me_truthy

            truthy_parser.set_defaults(func=libs.me_truthy.me_truthy, cmd="truthy")
        elif args.sub_parser_name == "iterators":
            import libs.me_iterators

            iterators_parser.set_defaults(
                func=libs.me_iterators.me_iterators,
                cmd="iterators",
            )
        elif args.sub_parser_name == "lambdas":
            import libs.me_lambdas

            lambdas_parser.set_defaults(
                func=libs.me_lambdas.me_lambdas,
                cmd="lambdas",
            )
        elif args.sub_parser_name == "generators":
            import libs.me_generators

            generators_parser.set_defaults(
                func=libs.me_generators.me_generators,
                cmd="generators",
            )
        elif args.sub_parser_name == "tuples":
            import libs.me_tuples

            tuples_parser.set_defaults(func=libs.me_tuples.me_tuples, cmd="tuples")
        elif args.sub_parser_name == "strings":
            import libs.me_strings

            strings_parser.set_defaults(
                func=libs.me_strings.me_strings,
                cmd="strings",
            )
        elif args.sub_parser_name == "sets":
            import libs.me_sets

            sets_parser.set_defaults(func=libs.me_sets.me_sets, cmd="sets")
        elif args.sub_parser_name == "exceptions":
            import libs.me_exceptions

            exceptions_parser.set_defaults(
                func=libs.me_exceptions.me_exceptions,
                cmd="exceptions",
            )
        elif args.sub_parser_name == "filedir":
            import libs.me_filedir

            filedir_parser.set_defaults(
                func=libs.me_filedir.me_filedir,
                cmd="filedir",
            )
        elif args.sub_parser_name == "unix":
            import libs.me_unix

            unix_parser.set_defaults(func=libs.me_unix.me_unix, cmd="unix")
        elif args.sub_parser_name == "networking":
            import libs.me_networking_IPC

            networking_parser.set_defaults(
                func=libs.me_networking_IPC.me_network,
                cmd="networking",
            )
        elif args.sub_parser_name == "threading":
            import libs.me_threading

            threading_parser.set_defaults(
                func=libs.me_threading.me_threading,
                cmd="threading",
            )
        elif args.sub_parser_name == "multiprocessing":
            import libs.me_multiprocessing

            multiprocessing_parser.set_defaults(
                func=libs.me_multiprocessing.me_multiprocessing,
                cmd="multiprocessing",
            )
        elif args.sub_parser_name == "async":
            import libs.me_async

            async_parser.set_defaults(func=libs.me_async.me_async, cmd="async")
        elif args.sub_parser_name == "coroutine":
            import libs.me_coroutine

            coroutine_parser.set_defaults(
                func=libs.me_coroutine.me_coroutine,
                cmd="coroutine",
            )
        elif args.sub_parser_name == "numerics":
            import libs.me_numerics

            numerics_parser.set_defaults(
                func=libs.me_numerics.me_numerics,
                cmd="numerics",
            )
        elif args.sub_parser_name == "comparisons":
            import libs.me_comparisons

            comparisons_parser.set_defaults(
                func=libs.me_comparisons.me_comparisons,
                cmd="comparisons",
            )
        elif args.sub_parser_name == "compression":
            import libs.me_compression

            compression_parser.set_defaults(
                func=libs.me_compression.me_compression,
                cmd="compression",
            )
        elif args.sub_parser_name == "internet":
            import libs.me_internet

            internet_parser.set_defaults(
                func=libs.me_internet.me_internet,
                cmd="internet",
            )
        elif args.sub_parser_name == "modules":
            if not args.modules_parser:
                import libs.me_modules as me_modules

                modules_parser.set_defaults(
                    func=me_modules.me_modules,
                    cmd="modules",
                )
            elif args.modules_parser == "astral":
                import libs.modules.me_modules_astral

                modules_subparser_astral.set_defaults(
                    func=libs.modules.me_modules_astral.me_modules_astral,
                    cmd="modules.astral",
                )
            elif args.modules_parser == "opencv":
                import libs.modules.me_modules_opencv

                modules_subparser_opencv.set_defaults(
                    func=libs.modules.me_modules_opencv.me_modules_opencv,
                    cmd="modules.opencv",
                )
            elif args.modules_parser == "sys":
                import libs.modules.me_modules_sys

                modules_subparser_sys.set_defaults(
                    func=libs.modules.me_modules_sys.me_modules_sys,
                    cmd="modules.sys",
                )
            elif args.modules_parser == "re":
                import libs.modules.me_modules_re

                modules_subparser_re.set_defaults(func=libs.modules.me_modules_re.me_modules_re, cmd="re")

            elif args.modules_parser == "ds":
                import libs.modules.me_modules_ds

                modules_subparser_ds.set_defaults(
                    func=libs.modules.me_modules_ds.me_modules_ds,
                    cmd="modules.ds",
                )
            elif args.modules_parser == "requests":
                import libs.me_modules as me_modules

                modules_subparser_requests.set_defaults(
                    func=me_modules.me_modules_requests,
                    cmd="modules.requests",
                )
            elif args.modules_parser == "datetime":
                import libs.me_modules as me_modules

                modules_subparser_datetime.set_defaults(
                    func=me_modules.me_modules_datetime,
                    cmd="modules.datetime",
                )
            elif args.modules_parser == "collections":
                import libs.me_modules as me_modules

                modules_subparser_collections.set_defaults(
                    func=me_modules.me_modules_collections,
                    cmd="modules.collections",
                )
            elif args.modules_parser == "heapq":
                import libs.me_modules as me_modules

                modules_subparser_heapq.set_defaults(
                    func=me_modules.me_modules_heapq,
                    cmd="modules.heapq",
                )
            elif args.modules_parser == "bisect":
                import libs.me_modules as me_modules

                modules_subparser_bisect.set_defaults(
                    func=me_modules.me_modules_bisect,
                    cmd="modules.bisect",
                )
            elif args.modules_parser == "types":
                import libs.me_modules as me_modules

                modules_subparser_types.set_defaults(
                    func=me_modules.me_modules_types,
                    cmd="modules.types",
                )
            elif args.modules_parser == "array":
                import libs.me_modules as me_modules

                modules_subparser_array.set_defaults(
                    func=me_modules.me_modules_array,
                    cmd="modules.array",
                )
            elif args.modules_parser == "copy":
                import libs.me_modules as me_modules

                modules_subparser_copy.set_defaults(
                    func=me_modules.me_modules_copy,
                    cmd="modules.copy",
                )
            elif args.modules_parser == "pprint":
                import libs.me_modules as me_modules

                modules_subparser_pprint.set_defaults(
                    func=me_modules.me_modules_pprint,
                    cmd="modules.pprint",
                )
            elif args.modules_parser == "math":
                import libs.me_modules as me_modules

                modules_subparser_math.set_defaults(
                    func=me_modules.me_modules_math,
                    cmd="modules.math",
                )
            elif args.modules_parser == "random":
                import libs.me_modules as me_modules

                modules_subparser_random.set_defaults(
                    func=me_modules.me_modules_random,
                    cmd="modules.random",
                )
            elif args.modules_parser == "statistics":
                import libs.me_modules as me_modules

                modules_subparser_statistics.set_defaults(
                    func=me_modules.me_modules_statistics,
                    cmd="modules.statistics",
                )
            elif args.modules_parser == "itertools":
                import libs.me_modules as me_modules

                modules_subparser_itertools.set_defaults(
                    func=me_modules.me_modules_itertools,
                    cmd="modules.itertools",
                )
            elif args.modules_parser == "functools":
                import libs.me_modules as me_modules

                modules_subparser_functools.set_defaults(
                    func=me_modules.me_modules_functools,
                    cmd="modules.functools",
                )
            elif args.modules_parser == "operator":
                import libs.me_modules as me_modules

                modules_subparser_operator.set_defaults(
                    func=me_modules.me_modules_operator,
                    cmd="modules.operator",
                )
            elif args.modules_parser == "pathlib":
                import libs.me_modules as me_modules

                modules_subparser_pathlib.set_defaults(
                    func=me_modules.me_modules_pathlib,
                    cmd="modules.pathlib",
                )
            elif args.modules_parser == "os":
                import libs.me_modules as me_modules

                modules_subparser_os.set_defaults(
                    func=me_modules.me_modules_os,
                    cmd="modules.os",
                )
            elif args.modules_parser == "glob":
                import libs.me_modules as me_modules

                modules_subparser_glob.set_defaults(
                    func=me_modules.me_modules_glob,
                    cmd="modules.glob",
                )
            elif args.modules_parser == "fnmatch":
                import libs.me_modules as me_modules

                modules_subparser_fnmatch.set_defaults(
                    func=me_modules.me_modules_fnmatch,
                    cmd="modules.fnmatch",
                )
            elif args.modules_parser == "shutil":
                import libs.me_modules as me_modules

                modules_subparser_shutil.set_defaults(
                    func=me_modules.me_modules_shutil,
                    cmd="modules.shutil",
                )
            elif args.modules_parser == "sqlite3":
                import libs.me_modules as me_modules

                modules_subparser_sqlite3.set_defaults(
                    func=me_modules.me_modules_sqlite3,
                    cmd="modules.sqlite3",
                )
            elif args.modules_parser == "csv":
                import libs.me_modules as me_modules

                modules_subparser_csv.set_defaults(
                    func=me_modules.me_modules_csv,
                    cmd="modules.csv",
                )
            elif args.modules_parser == "json":
                import libs.me_modules as me_modules

                modules_subparser_json.set_defaults(
                    func=me_modules.me_modules_json,
                    cmd="modules.json",
                )
            elif args.modules_parser == "configparser":
                import libs.me_modules as me_modules

                modules_subparser_configparser.set_defaults(
                    func=me_modules.me_modules_configparser,
                    cmd="modules.configparser",
                )
            elif args.modules_parser == "io":
                import libs.me_modules as me_modules

                modules_subparser_io.set_defaults(
                    func=me_modules.me_modules_io,
                    cmd="modules.io",
                )
            elif args.modules_parser == "time":
                import libs.me_modules as me_modules

                modules_subparser_time.set_defaults(
                    func=me_modules.me_modules_time,
                    cmd="modules.time",
                )
            elif args.modules_parser == "errno":
                import libs.me_modules as me_modules

                modules_subparser_errno.set_defaults(
                    func=me_modules.me_modules_errno,
                    cmd="modules.errno",
                )
            elif args.modules_parser == "curses":
                import libs.me_modules as me_modules

                modules_subparser_curses.set_defaults(
                    func=me_modules.me_modules_curses,
                    cmd="modules.curses",
                )
            elif args.modules_parser == "ctypes":
                import libs.me_modules as me_modules

                modules_subparser_ctypes.set_defaults(
                    func=me_modules.me_modules_ctypes,
                    cmd="modules.ctypes",
                )
            elif args.modules_parser == "threading":
                import libs.me_modules as me_modules

                modules_subparser_threading.set_defaults(
                    func=me_modules.me_modules_threading,
                    cmd="modules.threading",
                )
            elif args.modules_parser == "multiprocessing":
                import libs.me_modules as me_modules

                modules_subparser_multiprocessing.set_defaults(
                    func=me_modules.me_modules_multiprocessing,
                    cmd="modules.multiprocessing",
                )
            elif args.modules_parser == "concurrent":
                import libs.me_modules as me_modules

                modules_subparser_concurrent.set_defaults(
                    func=me_modules.me_modules_concurrent,
                    cmd="modules.concurrent",
                )
            elif args.modules_parser == "subprocess":
                import libs.me_modules as me_modules

                modules_subparser_subprocess.set_defaults(
                    func=me_modules.me_modules_subprocess,
                    cmd="modules.subprocess",
                )
            elif args.modules_parser == "sched":
                import libs.me_modules as me_modules

                modules_subparser_sched.set_defaults(
                    func=me_modules.me_modules_sched,
                    cmd="modules.sched",
                )
            elif args.modules_parser == "queue":
                import libs.me_modules as me_modules

                modules_subparser_queue.set_defaults(
                    func=me_modules.me_modules_queue,
                    cmd="modules.queue",
                )
            elif args.modules_parser == "_thread":
                import libs.me_modules as me_modules

                modules_subparser__thread.set_defaults(
                    func=me_modules.me_modules__thread,
                    cmd="modules._thread",
                )
            elif args.modules_parser == "asyncio":
                import libs.me_modules as me_modules

                modules_subparser_asyncio.set_defaults(
                    func=me_modules.me_modules_asyncio,
                    cmd="modules.asyncio",
                )
            elif args.modules_parser == "socket":
                import libs.me_modules as me_modules

                modules_subparser_socket.set_defaults(
                    func=me_modules.me_modules_socket,
                    cmd="modules.socket",
                )
            elif args.modules_parser == "ssl":
                import libs.me_modules as me_modules

                modules_subparser_ssl.set_defaults(
                    func=me_modules.me_modules_ssl,
                    cmd="modules.ssl",
                )
            elif args.modules_parser == "mmap":
                import libs.me_modules as me_modules

                modules_subparser_mmap.set_defaults(
                    func=me_modules.me_modules_mmap,
                    cmd="modules.mmap",
                )
            elif args.modules_parser == "signal":
                import libs.me_modules as me_modules

                modules_subparser_signal.set_defaults(
                    func=me_modules.me_modules_signal,
                    cmd="modules.signal",
                )
            elif args.modules_parser == "urllib":
                import libs.me_modules as me_modules

                modules_subparser_urllib.set_defaults(
                    func=me_modules.me_modules_urllib,
                    cmd="modules.urllib",
                )
            elif args.modules_parser == "http":
                import libs.me_modules as me_modules

                modules_subparser_http.set_defaults(
                    func=me_modules.me_modules_http,
                    cmd="modules.http",
                )
            elif args.modules_parser == "socketserver":
                import libs.me_modules as me_modules

                modules_subparser_socketserver.set_defaults(
                    func=me_modules.me_modules_socketserver,
                    cmd="modules.socketserver",
                )
            elif args.modules_parser == "ipaddress":
                import libs.me_modules as me_modules

                modules_subparser_ipaddress.set_defaults(
                    func=me_modules.me_modules_ipaddress,
                    cmd="modules.ipaddress",
                )
            elif args.modules_parser == "turtle":
                import libs.me_modules as me_modules

                modules_subparser_turtle.set_defaults(
                    func=me_modules.me_modules_turtle,
                    cmd="modules.turtle",
                )
            elif args.modules_parser == "cmd":
                import libs.me_modules as me_modules

                modules_subparser_cmd.set_defaults(
                    func=me_modules.me_modules_cmd,
                    cmd="modules.cmd",
                )
            elif args.modules_parser == "shlex":
                import libs.me_modules as me_modules

                modules_subparser_shlex.set_defaults(
                    func=me_modules.me_modules_shlex,
                    cmd="modules.shlex",
                )
            elif args.modules_parser == "tkinter":
                import libs.me_modules as me_modules

                modules_subparser_tkinter.set_defaults(
                    func=me_modules.me_modules_tkinter,
                    cmd="modules.tkinter",
                )
            elif args.modules_parser == "typing":
                import libs.me_modules as me_modules

                modules_subparser_typing.set_defaults(
                    func=me_modules.me_modules_typing,
                    cmd="modules.typing",
                )
            elif args.modules_parser == "pydoc":
                import libs.me_modules as me_modules

                modules_subparser_pydoc.set_defaults(
                    func=me_modules.me_modules_pydoc,
                    cmd="modules.pydoc",
                )
            elif args.modules_parser == "pdb":
                import libs.me_modules as me_modules

                modules_subparser_pdb.set_defaults(
                    func=me_modules.me_modules_pdb,
                    cmd="modules.pdb",
                )
            elif args.modules_parser == "timeit":
                import libs.me_modules as me_modules

                modules_subparser_timeit.set_defaults(
                    func=me_modules.me_modules_timeit,
                    cmd="modules.timeit",
                )

            elif args.modules_parser == "sysconfig":
                import libs.me_modules as me_modules

                modules_subparser_sysconfig.set_defaults(
                    func=me_modules.me_modules_sysconfig,
                    cmd="modules.sysconfig",
                )
            elif args.modules_parser == "inspect":
                import libs.modules.me_modules_inspect

                modules_subparser_inspect.set_defaults(
                    func=libs.modules.me_modules_inspect.me_modules_inspect,
                    cmd="modules.inspect",
                )
            elif args.modules_parser == "importlib":
                import libs.me_modules as me_modules

                modules_subparser_importlib.set_defaults(
                    func=me_modules.me_modules_importlib,
                    cmd="modules.importlib",
                )

    # args = parser.parse_args()

    # # debug messages
    # ##    print("after re parsing args...")
    # ##    print(vars(args))

    # return args

    # return parser.parse_args()
    return parser
