#!/usr/bin/env python3
'''Argument parsing with sub parsers'''

"""
The general idea will be to create sub parsers for testing various things

main [options] [list|dict|generator|collection] [sub-commands]


"""
import argparse
import libs.me_lists
import scratchpad.practice

def me_parse():
    parser = argparse.ArgumentParser(description='Demo program that highlights a lot of functionality of the python programming language.')

    # general / global arguments
    parser.add_argument('--practice', '-p', help="practice runs",  action='store_true')
    parser.add_argument('--verbose', '-v',  help="verbose levels", action='count', default=0)
    parser.add_argument('--log', '-l',      help="log level",      choices=['debug', 'info', 'warning', 'error', 'critical'], default='info')
    

    # create first level sub-parser
    subparsers = parser.add_subparsers(help="Available Subcommands", description="Sub commands for executing specific code blocks", dest="sub_parser_name")

    # Create sub-parser first args
    parser_a = subparsers.add_parser('a', help="A sub-command help")
    parser_b = subparsers.add_parser('b', help="B sub-command help")
    ext_parser = subparsers.add_parser('ext', help="External sub-command help")


    # Create sub-sub parser for A sub-commands
    subparser_a = parser_a.add_subparsers(help="A sub-command help")
    parser_a_a = subparser_a.add_parser('a', help="A A sub-command help")
    parser_a_b = subparser_a.add_parser('b', help="A B sub-command help")

    # Create sub-sub parser for B sub-commands
    subparser_b = parser_b.add_subparsers(help="B sub-command help")
    parser_b_a = subparser_b.add_parser('a', help="B A sub-command help")
    parser_b_b = subparser_b.add_parser('b', help="B B sub-command help")

    # Create sub-sub parser for B sub-commands
    ext_subparser = ext_parser.add_subparsers(help="External sub-sub-command help")
    ext_subparser_practice = ext_subparser.add_parser('practice', help="External Practice sub-command help")
    ext_subparser_weather = ext_subparser.add_parser('weather', help="External weather sub-command help")

    # Sub-command A arguments
    parser_a.add_argument('--bar', type=int, help="A --BAR help")
    parser_a.set_defaults(func=libs.me_lists.me_lists)

    # sub-command B arguments
    parser_b.add_argument('--baz', type=int, help="B --BAZ help")
    parser_b.set_defaults(func=libs.me_lists.me_lists)

    # sub-command external arguments
    ext_subparser_practice.set_defaults(func=scratchpad.practice.practice_demo, cmd='practice')
    ext_subparser_weather.set_defaults(module='scratchpad.practice', cmd='weather')

    # sub-commands of A A commands
    parser_a_a.add_argument('--aa', type=int, help="A A aa placeholder")

    # sub-commands of A B commands
    parser_a_b.add_argument('--ab', type=int, help="A B ab placeholder")

    # sub-commands of B A commands
    parser_b_a.add_argument('--ba', type=int, help="B A ba placeholder")

    # sub-commands of B B commands
    parser_b_b.add_argument('--bb', type=int, help="B B bb placeholder")


    args = parser.parse_args()

    
    return args

