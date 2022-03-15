#!/usr/bin/env python3
"""main for me
I have no idea what this program will be in the end

right now, it's just a playground for me

"""
import importlib

import logging

# import libs.me_globals
import libs.me_decorators
import libs.me_argparse
import libs.me_logging

# debugging - leaving in for future reference
# print(libs.me_argparse.__dict__)


@libs.me_decorators.timer
def main():

    # get and return the args from parsing the commandline options
    me_args_parser = libs.me_argparse.me_parse()
    me_args = me_args_parser.parse_args()

    libs.me_logging.start_logging(me_args.log)

    logger = logging.getLogger("MAIN")
    logger.info("main started")

    if me_args.verbose and me_args.log == "debug":
        logger.info(vars(me_args))  # noqa: WPS421
        logger.debug("Debug Logging initialized in main")
        logger.info("Info Logging initialized in main")
        logger.warning(
            "Warning Logging initialized in main"
        )
        logger.error("Error Logging initialized in main")
        logger.critical(
            "Critical Logging initialized in main"
        )

    # determine if there are any global settings that need to be set

    if me_args.practice:
        logger.debug("has practice args")
        import scratchpad.practice as practice  # noqa: F401 WPS433

        return

    #    if hasattr(me_args, 'sub_parser_name') and me_args.sub_parser_name == 'play':
    if getattr(me_args, "sub_parser_name"):

        logger.debug(
            "sub_parser_name: " + me_args.sub_parser_name
        )  # noqa: WPS336

        # check if there's a module attribute:
        if hasattr(me_args, "module"):
            logger.debug(
                "module: " + me_args.module
            )  # noqa: WPS336
            try:  # noqa: WPS229
                spec = importlib.util.find_spec(
                    me_args.module
                )
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
            except ImportError as err:
                logger.info(
                    "Import Module Error: " + err
                )  # noqa: WPS336

        # if a function was set, call it with the args object
        # that has the attributes we'd need in the call
        if hasattr(me_args, "func"):
            logger.debug("we have a fun in args")
            me_args.func(me_args)

    # save for rainy day
    # me_args_parser.print_help()

    logger.debug("END of MAIN")


if __name__ == "__main__":
    main()
