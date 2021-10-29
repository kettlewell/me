#!/usr/bin/env python3
'''main for me'''
"""
I have no idea what this program will be in the end

right now, it's just a playground for me

"""
import logging
import pprint as pp

#import libs.me_globals
#import libs.me_decorators
#import libs.me_lists

import libs.me_argparse
import libs.me_logging


def main():

    # get and return the args from parsing the commandline options
    me_args = libs.me_argparse.me_parse()
    libs.me_logging.start_logging(me_args.log)

    logger = logging.getLogger('MAIN')

    if me_args.verbose and me_args.log in ['debug']:
        logger.info(vars(me_args))
        logger.debug('Debug Logging initialized in main')
        logger.info('Info Logging initialized in main')
        logger.warning('Warning Logging initialized in main')
        logger.error('Error Logging initialized in main')
        logger.critical('Critical Logging initialized in main')

    # determine if there are any global settings that need to be set

    if me_args.practice:
        import scratchpad.practice as practice
        return

    # if a function was set, call it with the args object
    # that has the attributes we'd need in the call
    if hasattr(me_args, 'func'):
        me_args.func(me_args)


if __name__ == '__main__':
    main()
