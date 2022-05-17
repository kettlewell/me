#!/usr/bin/env python3
"""Concurrency tests"""
import sys

assert sys.version_info >= (3, 7), "Script requires Python 3.7+"

from threading import Thread
from queue import Queue

import concurrent.futures

import asyncio
from aiohttp import ClientSession, ClientConnectorError

import grequests

import requests

import logging
from config import INPUT_PATH

logger = logging.getLogger("CONCURRENCY")


infile = INPUT_PATH / "url_list.txt"


def concurrency(args=None):
    logger.info("concurrency")

    if args:
        print(vars(args))
        logger.info(vars(args))
    # from Medium article titled "Python -- How to Send 100K Requests Quickly"

    # Queue + Multithreading
    # queue_multithreading()

    # Thread Pool
    # thread_pool()

    # Coroutine + aiohttp
    coroutine_aiohttp()

    # grequests
    requests_gevent()


def queue_multithreading():
    logger.info("queue_multithreading")
    concurrent = 2

    def do_work():
        while True:
            url = q.get()
            status, url = get_status(url)
            do_sth_with_result(status, url)
            q.task_done()

    def get_status(o_url):
        try:
            res = requests.get(o_url)
            return res.status_code, o_url
        except:  # noqa: E722
            return "error", o_url

    def do_sth_with_result(status, url):
        print(status, url)

    q = Queue(concurrent * 2)
    for i in range(concurrent):
        t = Thread(target=do_work)
        t.daemon = True
        t.start()

    try:
        for url in open(infile):
            q.put(url.strip())
        q.join()
    except KeyboardInterrupt:
        sys.exit(1)


def thread_pool():
    logger.info("thread_pool")

    out = []
    CONNECTIONS = 2
    TIMEOUT = 5
    urls = []

    with open(infile) as reader:
        for url in reader:
            urls.append(url.strip())

    def load_url(url, timeout):
        ans = requests.get(url, timeout=timeout)
        return ans.status_code

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        future_to_url = (executor.submit(load_url, url, TIMEOUT) for url in urls)
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
            except Exception as exc:
                data = str(type(exc))
            finally:
                out.append(data)
                print(data)


def coroutine_aiohttp():
    logger.info("coroutine_aiohttp")

    async def fetch_html(url: str, session: ClientSession, **kwargs) -> tuple:
        try:
            resp = await session.request(method="GET", url=url, **kwargs)
        except ClientConnectorError:
            return (url, 404)
        return (url, resp.status)

    async def make_requests(urls: set, **kwargs) -> None:
        async with ClientSession() as session:
            tasks = []
            for url in urls:
                tasks.append(fetch_html(url=url, session=session, **kwargs))
            results = await asyncio.gather(*tasks)
        for result in results:
            print(f"{result[1]} - {str(result[0])}")

    with open(infile) as inf:
        urls = set(map(str.strip, inf))

    asyncio.run(make_requests(urls=urls))


def requests_gevent():
    logger.info("grequests")

    def exception_handler(request, exception):
        print("Request Failed")

    urls = []

    with open(infile) as reader:
        for url in reader:
            urls.append(url.strip())
    reqs = (grequests.get(u) for u in urls)

    for result in grequests.map(reqs, exception_handler=exception_handler):
        print(result.status_code, result.url)
