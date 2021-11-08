#!/usr/bin/env python3
'''Numerics based routines'''

import logging

from math import pi
import libs.me_truthy as truthy


logger = logging.getLogger('NUMERICS')

def me_numerics(args=None):
    logger.info("me_numerics")

    if args:
        print(vars(args))
        logger.info(vars(args))


    logger.info(tri_area(10,10))
    logger.info(min_to_secs(3))
    logger.info(cubes(10))
    logger.info(remainder(1,3))
    logger.info(sum_polygon(6))
    logger.info(dis(1500,50))
    logger.info(dis(89,20))
    logger.info(dis(100,75))
    logger.info(is_curzon(5))
    logger.info(is_curzon(10))
    logger.info(is_curzon(14))
    logger.info(rad_to_deg(50))


# NUMERICS
# area of a triangle
def tri_area(base,height):
    return (base * height) / 2

# NUMERICS
# minutes to seconds
def min_to_secs(min):
    return (min * 60)

# NUMBERICS
# cube of a value
def cubes(a):
    return a**3

# NUMERICS
# remainder of division
def remainder(divisor,quotient):
    return (divisor%quotient)

# NUMBERICS
# Angles of a polygon ( verifiable ? )
def sum_polygon(sides):
    return (sides - 2) * 180


# NUMERICS
# convert years to days
def calc_age(years):
    return years * 365



# Numerics 
# Builtin
# give a price discount, rounded down
def dis(price, discount):
    return round(price - (price * discount/100), 2)

# Numerics
# IMPORT: MATH
# radian to degreee conversion
def rad_to_deg(rad):
    return round(rad * 180/pi, 1)


# Numerics
# A number N is said to be a Curzon Number if 2N + 1 is divisible by 2*N + 1.
# check if a number is a curzon number
def is_curzon(x):
    if (2**x + 1) % (2 * x +1):
        return truthy.bool_to_string2(False)
    else:
        return truthy.bool_to_string2(True)
