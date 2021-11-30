#!/usr/bin/env python3
'''Truthy based routines'''

import logging

logger = logging.getLogger('TRUTHY')

def me_truthy(args=None):
    logger.info("me_truthy")

    if args:
        print(vars(args))
        logger.info(vars(args))




# TRUTHY
# Truthy to String
def bool_to_string(truth):
    if truth: 
        return "True" 
    else: 
        return "False"

# TRUTHY
# Truthy to String 
# seems like it's missing a str() conversion
def bool_to_string2(truth):
    return (bool(truth))

#in_arr=[100,11,12]
#print(get_first_value(in_arr))

#print(calc_age(20))

#print(bool_to_string(True))
#print(bool_to_string(False))
#print(bool_to_string(1))
#print(bool_to_string(0))

#print(bool_to_string2(True))
#print(bool_to_string2(False))
#print(bool_to_string2(1))
#print(bool_to_string2(0))
