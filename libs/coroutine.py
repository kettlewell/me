#!/usr/bin/env python3
"""coroutine based routines"""
import asyncio
import time

import logging

logger = logging.getLogger("COROUTINE")


def coroutine(args=None):
    logger.debug("coroutine")

    # how do I catch this issue?
    # try:
    #    coroutine_demo()
    # except RuntimeWarning as e:
    #    print("ERROR: ", str(e))
    #    logger.error("This is not how coroutines are called")

    # correct way to call coroutines
    #

    #    asyncio.run(coroutine_demo())
    #    asyncio.run(coroutine_demo2())

    #    asyncio.run(coroutine_tasks())

    asyncio.run(coroutine_factorial_generator())


async def coroutine_factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(0.25)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def coroutine_factorial_generator():
    L = await asyncio.gather(coroutine_factorial("A", 20), coroutine_factorial("B", 25), coroutine_factorial("C", 30))
    print(L)


async def coroutine_tasks():
    task1 = asyncio.create_task(say_after(2, "hello"))

    task2 = asyncio.create_task(say_after(1, "world"))

    logger.info(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    logger.info(f"finished at {time.strftime('%X')}")


async def say_after(delay, what):
    await asyncio.sleep(delay)
    logger.info(what)


async def coroutine_demo2():
    logger.info(f"started at {time.strftime('%X')}")
    await say_after(1, "Hello")
    await say_after(2, "world")
    logger.info(f"Finished at {time.strftime('%X')}")


async def coroutine_demo():
    logger.info("demo start")
    await asyncio.sleep(1)
    logger.info("demo stop")
