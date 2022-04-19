#!/usr/bin/env python3
"""Strings based routines"""
import os
import logging
import me.libs.decorators

import string

logger = logging.getLogger("STRINGS")


def strings(args=None):
    logger.debug("strings")

    system_string_funcs()

    lc_alphabet()
    uc_alphabet()
    str_digits()
    str_with_digits = "ABC123DEF456GHI789JKL"
    remove_digits(str_with_digits)

    s1 = "thistt"
    s2 = "histt"
    anagram(s1, s2)

    rewrite_immutable()
    longstrings()
    quote_strings()
    format_strings()
    slice_strings()

    lst = [1, 2, 3, 4, 5, 6, 7]
    join_objects_as_strings(lst)


def system_string_funcs():
    str_capitalize()
    str_casefold()
    str_center()
    str_count()
    str_encode()
    str_endswith()
    str_expandtabs()
    str_find()
    str_format()
    str_format_map()
    str_index()
    str_isalnum()
    str_isalpha()
    str_isascii()
    str_isdecimal()
    str_isdigit()
    str_isidentifier()
    str_islower()
    str_isnumeric()
    str_isprintable()
    str_isspace()
    str_istitle()
    str_isupper()
    str_join()
    str_ljust()
    str_lower()
    str_lstrip()
    str_maketrans()
    str_partition()
    str_removeprefix()
    str_removesuffix()
    str_replace()
    str_rfind()
    str_rindex()
    str_rjust()
    str_rpartition()
    str_rsplit()
    str_rstrip()
    str_split()
    str_splitlines()
    str_startswith()
    str_strip()
    str_swapcase()
    str_title()
    str_translate()
    str_upper()
    str_zfill()


def str_capitalize():
    pass


def str_casefold():
    pass


def str_center():
    pass


def str_count():
    pass


def str_encode():
    pass


def str_endswith():
    pass


def str_expandtabs():
    pass


def str_find():
    pass


def str_format():
    pass


def str_format_map():
    pass


def str_index():
    pass


def str_isalnum():
    pass


def str_isalpha():
    pass


def str_isascii():
    pass


def str_isdecimal():
    pass


def str_isdigit():
    pass


def str_isidentifier():
    pass


def str_islower():
    pass


def str_isnumeric():
    pass


def str_isprintable():
    pass


def str_isspace():
    pass


def str_istitle():
    pass


def str_isupper():
    pass


def str_join():
    pass


def str_ljust():
    pass


def str_lower():
    pass


def str_lstrip():
    pass


def str_maketrans():
    pass


def str_partition():
    pass


def str_removeprefix():
    pass


def str_removesuffix():
    pass


def str_replace():
    quote = "to be or not to be"
    logger.info(quote.replace("be", "me"))
    logger.info(quote)


def str_rfind():
    pass


def str_rindex():
    pass


def str_rjust():
    pass


def str_rpartition():
    pass


def str_rsplit():
    pass


def str_rstrip():
    pass


def str_split():
    pass


def str_splitlines():
    pass


def str_startswith():
    pass


def str_strip():
    pass


def str_swapcase():
    pass


def str_title():
    pass


def str_translate():
    pass


def str_upper():
    pass


def str_zfill():
    pass


def longstrings():
    password = "secr" "et" " " "agent " "man" "!"

    logger.info(password)
    longstring = """
WOW
      0 0
        ---
"""

    logger.info(longstring)


# we can't really re-write a string
# but we can use recipes to copy the string back to itself
def rewrite_immutable():
    title = "Recipe 5: some immutable string, with, punctuation"

    colon_position = title.index(":")

    logger.info("colon_position: %s", colon_position)

    pre_colon, post_colon = title[:colon_position], title[colon_position + 1 :]

    logger.info("pre_colon: %s", pre_colon)
    logger.info("post_colon: %s", post_colon)

    pre_colon, middle, post_colon = title.partition(":")
    logger.info("pre_colon: %s", pre_colon)
    logger.info("middle: %s", middle)

    logger.info("post_colon: %s", post_colon)

    print()


def anagram(s1, s2):
    from collections import Counter

    logger.info(Counter(s1))
    logger.info(Counter(s2))

    logger.info("anagram") if Counter(s1) == Counter(s2) else logger.info("NOT anagram")

    print()


def remove_digits(str):
    res = "".join(list(filter(lambda x: x.isalpha(), str)))
    logger.info("str with no digits: %s", res)
    print()


def lc_alphabet():
    logger.info(string.ascii_lowercase)


def uc_alphabet():
    logger.info(string.ascii_uppercase)


def str_digits():
    logger.info(string.digits)


def from_practice(args):
    logger.info("hello as a stutter :  " + stutter("hello"))

    # search_help('builtins')
    # logger.info(help(builtins.dict))

    # somestring = "1\n\n,2,\n3,4,5,6\n\n\n\n"
    # sstring = somestring.split(',')
    # logger.info(type(sstring))
    # logger.info(sstring)

    # somestring = '1,2,3,4,5,6\n\n\n\n'
    # sstring = somestring.splitlines()
    # logger.info(type(sstring))
    # logger.info(sstring)

    # sstring = somestring
    # sstring = somestring.strip('\n')
    # logger.info(type(sstring))
    # logger.info(sstring)


def join_objects_as_strings(lst):
    # Join objects as strings
    # https://blog.finxter.com/how-to-use-pythons-join-function-on-a-list-of-objects-rather-than-strings/

    join_method_1(lst)
    join_method_2(lst)
    join_method_3(lst)
    join_method_4(lst)
    join_method_5(lst)
    join_method_6(lst)


@me.libs.decorators.timer
def join_method_1(lst):
    # Method 1 - list comprehension with join
    logger.info("".join([str(x) for x in lst]))
    # ''.join([str(x) for x in lst])

    # 0124


@me.libs.decorators.timer
def join_method_2(lst):
    # Method 2 - generator expression
    logger.info("".join(str(x) for x in lst))
    # ''.join(str(x) for x in lst)

    # 0124


@me.libs.decorators.timer
def join_method_3(lst):
    # todo: this doesn't work with int types... so exclude it
    #       this is because there is no int.val attr.
    return
    # Method 3 - generator expression with custom string repr
    logger.info("".join(str(x.val) for x in lst))
    # ''.join(str(x.val) for x in lst)
    # 0124


@me.libs.decorators.timer
def join_method_4(lst):
    # Method 4 - lambda + str
    logger.info("".join(map(lambda x: str(x), lst)))
    # ''.join(map(lambda x: str(x), lst))
    # 0124


@me.libs.decorators.timer
def join_method_5(lst):
    # Method 5 - map + str
    logger.info("".join(map(str, lst)))
    # ''.join(map(str, lst))
    # 0124


@me.libs.decorators.timer
def join_method_6(lst):
    # Method 6 - naive loop
    s = ""
    for x in lst:
        s += str(x)
    logger.info(s)
    # 0124


class Obj:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)


# lst = [Obj(0), Obj(1), Obj(2), Obj(4)]

lst = [Obj(x) for x in range(0, 10)]


# STRING
# create a stuttering type string response
def stutter(word):
    return word[:2] + "..." + word[:2] + "..." + word + "?"


def search_help(keyword):
    os.system("pydoc -k {}".format(keyword))


def quote_strings():

    weather = 'It\'s "kind of" Sunny'
    logger.info(weather)


def format_strings():

    # formatted strings
    name = "johnny"
    age = 55

    print("Hi " + name + " you are " + str(age) + " years old")
    logger.info("Hi " + name + " you are " + str(age) + " years old")

    print(f"hi {name}. You are {age} years old")
    logger.info(f"hi {name}. You are {age} years old")

    # print('hi {age}. You are {name} years old'.format(name="blah", age=10))

    # print(f'hi {age}. You are {name} years old')


def slice_strings():
    selfish = "0123456789"
    # count evens backwards
    logger.info(selfish[-2::-2])
