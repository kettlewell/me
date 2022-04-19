#!/usr/bin/env python3

import os
import sys
import inspect
from pathlib import Path

# We need to include the root directory in sys.path to ensure that we can
# find everything we need when running in the standalone runtime.
# string object
ROOT = os.path.dirname(os.path.realpath(__file__))
if sys.path[0] != ROOT:
    sys.path.insert(0, ROOT)

# Path object
PROJECT_PATH = Path(ROOT)

# TODO: create string object version of the below functions ( maybe? )
# ALT: instead of inspect.stack, try sys._current_frames()
#      https://stackoverflow.com/a/5071539


def curr_file_path():
    """
    # get the calling modules file path
    # using the inspect module to look at the calling stack frame
    """
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])
    return Path(mod.__file__).resolve()


def curr_dir_path():
    """
    # get the calling modules dir path
    # using the inspect module to look at the calling stack frame
    """
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])
    return Path(mod.__file__).parent.resolve()
