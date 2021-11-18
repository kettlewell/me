#!/usr/bin/env python3
""" utility functions"""

import logging
logger = logging.getLogger(__name__)



def log_values(expected,actual):
    if cmp_values(expected,actual):
        logger.info("[OK] [ACTUAL] : " + str(actual) + "  [EXPECTED] : " + str(expected))
    else:
        logger.error("[ERROR] [ACTUAL] : " + str(actual) + "  [EXPECTED] : " + str(expected))

def cmp_values(expected,actual):

    # intialize types not same
    sameType = True

    # string compare
    if isinstance(expected,str) and isinstance(actual,str):
        pass
        #logger.info("expected value is STRING")
        
    # int compare
    elif isinstance(expected,int) and isinstance(actual,int):
        pass
        #logger.info("expected value is INT")

    # dict compare
    elif isinstance(expected,dict) and isinstance(actual,dict):
        pass
        #logger.info("expected value is DICT")

    # list compare
    elif isinstance(expected,list) and isinstance(actual,list):
        pass
        #logger.info("expected value is LIST")

    # tuple compare
    elif isinstance(expected,tuple) and isinstance(actual,tuple):
        pass
        #logger.info("expected value is TUPLE")

    # float compare
    elif isinstance(expected,float) and isinstance(actual,float):
        pass
        #logger.info("expected value is FLOAT")

    # bool compare
    elif isinstance(expected,bool) and isinstance(actual,bool):
        pass
        #logger.info("expected value is BOOL")
    
    # unknown
    else:
        logger.error("expected type is unknown or not same")
        sameType = False

        
    if sameType:
        return actual == expected
    else:
        return False    
   