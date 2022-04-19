#!/usr/bin/env python3
"""This is a playground for... me

If you happen to stop by, please note that it's completely unorganized,
free flowing, and just a place for me to jot down learnings and play
around with code for me personally, and not intended to be used by
any audiences outside of myself
"""
from config import PROJECT_PATH
import importlib

import logging

# import libs.globals
import libs.decorators
import libs.argparse
import libs.logging

# debugging - leaving in for future reference
# print(libs.argparse.__dict__)


@libs.decorators.timer
def main():

    # get and return the args from parsing the commandline options
    args_parser = libs.argparse.parse()
    args = args_parser.parse_args()

    libs.logging.start_logging(args.log)

    logger = logging.getLogger("MAIN")
    logger.info(f"main started in {PROJECT_PATH} ")

    if args.verbose and args.log == "debug":
        logger.info(vars(args))  # noqa: WPS421
        logger.debug("Debug Logging initialized in main")
        logger.info("Info Logging initialized in main")
        logger.warning("Warning Logging initialized in main")
        logger.error("Error Logging initialized in main")
        logger.critical("Critical Logging initialized in main")

    # determine if there are any global settings that need to be set

    if args.practice:
        logger.debug("has practice args")
        import scratchpad.practice as practice  # noqa: F401 WPS433

        return

    #    if hasattr(args, 'sub_parser_name') and args.sub_parser_name == 'play':
    if getattr(args, "sub_parser_name"):

        logger.debug("sub_parser_name: " + args.sub_parser_name)  # noqa: WPS336

        # check if there's a module attribute:
        if hasattr(args, "module"):
            logger.debug("module: " + args.module)  # noqa: WPS336
            try:  # noqa: WPS229
                spec = importlib.util.find_spec(args.module)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
            except ImportError as err:
                logger.info("Import Module Error: " + err)  # noqa: WPS336

        # if a function was set, call it with the args object
        # that has the attributes we'd need in the call
        if hasattr(args, "func"):
            logger.debug("we have a fun in args")
            args.func(args)

    # save for rainy day
    # args_parser.print_help()

    logger.debug("END of MAIN")


if __name__ == "__main__":
    main()
