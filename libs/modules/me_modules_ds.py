#!/usr/bin/env python3
"""Lists based routines"""

import logging
import re
import numpy as np
import pandas as pd


from libs.me_utilities import log_values as lv
from libs.me_utilities import cmp_values as cv

logger = logging.getLogger("DS")


def me_modules_ds(args=None):
    logger.debug("me_modules_ds")
