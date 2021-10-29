#!/usr/bin/env python3
'''logging initialization and wrappers'''

import logging

def start_logging(loglvl='info'):
    #logging.basicConfig(level=logging.INFO)
    logging.basicConfig(format='[ %(levelname)-8s ] [ %(name)s ] [ %(asctime)-22s ]  %(message)s', level=loglvl.upper(),datefmt='%m/%d/%Y %I:%M:%S %p')