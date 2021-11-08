#!/usr/bin/env python3
'''Argument parsing with sub parsers'''

"""
The general idea will be to create sub parsers for testing various things

main [options] [list|dict|generator|collection] [sub-commands]

original outline consideration: https://docs.python.org/3/library/index.html


Completed:


In Progress:


Stubbed in:
lists
dicts

TODO: 
numerics
scope
functions ( built-in )
truthy
comparisons
iterators
tuples
strings
sets
exceptions
re
file_dir
compression
threading
multiprocessing
async
coroutine
networking_IPC
email
html_xml
internet
multimedia
internationalization
typing
pydoc
testing
debugging
profiling
python runtime
imports
unix

modules:

datetime
collections
heapq
bisect
types
array
copy
pprint
math
random
statistics
itertools
functools
operator
pathlib
os
glob
fnmatch
shutil
sqlite3
csv
json
configparser
io
time
argparse
logging
errno
curses
ctypes
threading
multiprocessing
concurrent
subprocess
sched
queue
_thread
asyncio
socket
ssl
mmap
signal
urllib
requests
http
socketserver
ipaddress
turtle
cmd ?
shlex
tkinter
typing
pydoc
pdb
timeit
sys
sysconfig
inspect
importlib



"""
import argparse
import libs.me_lists
import libs.me_dicts

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


    ### MODULES

    # modules ... code that is based on certain modules ( ie, requests)
    modules_parser = subparsers.add_parser('modules', help="Modules sub-command help")

    # Create sub-sub parser for module sub-commands
    modules_subparser = modules_parser.add_subparsers(help="Modules sub commands", dest="modules_parser")
    modules_subparser_requests = modules_subparser.add_parser('requests', help="Modules Requests Sub Command")


    ### COLLECTIONS 

    # collections ... collections based code
    collections_parser = subparsers.add_parser('collections', help="collections sub-command help")

    # Create sub-sub parser for collections sub-commands
    collections_subparser = collections_parser.add_subparsers(help="Collections sub commands", dest="module_parser")
    collections_subparser_lists = collections_subparser.add_parser('lists', help="Collection Lists Sub Command")
    collections_subparser_dicts = collections_subparser.add_parser('dicts', help="Collection Lists Sub Command")


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



    args = parser.parse_args()    
    return args

