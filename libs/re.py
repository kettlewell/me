#!/usr/bin/env python3
"""
Regex based routines
https://docs.python.org/3/library/re.html

"""

import logging
import re
import random

logger = logging.getLogger("RE")


def re_module(args=None):
    logger.info("re")

    if args:
        print(vars(args))
        logger.info(vars(args))

    re_list_functions()

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


def re_list_functions():
    import libs.utilities

    logger.debug("re_list_functions")

    libs.utilities.obj_functions(re, gen_func=True)


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
    logger.info("re.VERBOSE is a way to create explicit and commented re.compile statements")
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

    text = "He was carefully disguised but captured quickly by police."

    ly = re.findall(r"\w+ly\b", text)

    logger.info(type(ly))
    logger.info(ly)

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

    text = "He was carefully disguised but captured quickly by police."
    p = re.compile(r"\w+ly\b")
    matches = p.finditer(text)
    for m in matches:
        logger.info("{:>03d} - {:>03d}: {}".format(m.start(), m.end(), m.group(0)))

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

    str = "abcdefghijk"
    p = re.compile("((a(((b)c)def)(g(h)i)j)k)")
    m = p.match(str)
    if m:
        logger.info(m)
        logger.info(m.groups())
        logger.info(m.group(0))
        logger.info(m.group(1))
        logger.info(m.group(2))
        logger.info(m.group(3))
        logger.info(m.group(4))
        logger.info(m.group(5))
        logger.info(m.group(6))
        logger.info(m.group(7))

    print()
    m1 = re.match("([abc])+", "abcd")
    m2 = re.match("(?:[abc])+", "abcd")
    m3 = re.match("(([abc])+)", "abcd")
    m4 = re.match("(?P<letter>[abc])+", "abcd")
    m5 = re.match("(?P<letters>(?P<letter>[abc])+)", "abcd")

    logger.info(m1)
    logger.info(m1.groups())
    logger.info(m1.group(0))
    logger.info(m1.group(1))
    print()

    logger.info(m2)
    logger.info(m2.groups())
    logger.info(m2.group(0))
    # logger.info(m2.group(1))
    print()

    logger.info(m3)
    logger.info(m3.groups())
    logger.info(m3.group(0))
    logger.info(m3.group(1))

    logger.info(m4)
    logger.info(m4.groupdict())
    print()
    logger.info(m5)
    logger.info(m5.string)
    logger.info(m5.re)
    logger.info(m5.groupdict()["letter"])
    logger.info(m5.groupdict()["letters"])

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

    p = re.compile(r"\b(\w+)\s+\1\b")
    g = p.search("Paris in the the spring").group()
    gs = p.search("Paris in the the spring").groups()
    logger.info(g)
    logger.info(gs)
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

    text = """Ross McFluff: 834.345.1254 155 Elm Street
    Ronald Heathmore: 892.345.3428 436 Finley Avenue
    Frank Burger: 925.541.7625 662 South Dogwood Way
    Heather Albrecht: 548.326.4584 919 Park Place"""

    entries = re.split("\n+", text)
    logger.info(type(entries))
    logger.info(entries)

    entries = [re.sub(r"^\s+", "", entry) for entry in entries]
    print()

    [logger.info(re.split(":? ", entry, 3)) for entry in entries]
    # logger.info(entries_3)

    print()


def module_re_sre_compile():
    pass


def module_re_sre_parse():
    pass


def module_re_sub():
    logger.info("module_re_sub")

    def repl(m):
        inner_word = list(m.group(2))
        random.shuffle(inner_word)
        return m.group(1) + "".join(inner_word) + m.group(3)

    text = "Professor Abdolmalek, please report your absences promptly."

    response = re.sub(r"(\w)(\w+)(\w)", repl, text)
    logger.info(response)
    response = re.sub(r"(\w)(\w+)(\w)", repl, text)
    logger.info(response)

    print()


def module_re_subn():
    pass


def module_re_template():
    pass
