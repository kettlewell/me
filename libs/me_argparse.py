#!/usr/bin/env python3
'''Argument parsing with sub parsers'''

"""
The general idea will be to create sub parsers for testing various things

main [options] [list|dict|generator|collection] [sub-commands]

original outline consideration: https://docs.python.org/3/library/index.html


Completed (relative term meaning, I'm probably not going to do much more with it):


In Progress:



Stubbed in:
* lists
* dicts
* re
* scope
* functions
* truthy
* iterators
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


TODO: 

I put all the calling code into the libs directory... I think that is incorrect, and should be split out differently


"""
import argparse
import libs.me_lists
import libs.me_dicts
import libs.me_re

import libs.me_scope
import libs.me_functions
import libs.me_truthy
import libs.me_iterators
import libs.me_lambdas
import libs.me_generators
import libs.me_tuples
import libs.me_strings
import libs.me_sets
import libs.me_exceptions
import libs.me_filedir
import libs.me_unix
import libs.me_networking_IPC
import libs.me_threading
import libs.me_multiprocessing
import libs.me_async
import libs.me_coroutine
import libs.me_numerics
import libs.me_comparisons
import libs.me_compression
import libs.me_internet
import libs.me_decorators

import libs.me_modules
import scratchpad.practice

def me_parse():
    parser = argparse.ArgumentParser(description='Demo program that highlights a lot of functionality of the python programming language.')

    # general / global arguments
    parser.add_argument('--practice', '-p', help="practice runs",  action='store_true') # example calling a module from arguments
    parser.add_argument('--verbose', '-v',  help="verbose levels", action='count', default=0)
    parser.add_argument('--log', '-l',      help="log level",      choices=['debug', 'info', 'warning', 'error', 'critical'], default='info')
    
    # create first level sub-parser
    subparsers = parser.add_subparsers(help="Available Subcommands", description="Sub commands for executing specific code blocks", dest="sub_parser_name")


    ### LISTS

    # lists ... lists based code
    lists_parser = subparsers.add_parser('lists', help="lists commands")
    lists_parser.set_defaults(func=libs.me_lists.me_lists, cmd='lists')

    ### DICTS

    # dicts ... dict based code
    dicts_parser = subparsers.add_parser('dicts', help="dicts commands")
    dicts_parser.set_defaults(func=libs.me_dicts.me_dicts, cmd='dicts')

    ### DECORATORS

    # decorators ... decorators based code
    decorators_parser = subparsers.add_parser('decorators', help="decorator commands")
    decorators_parser.set_defaults(func=libs.me_decorators.me_decorators, cmd='decorator')

    ### RE

    # re ... regular expressions based code
    re_parser = subparsers.add_parser('re', help="regex commands")
    re_parser.set_defaults(func=libs.me_re.me_re, cmd='re')


# import libs.me_scope
    scope_parser = subparsers.add_parser('scope', help="Scope  commands")
    scope_parser.set_defaults(func=libs.me_scope.me_scope, cmd='scope')

# import libs.me_functions
    functions_parser = subparsers.add_parser('functions', help="Function (builtin) commands")
    functions_parser.set_defaults(func=libs.me_functions.me_functions , cmd='functions')

# import libs.me_truthy
    truthy_parser = subparsers.add_parser('truthy', help="Truthy commands")
    truthy_parser.set_defaults(func=libs.me_truthy.me_truthy , cmd='truthy')

# import libs.me_iterators
    iterators_parser = subparsers.add_parser('iterators', help="Iterators commands")
    iterators_parser.set_defaults(func=libs.me_iterators.me_iterators, cmd='iterators')

# import libs.me_lambdas
    lambdas_parser = subparsers.add_parser('lambdas', help="Lambdas commands")
    lambdas_parser.set_defaults(func=libs.me_lambdas.me_lambdas , cmd='lambdas')

# import libs.me_generators
    generators_parser = subparsers.add_parser('generators', help="generators commands")
    generators_parser.set_defaults(func=libs.me_generators.me_generators , cmd='generators')

# import libs.me_tuples
    tuples_parser = subparsers.add_parser('tuples', help="tuples commands")
    tuples_parser.set_defaults(func=libs.me_tuples.me_tuples , cmd='tuples')

# import libs.me_strings
    strings_parser = subparsers.add_parser('strings', help="Strings commands")
    strings_parser.set_defaults(func=libs.me_strings.me_strings , cmd='strings')

# import libs.me_sets
    sets_parser = subparsers.add_parser('sets', help="sets commands")
    sets_parser.set_defaults(func=libs.me_sets.me_sets , cmd='sets')

# import libs.me_exceptions
    exceptions_parser = subparsers.add_parser('exceptions', help="Exceptions commands")
    exceptions_parser.set_defaults(func=libs.me_exceptions.me_exceptions , cmd='exceptions')

# import libs.me_filedir
    filedir_parser = subparsers.add_parser('filedir', help="File and Directory commands")
    filedir_parser.set_defaults(func=libs.me_filedir.me_filedir , cmd='filedir')

# import libs.me_unix
    unix_parser = subparsers.add_parser('unix', help="Unix commands")
    unix_parser.set_defaults(func=libs.me_unix.me_unix , cmd='unix')

# import libs.me_networking_IPC
    networking_parser = subparsers.add_parser('networking', help="Networking and IPC commands")
    networking_parser.set_defaults(func=libs.me_networking_IPC.me_network , cmd='networking')

# import libs.me_threading
    threading_parser = subparsers.add_parser('threading', help="Threading commands")
    threading_parser.set_defaults(func=libs.me_threading.me_threading , cmd='threading')

# import libs.me_multiprocessing
    multiprocessing_parser = subparsers.add_parser('multiprocessing', help="Multiprocessing commands")
    multiprocessing_parser.set_defaults(func=libs.me_multiprocessing.me_multiprocessing , cmd='multiprocessing')

# import libs.me_async
    async_parser = subparsers.add_parser('async', help="async commands")
    async_parser.set_defaults(func=libs.me_async.me_async, cmd='async')

# import libs.me_coroutine
    coroutine_parser = subparsers.add_parser('coroutine', help="coroutine commands")
    coroutine_parser.set_defaults(func=libs.me_coroutine.me_coroutine , cmd='coroutine')

# import libs.me_numerics
    numerics_parser = subparsers.add_parser('numerics', help="numerics commands")
    numerics_parser.set_defaults(func=libs.me_numerics.me_numerics, cmd='numerics')

# import libs.me_comparisons
    comparisons_parser = subparsers.add_parser('comparisons', help="comparison commands")
    comparisons_parser.set_defaults(func=libs.me_comparisons.me_comparisons , cmd='comparisons')

# import libs.me_compression
    compression_parser = subparsers.add_parser('compression', help="Compression commands")
    compression_parser.set_defaults(func=libs.me_compression.me_compression , cmd='compression')

# import libs.me_internet
    internet_parser = subparsers.add_parser('internet', help="Internet commands")
    internet_parser.set_defaults(func=libs.me_internet.me_internet , cmd='internet')



    ### PLAY

    # play... playground area to test new ideas quickly and without judgement... 
    play_parser = subparsers.add_parser('play', help="Play sub-command help")

    # Create sub-sub parser for play sub-commands
    play_subparser = play_parser.add_subparsers(help="Play sub-sub-command help", dest="play_parser")
    play_subparser_practice = play_subparser.add_parser('practice', help="Play Practice sub-command help")
    play_subparser_weather = play_subparser.add_parser('weather', help="Play weather sub-command help")


    # sub-command play arguments
    # example calling a sub-command with a function
    play_subparser_practice.set_defaults(func=scratchpad.practice.practice_demo, cmd='practice')

    # example calling a sub-command with a module
    play_subparser_weather.set_defaults(module='scratchpad.practice', cmd='weather')


    # play practice sub-sub commands testing
    play_subsubparser_practice = play_subparser_practice.add_subparsers(help="Play sub-sub-command help", dest="play_subparser_practice")
    play_subparser_practice_good = play_subsubparser_practice.add_parser('good', help="Play Practice good sub-command help")
    play_subparser_practice_bad = play_subsubparser_practice.add_parser('bad', help="Play Practice bad sub-command help")



    ### MODULES

    # modules ... code that is based on certain modules ( ie, requests)
    modules_parser = subparsers.add_parser('modules', help="Modules commands")
    modules_parser.set_defaults(func=libs.me_modules.me_modules, cmd='modules')

    # Create sub-sub parser for module sub-commands
    modules_subparser = modules_parser.add_subparsers(help="Modules sub commands", dest="modules_parser")

    # request module sub-command
    modules_subparser_requests = modules_subparser.add_parser('requests', help="Modules Requests Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_requests, cmd='modules.requests')

    #  datetime module sub-command
    modules_subparser_requests = modules_subparser.add_parser('datetime', help="Modules datetime Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_datetime, cmd='modules.datetime')
 
    # collections module sub-command
    modules_subparser_requests = modules_subparser.add_parser('collections', help="Modules collections Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_collections, cmd='modules.collections')
 
    # heapq  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('heapq', help="Modules heapq Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_heapq, cmd='modules.heapq')
 
    # bisect  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('bisect', help="Modules bisect Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_bisect, cmd='modules.bisect')
 
    # types  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('types', help="Modules types Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_types, cmd='modules.types')
 
    # array  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('array', help="Modules array Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_array, cmd='modules.array')
 
    # copy  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('copy', help="Modules copy Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_copy, cmd='modules.copy')
 
    # pprint  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('pprint', help="Modules pprint Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_pprint, cmd='modules.pprint')
 
    # math  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('math', help="Modules math Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_math, cmd='modules.math')
 
    # random  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('random', help="Modules random Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_random, cmd='modules.random')
 
    # statistics  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('statistics', help="Modules statistics Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_statistics, cmd='modules.statistics')
 
    # itertools  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('itertools', help="Modules itertools Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_itertools, cmd='modules.itertools')
 
    # functools  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('functools', help="Modules functools Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_functools, cmd='modules.functools')
 
    # operator  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('operator', help="Modules operator Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_operator, cmd='modules.operator')
 
    # pathlib  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('pathlib', help="Modules pathlib Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_pathlib, cmd='modules.pathlib')
 
    # os  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('os', help="Modules os Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_os, cmd='modules.os')
 
    #  glob module sub-command
    modules_subparser_requests = modules_subparser.add_parser('glob', help="Modules glob Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_glob, cmd='modules.glob')
 
    # fnmatch  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('fnmatch', help="Modules fnmatch Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_fnmatch, cmd='modules.fnmatch')
 
    # shutil  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('shutil', help="Modules shutil Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_shutil, cmd='modules.shutil')
 
    # sqlite3  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('sqlite3', help="Modules sqlite3 Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_sqlite3, cmd='modules.sqlite3')
 
    # csv  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('csv', help="Modules csv Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_csv, cmd='modules.csv')
 
    # json  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('json', help="Modules json Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_json, cmd='modules.json')
 
    # configparser  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('configparser', help="Modules configparser Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_configparser, cmd='modules.configparser')
 
    # io  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('io', help="Modules io Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_io, cmd='modules.io')
 
    # time  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('time', help="Modules time Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_time, cmd='modules.time')
 
    # errno  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('errno', help="Modules errno Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_errno, cmd='modules.errno')
 
    # curses  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('curses', help="Modules curses Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_curses, cmd='modules.curses')
 
    # ctypes  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('ctypes', help="Modules ctypes Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_ctypes, cmd='modules.ctypes')
 
    # threading  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('threading', help="Modules threading Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_threading, cmd='modules.threading')
 
    # multiprocessing  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('multiprocessing', help="Modules multiprocessing Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_multiprocessing, cmd='modules.multiprocessing')
 
    # concurrent module sub-command
    modules_subparser_requests = modules_subparser.add_parser('concurrent', help="Modules concurrent Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_concurrent, cmd='modules.concurrent')
 
    # subprocess  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('subprocess', help="Modules subprocess Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_subprocess, cmd='modules.subprocess')
 
    # sched  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('sched', help="Modules sched Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_sched, cmd='modules.sched')
 
    # queue  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('queue', help="Modules queue Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_queue, cmd='modules.queue')
 
    # _thread  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('_thread', help="Modules _thread Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules__thread, cmd='modules._thread')
 
    # asyncio  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('asyncio', help="Modules asyncio Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_asyncio, cmd='modules.asyncio')
 
    # socket  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('socket', help="Modules socket Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_socket, cmd='modules.socket')
 
    # ssl  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('ssl', help="Modules ssl Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_ssl, cmd='modules.ssl')
 
    # mmap  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('mmap', help="Modules mmap Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_mmap, cmd='modules.mmap')
 
    #  signal module sub-command
    modules_subparser_requests = modules_subparser.add_parser('signal', help="Modules signal Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_signal, cmd='modules.signal')
 
    # urllib  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('urllib', help="Modules urllib Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_urllib, cmd='modules.urllib')
 
    # http  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('http', help="Modules http Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_http, cmd='modules.http')
 
    # socketserver  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('socketserver', help="Modules socketserver Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_socketserver, cmd='modules.socketserver')
 
    #  ipaddress module sub-command
    modules_subparser_requests = modules_subparser.add_parser('ipaddress', help="Modules ipaddress Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_ipaddress, cmd='modules.ipaddress')
 
    # turtle  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('turtle', help="Modules turtle Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_turtle, cmd='modules.turtle')
 
    # cmd  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('cmd', help="Modules cmd Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_cmd, cmd='modules.cmd')
 
    # shlex  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('shlex', help="Modules shlex Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_shlex, cmd='modules.shlex')
 
    # tkinter  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('tkinter', help="Modules tkinter Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_tkinter, cmd='modules.tkinter')
 
    # typing  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('typing', help="Modules typing Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_typing, cmd='modules.typing')
 
    # pydoc  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('pydoc', help="Modules pydoc Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_pydoc, cmd='modules.pydoc')
 
    # pdb  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('pdb', help="Modules pdb Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_pdb, cmd='modules.pdb')
 
    # timeit  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('timeit', help="Modules timeit Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_timeit, cmd='modules.timeit')
 
    # sys  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('sys', help="Modules sys Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_sys, cmd='modules.sys')
 
    # sysconfig  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('sysconfig', help="Modules sysconfig Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_sysconfig, cmd='modules.sysconfig')
 
    # inspect  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('inspect', help="Modules inspect Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_inspect, cmd='modules.inspect')
 
    # importlib  module sub-command
    modules_subparser_requests = modules_subparser.add_parser('importlib', help="Modules importlib Sub Command")
    modules_subparser_requests.set_defaults(func=libs.me_modules.me_modules_importlib, cmd='modules.importlib')


    args = parser.parse_args()    

    return args
