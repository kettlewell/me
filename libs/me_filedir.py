#!/usr/bin/env python3
'''File and Directory based routines'''

"""

Nice SO answer on files / directories
https://stackoverflow.com/a/16826913

"""

import os
import sys

from pathlib import Path
import pprint as pp

import logging

logger = logging.getLogger('FILEDIR')

def me_filedir(args=None):
    logger.info("me_filedir")

    if args:
        print(vars(args))
        logger.info(vars(args))

    test_paths(args)
    test_file_name(args)


def test_paths(args):
    # TODO: create a utility function for getting the module directory
    # move these examples into the file_dir module later
    module_path = os.path.realpath(__file__)
    module_path2 = os.path.relpath(__file__)

    current_file: Path = Path(__file__).resolve()
    current_path: Path = Path(__file__).parent.resolve()
    pp.pprint(current_file)
    pp.pprint(current_path)
    
    # no external imports ( just os and sys )
    # top level project path
    PROJECT_PATH = os.path.abspath(os.path.split(sys.argv[0])[0])
    logger.info("PROJECT_PATH: " + PROJECT_PATH)

# https://stackoverflow.com/questions/247770/how-to-retrieve-a-modules-path
def test_file_name(args):
    if '__file__' in globals():
        self_name = globals()['__file__']
    elif '__file__' in locals():
        self_name = locals()['__file__']
    else:
        self_name = __name__

    logger.info("self_name 1: " + self_name)

    self_name = globals().get('__file__', locals().get('__file__', __name__))
    logger.info("self_name 2: " + self_name)
    