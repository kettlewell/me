#!/usr/bin/env python3
'''main for me'''
"""
I have no idea what this program will be in the end

right now, it's just a playground for me

"""
import importlib

import logging
import pprint as pp

#import libs.me_globals
import libs.me_decorators
import libs.me_argparse
import libs.me_logging

# debugging
#print(libs.me_argparse.__dict__)

@libs.me_decorators.timer
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
        logger.debug('has practice args')
        import scratchpad.practice as practice
        return

#    if hasattr(me_args, 'sub_parser_name') and me_args.sub_parser_name == 'play':
    if hasattr(me_args, 'sub_parser_name'):
        logger.debug('sub_parser_name: ' + me_args.sub_parser_name)
        
        # check if there's a module attribute:
        if hasattr(me_args, 'modules'):
            logger.debug('module: ' + me_args.module )
            try:
                spec = importlib.util.find_spec(me_args.module)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
            except ImportError as err:
                logger.info('Import Module Error: ' + err)
    
        # if a function was set, call it with the args object
        # that has the attributes we'd need in the call
        if hasattr(me_args, 'func'):
            logger.debug('we have a fun in args')
            me_args.func(me_args)

    logger.debug('END of MAIN')

if __name__ == '__main__':
    main()
