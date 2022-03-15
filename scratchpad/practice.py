#!/usr/bin/env python3

__name__ = "practice"  # noqa: WPS125
# import functools
# from functools import cache, reduce
from functools import lru_cache

import math

# import struct

# for md5sum
import hashlib

# import simpleaudio
from itertools import repeat, chain

import logging
import statistics
import pprint as pp
import random
from typing import Tuple
from datetime import date

from collections import deque

# import json

import time

from functools import wraps

from datetime import datetime
import pytz

# import re
import pandas as pd
import numpy as np

import libs.me_decorators as me_decorators  # noqa: WPS301
from libs.me_utilities import obj_functions

logger = logging.getLogger("PRACTICE")
logger.info("Importing practice.py")

# noqa: WPS462
"""  # noqa:  WPS428
    Builtin Types List:
    str
    int
    float
    complex
    list
    tuple
    range
    dict
    set
    frozenset
    bool
    bytes
    bytearray
    memoryview
"""
str_type = str()  # noqa: WPS351
int_type = int()  # noqa: WPS351
float_type = float(1.0)  # noqa: WPS351
complex_type = complex()  # noqa: WPS351
lst_type = []
tuple_type = ()
range_type = range(0)
dict_type = {}
set_type = set()
frozenset_type = frozenset()
bool_type = bool()  # noqa: WPS351
bytes_type = bytes()  # noqa: WPS351
bytearray_type = bytearray()
memoryview_type = memoryview(bytearray_type)

#    obj_functions(str_type, gen_func=True)
#    obj_functions(int_type)
#    obj_functions(float_type)

#    obj_functions(complex_type)
#    obj_functions(lst_type)
#    obj_functions(tuple_type)
#    obj_functions(range_type)
#    obj_functions(dict_type)
#    obj_functions(set_type)
#    obj_functions(frozenset_type)
#    obj_functions(bool_type)
#    obj_functions(bytes_type)
#    obj_functions(bytearray_type)
#    obj_functions(memoryview_type)


# print(int(str(100)))


## BOOL
is_cool = False
is_cool = True

# print(bool(None))


## STRINGS
status = "it's complicated"

# print(status)

## NUMERICS
age = 50
birth_year = int("1986")
age = 2019 - birth_year

# print(age)
# print( "blah" + 6)

## LISTS
li = [1, 2, 3, 4, 5, 6]
li2 = ["a", "b", "c"]
li3 = [1, 2, "a", True, False]
# pp.pprint(li[7])


cart = ["laptop", "notbook", "sunglasses", "toys", "grapes"]
new_cart0 = cart
new_cart1 = cart.copy()

# new_cart0[0] = 'blah'
# new_cart1[0] = 'blahblah'

# pp.pprint(cart)
# pp.pprint(new_cart0)
# pp.pprint(new_cart1)

# noqa: WPS462
"""  # noqa:  WPS428
if new_cart0 is cart:
    print("cart0 is the same object")
else:
    print("cart0 is a different object")

if new_cart1 is cart:
    print("cart1 is the same object")
else:
    print("cart1 is a different object")


if new_cart0 == cart:
    print("cart0 is the same list contents")
else:
    print("cart0 is differnt list contents")

if new_cart1 == cart:
    print("cart1 is the same list contents")
else:
    print("cart1 is a different list contents")
 """

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # noqa: WPS221

# print(matrix[0][2])


# print(len(matrix))

dictionary = {"a": [1, 2, 1000], "b": 2}

# print(dictionary['a'][2])

user = {"basket": [1, 2, 3], "greet": "hello", "age": 20}
user2 = user.copy()
user.clear()
# print(user)
# print(user2)

# print('a' > 'A')
# print(chr('a'))
# print(ord('a'))
# print(ord('A'))

# my_list = [1,2,3,4,5,6,7,8,9,10]
# cnt = 0
# for x in my_list:
#    cnt += x
# print(cnt)


# print(range(100,20, -5))
# for x in range(100,20,-5):
#    print(x)

my_list = list(range(10))
# print(my_list)

# for i,char in enumerate('helloooo'):
#    print(i,char)


def highest_even(li):
    sl = sorted(li)
    sl = sl[::-1]
    # print(sl)
    for x in sl:
        if not x % 2:
            return x
    return False


# values = [10, 2, 3, 4, 5, 6, 7, 8, 11]
# print(highest_even(values))


total = 0


def count(total):
    total = total + 1
    # total += 1
    return total


# count()
# count()

# print(count())

x = "blah"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


# outer()

# print("X:",x)

""" import sys
try:
    age = str('abcde')
    print(age)
except ValueError as ve:
    print(f'ERROR: {ve}')
    print(f'ERROR: {ve.args}')
except:
    a,b,c = sys.exc_info()
    print(a)
    print(b)
    print(c)
else:
    print("all good")
finally:
    print("finally all done")

print("after")
 """


def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(3)
# print(my_list)


def generator_function(num):
    for i in range(num):
        yield i * 2


g = generator_function(1000)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# for item in generator_function(1000):
#    print(item)


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
            # next(iterator)
        except StopIteration:
            break


# special_for([1,2,3,4,5])


def fib(num=5):
    a = 0
    b = 1
    for _i in range(num):
        yield a
        tmp = a
        a = b
        b = tmp + b


# for x in fib(10):
#    print(x)

# import random
# print(dir(random))
# help(random.shuffle)


# import sys
# print(len(sys.argv) - 1)
# print(datetime.date.today())

# print(dir(array))

# arr = array.array('i', [1,2,3])
# pp.pprint(arr)

# pdb
def add(n1, n2):
    # pdb.set_trace()
    t = 4 * 5  # noqa: F841
    return n1 + n2


# add(4, 'blah')

# with open('/home/matt/git/snips/python/test.txt', mode='a') as myfile:
#    text = myfile.write('blahblah')

# myfile.seek(0)
# print(myfile.readlines())
# print(myfile.readline())

# myfile.close()

# with open('/home/matt/git/snips/python/test.txt', mode='r') as myfile:
# text = myfile.write('blahblah')
#    myfile.seek(0)
# print(myfile.readlines())
#    print(myfile.readline())

# print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep="\n")


def shortFact(x):
    return 1 if x <= 1 else x * shortFact(x - 1)


# f = shortFact(8)
# print(f'Factorial of 8 is {f}')

n = 1
ans = {i: i * i for i in range(1, n + 1)}
# print(ans)

# print(tuple(input("Enter a series of numbers separated by a comma :").split(',')))
lst = sorted("hi hi this is a stickup".split(" "))
tpl = sorted(set(lst))
# print(lst,tpl)
# print(dir(sorted))


# class myclass():
#    def __init__(self):
#        self.s = ""
#    def getstring(self):
#        self.s = input()
#    def printstring(self):
#        print(self.s.upper())

# str = myclass()
# str.getstring()
# str.printstring()

# for file in os.listdir('.'):
#    if fnmatch.fnmatch(file, '*.py'):
#        print(file)

# for x in filter(None, [0,1,2,3,4,5,6,7,8,9,False,None]):
#    print(x)

# print(hex(hash(str)).upper())
# print(hex(id(str)).upper())
# print(int())
# print(int('100',base=16))
# print(issubclass(myclass,object))

# print(globals())

# print(help(type(self)))
# print(locale.getpreferredencoding())

# print(x)
# print([x for x in reversed(x)])
# print(x)

# print(round(2.00454542462345623462352345234523452345234556789*1.00045234545634534534534534536778, 50))

# print(vars(object))

x = [1, 2, 3, 4, 5, 6, 7]
y = ["a", "b", "c", "d", "e", "f", "g"]
# zipped = zip(x,y)

# x2,y2 = zip(*zipped)
# print(x2)
# print(y2)
# print([x for x in zipped])
# print(bin(5))
# print(int('5').bit_length())


arts = [3, 4, 5]
farts = {"x": 1, "y": 2}
# print(arts)
# print(*arts)
# print(farts)
# print(**farts)

# def make_inc(n):
#    return lambda x: x + n

# f = make_inc(10)
# print(f(0))
# print(f(0))
# print(f(0))
# print(f(10))

pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]

# pairs.sort(key=lambda pair: pair[1])
# print(pairs)

# print(pairs[0][0])


def some_func(ham: str, eggs: str = "eggs") -> str:
    """This func does something

    But we're not really sure of what that something is
        but apparently, it does it well
        really really well

    but it also can collapse on itself... you have been warned.
    """
    print("Annotations: ", some_func.__annotations__)
    print("Args: ", ham, eggs)
    return ham + " and " + eggs


# print(some_func.__doc__)
# print(some_func("HAM",eggs = "EGGS"))

# x = 10
# def my_func(x):
#    print(x)
# my_func(x)

y = [99, 98, 97]
x.append(10)
x.extend(y)
x.insert(7, 13)
x.insert(7, 13)
x.insert(7, 13)
# print("Count of 13: " + str(x.count(13)))
ndx = x.index(13)
pndx = x.pop(ndx)
# print(pndx)
# x.remove(13)
# try:
#    x.remove(13)
# except ValueError as err:
#    print("value not found. Skipping.")

nn = x.pop()
# print(nn)
x.sort(reverse=True)
# print(x)
x.clear()
# print(x)

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
# print(stack)

# poop = stack.pop()
# print(poop)

# poop = stack.pop()
# print(poop)

# poop = stack.pop()
# print(poop)

# poop = stack.pop()
# print(poop)

# print(stack)


queue = deque(["Eric", "John", "Michael"], maxlen=5)
queue.append("Terry")
queue.append("Graham")
queue.appendleft("SAM")

# print(queue)

queue.popleft()
# print(queue)


squares = []
for x in range(10):
    squares.append(x**2)

# print(squares)

squares2 = list(map(lambda x: x**2, range(10)))
# print(squares2)

squares3 = [x**2 for x in range(10)]
# print(squares3)

combs = [
    [x, y] for x in [1, 2, 3] for y in [3, 1, 4] if x != y
]  # noqa: WPS441 WPS335
# print(combs)


vec = [-4, -2, 0, 2, 4]
vec2 = [x * 2 for x in vec if x > 0]
vec3 = [abs(x * 2) for x in vec]
# print(vec)
# print(vec2)
# print(vec3)

# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# stripped_fruit = [weapon.strip() for weapon in freshfruit]
# print(stripped_fruit)

sqr_tuples = [(x, x**2) for x in range(10)]
# print(sqr_tuples)

fat_vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(fat_vec)
# print([elem for elem in fat_vec])
thin_vec = [num for elem in fat_vec for num in elem]
# print(thin_vec)


rnd_pi = [str(round(math.pi, i)) for i in range(1, 12)]
# print(rnd_pi)


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# print(matrix)

# for i in range(4):
#    for row in matrix:
#        print(row[i])

# matrix2 = [[row[i] for row in matrix] for i in range(4)]

# print(list(zip(*matrix)))


# t1 = 12345, 54321, 'hello'
# print(t1)
# t2 = (12345, 54321, 'hello')
# print(t2)
# t3 = ()
# print(t3)


basket = {
    "apple",
    "orange",
    "apple",
    "pear",
    "orange",
    "banana",
}
# pp.pprint(basket)
# print('oranged' in basket)

a = set("abracadabra")
b = set("alacazam")

# print(sorted(a))
# print(sorted(b))

# print(a-b)
# print(b-a)

# print(a&b)
# print(a|b)
# print(a^b)


tel = {"jack": 4098, "sape": 4139}
tel["guido"] = 4127


# print(tel)
# print(list(tel))
# print(sorted(tel))

# print('guido' in tel)
# print('hi' in tel)
# print('jack' not in tel)

# d2 = dict([("sape", 4139), ("guido", 4127), ("jack", 4098)])
d2 = dict(
    [("sape", 4139), ("guido", 4127), ("jack", 4098)]
)  # noqa: C406
# print(d2)

d3 = {x: x**2 for x in range(0, 12, 2)}
# print(d3)


# for k,v in d3.items():
#    print(k,v)

# for i,v in enumerate(d3):
#    print(i,v)

basket = [
    "apple",
    "orange",
    "apple",
    "pear",
    "orange",
    "banana",
]
# print(type(basket))

basket_set = set(basket)
# print(type(basket_set))

sorted_basket_set = sorted(set(basket))
# print(type(sorted_basket_set))

# print(basket)
# print(basket_set)
# print(sorted_basket_set)
# print(__name__)

# if __name__ == "__main__":
#    print("MAIN")
#    print(__name__)
# elif __name__ == 'practice':
#    print('PRACTICE')
#    print(__name__)


# import builtins
# print(dir(builtins))


# with open('rando_file.txt', 'w') as f:
#    f.write('this is a string\n')
#    f.write('another string\n')

# with open('rando_file.txt', 'r') as f:
#    for line in f:
#        print(line, end='')

# with open('rando_file.txt', 'r') as f:
#    for line in f.readlines():
#        print(line, end='')

# with open('rando_file.txt', 'r') as f:
#    for line in list(f):
#        print(line, end='')


# xx = [1, "simple", "list"]

# with open("rando_file.txt", "w") as f:
#    json.dump(xx, f)

# with open("rando_file.txt", "r") as f:
#    json_loaded = json.load(f)
#    # pp.pprint(json_loaded)


# class MyClass:
#    """some doc string"""
# print(dir(MyClass))
# for att in dir(MyClass):
#    print(att)
#    print(dir(att))


# try:
#     s = 'abcdefg'
#     it = iter(s)
#     while True:
#         print(next(it),end=' ')
# except StopIteration as err:
#     print('\nno more iterations... ')
# else:
#     print('what else')
# finally:
#     print("all good")


def rev_data(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


# for char in rev_data('golf is fun'):
#     print(char, end=' ')

# cwd = os.getcwd()
# files = os.system("ls -1 " + cwd + '/*.txt')

# print(os.listdir(path = '.'))

# with urlopen('https://www.usno.navy.mil/USNO/time/master-clock') as response:
#    for line in response:
#        line = line.decode('utf-8')  # Decoding the binary data to text.
#        if 'UTC' in line:  # look for Eastern Time
#            print(line)


now = date.today().strftime(
    "%m-%d-%y. %d %b %Y is a %A on the %d day of %B."
)
# print(now)

# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# print(now)


s = b"witch which has which witches wrist watch"
# print(len(s))
# print(zlib.crc32(s))

# t = zlib.compress(s)
# print(len(t))
# print(zlib.crc32(t))

# w = zlib.decompress(t)
# print(len(w))
# print(zlib.crc32(w))


# with open('some.zip', 'rb') as f:
#     data = f.read()

# start = 0

# for i in range(5):
#     start += 14
#     fields = struct.unpack('<IIIHH', data[start:start+16])
#     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

#     start += 16
#     filename = data[start:start+filenamesize]
#     start += filenamesize
#     extra = data[start:start+extra_size]
#     print(filename, hex(crc32), comp_size, uncomp_size)

#     start += extra_size + comp_size     # skip to the next header

# full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
def full_name():
    return (
        lambda fn, ln: fn.strip().title()
        + " "
        + ln.strip().title()
    )


# print(full_name("first", " last "))


namelist = [
    "name4 A. Zast4",
    "name1 Cast1",
    "name2 Bast2",
    "name3 Aast3",
]
# print(namelist)
namelist.sort(key=lambda name: name.split(" ")[-1].lower())
# print(namelist)


def build_quad(a, b, c):
    return lambda x: a * x**2 + b * x + c


f = build_quad(2, 3, -5)


def bogus_func(a, b):
    return lambda x, y: a * x + b * y


f = bogus_func(1, 1)

temps = [("Berlin", 29), ("Cairo", 36)]


def c_to_f():
    return lambda data: (data[0], (9 / 5) * data[1] + 32)


# print(c_to_f(("blah", 100)))

# print(list(map(c_to_f, temps)))


data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
# print(avg)

# print(list(filter(lambda x: x > avg, data)))


# print(f(1,0))
# print(bogus_func(10,10)(1,1))

data = range(1, 6)
#
# multiplier = lambda x, y: x * y


def multiplier():
    return lambda x, y: x * y


# print(reduce(multiplier,data))


def mult(data):
    prod = 1
    for x in data:
        # prod = prod * x
        prod *= x
    return prod


# print(mult(data))

# 0 1 1 2 3 5 8 13 21 34

# @cache
@lru_cache(maxsize=1000)
def fib2(n):
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib2(n - 1) + fib2(n - 2)


# for n in range(1,500):
#    print(n, " : ", fib(n))

# fib(10)

fib_cache = {}


def fib3(n):
    if n in fib_cache:
        return fib_cache.get(n)

    if n == 1:
        val = 1
    elif n == 2:
        val = 1
    elif n > 2:
        val = fib3(n - 1) + fib3(n - 2)

    fib_cache[n] = val
    return val


# for n in range(1,1001):
#    print(n, " : ", fib2(n))


def greet(name):
    return f"HELLO, {name}"


# print(greet("me"))


def me(func):
    return func("ME!")


# print(me(greet))


def respect(maybe):
    def congrats():
        return "Congrats, bro!"

    def insult():
        return "You're silly!"

    if maybe == "yes":
        return congrats
    else:
        return insult


# print(respect("no")())


def startstop(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished!")

    return wrapper


@startstop  # roll = startstop(roll)
def roll():
    print("Rolling on the floor laughing XD")


# print(roll)
# print(id(roll))
# roll = startstop(roll)
# print(id(roll))
# print(roll)


# roll()

# print(roll())


def measuretime(func):
    def wrapper():
        starttime = time.perf_counter()
        func()
        endtime = time.perf_counter()
        print(f"Time needed: {endtime - starttime} seconds")

    return wrapper


@measuretime
def wastetime():
    sum([i**2 for i in range(1000000)])


# wastetime()


def sleep(func):
    def wrapper():
        time.sleep(3)
        func()
        # return func()

    return wrapper


# @sleep
# def wakeup():
#    print("Get up! Your break is over.")


# wakeup()


def debug(func):
    def wrapper():
        print(f"Calling {func.__name__}")
        func()

    return wrapper


@debug
def scare():
    print("Boo!")


# scare()


# def do_twice(func):
#    def wrapper_do_twice():
#        func()
#        func()
#    return wrapper_do_twice

# def do_twice(func):
#    def wrapper_do_twice(*args, **kwargs):
#        func(*args, **kwargs)
#        return func(*args, **kwargs)
#    return wrapper_do_twice


def do_twice(func):
    # @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def say_whee(name):
    print("WHEE!" + name)
    return f"say_whee {name}"


@do_twice
def greet_me():
    print("hello me!")
    return f"greet_me"  # noqa: F541


# say=say_whee('blah')
# greet=greet_me()

# print(say_whee)
# print(greet_me)


def get_counter():
    i = 0

    def out():
        nonlocal i
        i += 1
        return i

    return out


counter = get_counter()

# print(counter())
# print(counter())
# print(counter())


def debug(print_result=False):
    def decorator(func):
        @wraps(func)
        def out(*args, **kwargs):
            result = func(*args, **kwargs)
            print(
                func.__name__,
                result if print_result else "",
            )
            return result

        return out

    return decorator


@debug()
def add2(x, y):
    return x + y


# add2(10,20)


F = 44100
P1 = "71♩,69♪,,71♩,66♪,,62♩,66♪,,59♩,,"
P2 = "71♩,73♪,,74♩,73♪,,74♪,,71♪,,73♩,71♪,,73♪,,69♪,,71♩,69♪,,71♪,,67♪,,71♩,,"
# get_pause = lambda seconds: repeat(0, int(seconds * F))
# sin_f = lambda i, hz: math.sin(i * 2 * math.pi * hz / F)
# get_wave = lambda hz, seconds: (sin_f(i, hz) for i in range(int(seconds * F)))
# get_hz = lambda key: 8.176 * 2 ** (int(key) / 12)
# parse_note = lambda note: (get_hz(note[:2]), 1 / 4 if "♩" in note else 1 / 8)
# get_samples = lambda note: get_wave(*parse_note(note)) if note else get_pause(1 / 8)


def get_pause():
    return lambda seconds: repeat(0, int(seconds * F))


def sin_f():
    return lambda i, hz: math.sin(i * 2 * math.pi * hz / F)


def get_wave():
    return lambda hz, seconds: (
        sin_f(i, hz) for i in range(int(seconds * F))
    )


def get_hz():
    return lambda key: 8.176 * 2 ** (int(key) / 12)


def parse_note():
    return lambda note: (
        get_hz(note[:2]),
        1 / 4 if "♩" in note else 1 / 8,
    )


def get_samples():
    return (
        lambda note: get_wave(*parse_note(note))
        if note
        else get_pause(1 / 8)
    )


# samples_f = chain.from_iterable(get_samples(n) for n in f"{P1},{P1},{P2}".split(","))
# samples_b = b"".join(struct.pack("<h", int(f * 30000)) for f in samples_f)
# simpleaudio.play_buffer(samples_b, 1, 2, F)
# print(sys.getsizeof(greet_me))


pairs = [(1, "one"), (3, "three"), (2, "two"), (4, "four")]
tuples = [
    (1, 2, 3),
    (2, 3, 4),
    (2, 5, 6),
    (1, 7, 9),
    (3, 1, 1),
    (1, 4, 1),
]

# tuples.sort(key=itemgetter(0,2))
# tuples.sort(key=lambda tpl: tpl[0], reverse=False)
# pp.pprint(tuples)
# pp.pprint(pairs.sort(key=lambda pair: pair[0]))
# pp.pprint(sorted_pairs)
# pp.pprint(pairs)


def generate_big_tuple(size) -> tuple:
    big_list = []
    for i in range(size):
        big_list.append(i * random.randint(1, 10000))
    return tuple(big_list)


size = random.randrange(1500, 2000)
size = 5
big_tuple = generate_big_tuple(size)

# @me_decorators.log_call(CRITICAL=True)
# @me_decorators.debug
# @me_decorators.timer

# from log_calls import log_calls
# import log_calls
# print(type(log_calls.log_calls))
# @log_calls.log_calls()


def uncached_lookup(big_tuple: tuple, number_to_find: int):
    return number_to_find in big_tuple


@lru_cache(maxsize=256)
def cached_lookup(big_tuple: tuple, number_to_find: int):
    return number_to_find in big_tuple


@me_decorators.timer
def lookup_testing(bt, sz, lookuptype="cached"):
    lookup_count = 0
    rng1 = 100
    rng2 = 100

    if lookuptype == "cached":
        func = cached_lookup
    else:
        func = uncached_lookup

    for _ in range(rng1):
        for i in range(1, rng2):
            _ = func(bt, (sz - (i * 10)))
            lookup_count += 1

    logger.info(f"{lookuptype} :: {lookup_count} lookups")


# lookup_testing(big_tuple,size,'uncached')
# lookup_testing(big_tuple,size,'cached')

# https://gist.github.com/svidovich/4b40335e19ff16ab3c10eb88aefbbeee
@me_decorators.timer
def generate_big_list(size) -> list:
    big_list = []
    for _ in range(size):
        # big_list.append(random.randint(1, 100))
        big_list.append(int(random.random() * 100))
    return big_list


size = 10
# big_list = generate_big_list(size)

deduped_list = []


# @me_decorators.timer
# def dedup_list_1():
#    for item in big_list:
#        if item not in deduped_list:
#            deduped_list.append(item)


# deduped_list = []


# @me_decorators.timer
# def dedup_list_2():
#    deduped_list = list(set(big_list))


# dedup_list_1()
# dedup_list_2()

# t0 = time.time()
# lookup_count = 0
# for _ in range(100):
#     for i in range(1, 100):
#         _ = uncached_lookup(big_tuple, (size - (i * 10)))
#         lookup_count += 1
# t1 = time.time()

# print(f'{lookup_count} uncached lookups took {t1 - t0:.10f}ms')
# logger.info(f'{lookup_count} uncached lookups took {t1 - t0:.10f}ms')

# t0 = time.time()
# lookup_count = 0
# for _ in range(100):
#     for i in range(1, 100):
#         _ = cached_lookup(big_tuple, size - (i * 10))
#         lookup_count += 1

# t1 = time.time()

# print(f'{lookup_count} uncached lookups took {t1 - t0:.10f}ms')
# logger.info(f'{lookup_count}   cached lookups took {t1 - t0:.10f}ms')


# https://gist.github.com/svidovich/515190eff7322cdb899b3e51ebb32e9d


@me_decorators.timer
def generate_big_list_and_big_set(size) -> Tuple[list, set]:
    big_list = []
    big_set = set()
    for _ in range(size):
        number_to_append = int(random.random() * 100000000)
        # number_to_append = random.randint(1, 100000000)
        big_list.append(number_to_append)
        big_set.add(number_to_append)
    return big_list, big_set


@me_decorators.timer
def gen_big_list(size):
    big_list = []
    for _ in range(size):
        number_to_append = random.randint(1, 100000000)
        big_list.append(number_to_append)
    return big_list


@me_decorators.timer
def gen_big_set(size):
    big_set = set()
    for _ in range(size):
        number_to_append = random.randint(1, 100000000)
        big_set.add(number_to_append)
    return big_set


@me_decorators.timer
def gen_numbers_randint(size, rand_range=100000000):
    for _ in range(size):
        random.randint(1, rand_range)


@me_decorators.timer
def gen_numbers_randfloat(size, rand_range=100000000):
    for _ in range(size):
        int(random.random() * rand_range)


# size = 10000000
# random_range = 10000
# big_list, big_set = generate_big_list_and_big_set(size)

# gen_numbers_randint(size,random_range)
# gen_numbers_randfloat(size,random_range)

size = 3
big_list = gen_big_list(size)
big_set = gen_big_set(size)


@me_decorators.timer
def cast_list_to_set(lst):
    return set(lst)


@me_decorators.timer
def cast_set_to_list(st):
    return list(st)


# cast_list_to_set(big_list)
# cast_set_to_list(big_set)


lookup_count = 10


@me_decorators.timer
def set_lookup_1():
    for i in range(lookup_count):
        _ = i in big_list


@me_decorators.timer
def set_lookup_2():
    for i in range(lookup_count):
        _ = i in big_set


# set_lookup_1()
# set_lookup_2()


# size = 1000

# https://gist.github.com/svidovich/667fa6da22d76a79ff9457cd212cbf99
list_size = 10

# big_list_1 = generate_big_list(list_size)
# big_list_2 = generate_big_list(list_size)
xored_list = []


@me_decorators.timer
def xor_looping(big_list_1, big_list_2):
    for item in big_list_1:
        if item not in big_list_2:
            xored_list.append(item)
    for item in big_list_2:
        if item not in big_list_1:
            xored_list.append(item)


# @me_decorators.timer
# def xor_symmetric_differences(big_list_1, big_list_2):
#     xored_list = list(set(big_list_1).symmetric_difference(big_list_2))


# xor_looping(big_list_1, big_list_2)
# xor_symmetric_differences(big_list_1,big_list_2)


# https://gist.github.com/svidovich/14ccdd51bd7f9cbfbf9f1821968a0f0b
# https://medium.com/analytics-vidhya/hastily-constructed-precipitation-analysis-32e132dc1933


# https://leetcode.com/problems/lru-cache/discuss/1609364/Python.-Very-simple.-O(1)-Faster-than-80

# Alternate to explore later:
#    https://leetcode.com/problems/lru-cache/discuss/1628098/Python-Faster-Than-97-Using-Dictionary
#
class LRUCache:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__cache = {}

    def get(self, val: int) -> int:
        key = self.getmd5(val)
        if key not in self.__cache.keys():
            return -1
        else:
            val = self.__cache[key]
            self.__cache.pop(key)
            self.__cache[key] = val
            return val

    def put(self, val: int) -> None:
        key = self.getmd5(val)
        logger.info("key: %s\n", key)

        if key in self.__cache.keys():
            self.__cache.pop(key)
        self.__cache[key] = val
        if len(self.__cache.keys()) > self.__capacity:
            keyToRemove = next(iter(self.__cache.keys()))
            self.__cache.pop(keyToRemove)

    def getmd5(self, val):
        return hashlib.md5(str(val).encode()).hexdigest()

    def printlrucache(self):
        pp.pprint(self.__cache)


def practice_demo(args):
    logger.info("practice demo ")


logger.info("end of practice")
## END
