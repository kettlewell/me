#!/usr/bin/env python3
"""
Regex based routines
https://docs.python.org/3/library/re.html

"""

import logging
import re

logger = logging.getLogger("RE")


def me_modules_re(args=None):
    logger.info("me_re")

    if args:
        print(vars(args))
        logger.info(vars(args))

    me_re_list_functions()

    module_re_A()
    module_re_ASCII()
    module_re_DEBUG()
    module_re_DOTALL()
    module_re_I()
    module_re_IGNORECASE()
    module_re_L()
    module_re_LOCALE()
    module_re_M()
    module_re_MULTILINE()
    module_re_RegexFlag()
    module_re_S()
    module_re_Scanner()
    module_re_T()
    module_re_TEMPLATE()
    module_re_U()
    module_re_UNICODE()
    module_re_VERBOSE()
    module_re_X()
    module_re_compile()
    module_re_copyreg()
    module_re_enum()
    module_re_error()
    module_re_escape()
    module_re_findall()
    module_re_finditer()
    module_re_fullmatch()
    module_re_functools()
    module_re_match()
    module_re_purge()
    module_re_search()
    module_re_split()
    module_re_sre_compile()
    module_re_sre_parse()
    module_re_sub()
    module_re_subn()
    module_re_template()


def matchme(regex, str):
    # print(str)
    m = regex.search(str)
    if m:
        msg = "we have a match"
    else:
        msg = "sorry, no match"
    logger.info("{0:<15s} : {1:<30}".format(msg, str))

    s = regex.split(str)
    logger.info(s)

    if m:
        logger.info("{}:{}\n".format(m.span(), s))
    else:
        logger.info("{}\n".format(s))


def me_re_list_functions():
    import libs.me_utilities

    logger.debug("me_re_list_functions")

    libs.me_utilities.obj_functions(re, gen_func=True)


def module_re_A():
    # regex flag for ascii
    module_re_ASCII()


def module_re_ASCII():
    # regex flag for ascii
    pass


def module_re_DEBUG():
    # regex flag for debugging re.compile()
    pass


def module_re_DOTALL():
    pass


def module_re_I():
    pass


def module_re_IGNORECASE():
    pass


def module_re_L():
    pass


def module_re_LOCALE():
    pass


def module_re_M():
    pass


def module_re_MULTILINE():
    pass


def module_re_RegexFlag():
    pass


def module_re_S():
    pass


def module_re_Scanner():
    pass


def module_re_T():
    pass


def module_re_TEMPLATE():
    pass


def module_re_U():
    logger.info("module_re_U")

    p = re.compile("ab*", re.U)
    logger.info(p)


def module_re_UNICODE():
    logger.info("module_re_UNICODE")

    p = re.compile("ab*", re.UNICODE)
    logger.info(p)


def module_re_VERBOSE():
    logger.info("module_re_VERBOSE")

    charref = re.compile(
        r"""
    (
    &[#]                # Start of a numeric entity reference
    (
        0[0-7]+         # Octal form
    | [0-9]+          # Decimal form
    | x[0-9a-fA-F]+   # Hexadecimal form
    )
    ;                   # Trailing semicolon
    )
    """,
        re.VERBOSE,
    )

    logger.info(charref)
    matchstr = "&#123; or maybe &#007; or maybe &#x004a;"
    fa = charref.findall(matchstr)
    for f in fa:
        logger.info(f[0])
    print()


def module_re_X():
    module_re_VERBOSE()


def module_re_compile():
    logger.info("module_re_compile")

    p = re.compile("ab*", re.IGNORECASE)
    logger.info(p)

    p = re.compile("ab*")
    logger.info(p)

    print()


def module_re_copyreg():
    pass


def module_re_enum():
    pass


def module_re_error():
    pass


def module_re_escape():
    pass


def module_re_findall():
    """
    Find all substrings where the RE matches, and returns them as a list.
    """
    logger.info("module_re_findall")
    logger.info("Find all substrings where the RE matches, and returns them as a list.")
    print()

    p = re.compile(r"\d+")
    fa = p.findall("12 drummers drumming, 11 pipers piping, 10 lords a-leaping")
    logger.info(fa)

    print()


def module_re_finditer():
    """
    Find all substrings where the RE matches, and returns them as an iterator.
    """
    logger.info("module_re_finditer")
    logger.info("Find all substrings where the RE matches, and returns them as an iterator.")
    print()

    p = re.compile(r"\d+")
    fi = p.finditer("12 drummers drumming, 11 pipers piping, 10 lords a-leaping")
    logger.info(fi)
    logger.info(type(fi))

    for match in fi:
        logger.info(type(match))
        logger.info(match.group())
        logger.info(match.span())

    print()


def module_re_fullmatch():
    pass


def module_re_functools():
    pass


def module_re_match():
    """
    Determine if the RE matches at the beginning of the string.
    """
    logger.info("module_re_match")
    logger.info("Determine if the RE matches at the BEGINNING of the string.")

    regex = re.compile(r"abc.*123")

    str1 = "ABCabcwhoami123DEF"
    str2 = "abcwhoami123456"
    str3 = "1abcwhoami123"
    str4 = "abc123whoami123"
    str5 = "abc123"

    matchme(regex, str1)
    matchme(regex, str2)
    matchme(regex, str3)
    matchme(regex, str4)
    matchme(regex, str5)

    print()

    p = re.compile("[a-z]+")
    logger.info(p)
    print()

    logger.info(p.match(""))
    print()

    m = p.match("tempo")
    logger.info(m)

    logger.info(m.group())
    logger.info(m.start())
    logger.info(m.end())
    logger.info(m.span())

    print()


def module_re_purge():
    pass


def module_re_search():
    """
    Scan through a string, looking for any location where this RE matches.
    """
    logger.info("module_re_search")
    logger.info("Scan through a string, looking for any location where this RE matches.")
    print()

    p = re.compile("[a-z]+")
    logger.info(p)
    print()
    logger.info(p.match("::: message"))
    m = p.search("::: message")
    logger.info(m)
    logger.info(m.group())
    logger.info(m.start())
    logger.info(m.end())
    logger.info(m.span())

    print()


def module_re_split():
    logger.info("module_re_split")

    p1 = re.compile(r"\W+")
    p2 = re.compile(r"(\W+)")

    splitstr = "This...is a semi-long test of the something system"
    p1_res = p1.split(splitstr)
    p2_res = p2.split(splitstr)

    logger.info(type(p1_res))
    logger.info(type(p2_res))

    logger.info(p1_res)
    logger.info(p2_res)

    print()


def module_re_sre_compile():
    pass


def module_re_sre_parse():
    pass


def module_re_sub():
    pass


def module_re_subn():
    pass


def module_re_template():
    pass
