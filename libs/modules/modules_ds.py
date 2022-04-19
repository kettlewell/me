#!/usr/bin/env python3
"""Lists based routines"""

import logging
import pprint as pp
import numpy as np
import pandas as pd

from datetime import datetime
import pytz

import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt


logger = logging.getLogger("DS")


def modules_ds(args=None):
    logger.info("\nSTART modules_ds")
    # read_pandas(do_plot=False)
    # read_httpd_log_with_pandas()
    # ris_demo()
    np_init()
    logger.info("END modules_ds\n")


def np_init():
    logger.info("\nSTART np_init()")
    a = np.array([1, 2, 3])
    b = np.array((3, 4, 5))
    ones = np.ones((3, 4), dtype=np.int16)
    full = np.full((3, 4), 0.11)
    arange_1 = np.arange(10, 30, 5)
    arange_2 = np.arange(0, 2, 0.3)
    linspace = np.linspace(0, 5 / 3, 6)
    rand = np.random.rand(4, 6)
    empty = np.empty((2, 3))

    logger.debug("\n[{}] - {}\n".format(" np array A ", a))
    logger.debug("\n[{}] - {}\n".format(" np array B ", b))
    logger.debug("\n{}  {}\n".format("Type of np array A : ", type(a)))
    logger.debug("\n{}  {}\n".format("Type of np array B : ", type(b)))

    logger.debug("\n\nONES\n{}\n".format(ones))
    logger.debug("\n\nARANGE_1\n{}\n".format(arange_1))
    logger.debug("\n\nARANGE_2\n{}\n".format(arange_2))
    logger.debug("\n\nLINSPACE\n{}\n".format(linspace))
    logger.debug("\n\nRAND\n{}\n".format(rand))
    logger.debug("\n\nRAND.reshape\n{}\n".format(rand.reshape(12, 2)))
    logger.debug("\n\nRAND\n{}\n".format(rand))

    logger.debug("\n\nEMPTY\n{}\n".format(empty))

    logger.debug("\n\nFULL\n{}\n".format(full))
    logger.debug("FULL.itemsize  {}".format(full.itemsize))
    logger.debug("FULL.dtype     {}".format(full.dtype))
    logger.debug("FULL.size      {}".format(full.size))
    logger.debug("FULL.shape     {}".format(full.shape))
    logger.debug("FULL.ndim      {}".format(full.ndim))

    full = full.reshape(2, 6)
    logger.debug("\nFULL\n{}\n".format(full))

    r1 = rand[2:5]
    r2 = rand[2::]
    r3 = rand[::-1]
    r4 = rand[1:]

    logger.debug("\n\nRAND\n{}\n".format(rand))

    logger.debug("\nR1{}\n".format(r1))
    logger.debug("\nR2{}\n".format(r2))
    logger.debug("\nR3{}\n".format(r3))
    logger.debug("\nR4{}\n".format(r4))
    logger.debug("Type(rand): {}".format(type(rand)))
    logger.debug("Type(rand[0]): {}".format(type(rand[0])))
    logger.debug("Type(rand[0][0]): {}".format(type(rand[0][0])))

    a = np.array([1, 2, 5, 7, 8])
    b = [1, 2, 5, 7, 8]

    try:
        a[1:3] = -1
        b[1:3] = -1
    except TypeError:
        logger.exception("Can't Assign Type - not iterable")

    logger.debug("A: {}".format(a))
    logger.debug("B: {}".format(b))

    np_a = np.array([1, 2, 5, 7, 8])
    np_a_slice = np_a[1:5]
    np_a_slice[1] = 1000
    logger.debug("N_A: {}".format(np_a))

    p_a = [1, 2, 5, 7, 8]
    p_b = p_a[1:5]
    p_b[1] = 3

    logger.debug("P_A: {}".format(p_a))
    logger.debug("P_B: {}".format(p_b))

    del a

    a = np.arange(12).reshape(3, 4)
    logger.debug("A: {}".format(a))

    rows_on = np.array([True, False, True])
    rows_binary = np.array([1, 0, 1])

    logger.debug("\n\nA[rows_on, :] : \n{}\n".format(a[rows_on, :]))
    logger.debug("\n\nA : \n{}\n".format(a))
    logger.debug("\n\nA[rows_binary, :] : \n{}\n\n\n\n".format(a[rows_binary, :]))

    logger.info("\n\n\n")
    logger.info("END np_init\n")


def get_iris_data():
    data = pd.read_csv(
        "./input/iris.csv",
        header=0,
        usecols=[0, 1, 2, 3, 4],
        names=[
            "sepal_width",
            "sepal_length",
            "petal_width",
            "petal_length",
            "class",
        ],
    )
    return data


def read_httpd_log_with_pandas():

    #    print(parse_str("[my string]"))
    #    print(parse_datetime("13/Nov/2015:11:45:42 +0000"))
    print()
    data = pd.read_csv(
        "./input/httpd.log",
        sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
        engine="python",
        na_values="-",
        header=None,
        usecols=[0, 3, 4, 5, 6, 7, 8],
        names=[
            "ip",
            "time",
            "request",
            "status",
            "size",
            "referer",
            "user_agent",
        ],
        converters={
            "time": parse_datetime,
            "request": parse_str,
            "status": int,
            "size": int,
            "referer": parse_str,
            "user_agent": parse_str,
        },
    )

    # pd.set_option("max_colwidth", 35)
    # data = read_httpd_log_with_pandas()

    # print(data.head())

    #    split_request(data)
    #    print(data.head())
    print()
    #    print(data.groupby("status").get_group(403))
    #    print()
    #    print(data.groupby("status").get_group(200))

    print(data.info(verbose=True))
    print()
    for x in data.columns:
        print(x)

    print(data.attrs)
    print(data.axes)
    print(data.ndim)
    print(data.loc[[2, 3, 4, 5], "status"])
    # return data


def read_pandas(do_plot=False):

    # Make the graphs a bit prettier, and bigger
    #    plt.style.use("ggplot")
    plt.rcParams["figure.figsize"] = (45, 7)

    df = pd.read_csv("./input/metrics_demo2.csv")
    #    print(metrics_df[:3])
    #    pp.pprint(metrics_df[["latency", "timestamp"]][:5])

    #    pp.pprint(metrics_df.iloc[3])
    # metrics_df["timestamp"].plot(x="name", y="age", kind="bar")
    # pp.pprint(matplotlib.get_backend())

    for x, y in df[:5].iterrows():
        pp.pprint(x)
        pp.pprint(y)
        print()

    print()
    print()
    for i in list(df):
        print(df[i][0])

    print()
    print()

    # columns = list(df[:5])
    # for i in columns:
    #     pp.pprint(df[i])
    print(df.head(3))
    print(df[:2])
    print(list(df))
    for i in df[:5].itertuples():
        print(i)

    for name, data in df[:5].iteritems():
        print("NAME: ", name)
        print("DATA: ", data.values)

    plt.plot(df[["latency", "timestamp"]])

    if do_plot:
        plt.show()


def split_request(data):
    request = data.pop("request").str.split()
    data["url"] = request.str[1]
    data["action"] = request.str[0]
    data["proto"] = request.str[2]
    return data


# https://mmas.github.io/read-apache-access-log-pandas
def parse_str(x):
    return x[1:-1]


def parse_datetime(x):
    dt = datetime.strptime(x[1:-7], "%d/%b/%Y:%H:%M:%S")
    dt_tz = int(x[-6:-3]) * 60 + int(x[-3:-1])
    return dt.replace(tzinfo=pytz.FixedOffset(dt_tz))


def moving_avg(data, window):
    dma = data.copy()
    dma["MA"] = dma.rolling(window=window).mean()
    return dma


def iris_demo():
    logger.info("iris demo ")

    # lru = LRUCache(5)
    # lru.printlrucache()
    # lru.put(10)
    # lru.printlrucache()
    # lru.put(20)
    # lru.printlrucache()
    # lru.put(30)
    # lru.printlrucache()
    # lru.put(40)
    # lru.printlrucache()
    # lru.put(50)
    # lru.printlrucache()
    # lru.put(60)
    #   lru.printlrucache()
    #    lru.put(70)
    #    lru.printlrucache()

    # logger.info(lru.get(10))
    # logger.info(lru.get(20))
    # logger.info(lru.get(30))
    # logger.info(lru.get(40))
    # logger.info(lru.get(50))
    # logger.info(lru.get(60))
    # logger.info(lru.get(70))

    # read_pandas()

    iris_data = get_iris_data()
    # print()
    print(iris_data.head())

    # print()

    # print(iris_data.groupby("class").get_group("Iris-setosa"))
    # print()
    groups = iris_data.groupby("class").groups
    print(groups.keys())

    group_class = iris_data.groupby("class")
    #    for name, group in group_class:
    #        print(name)
    #        # print(group)

    class_agg = group_class.aggregate(np.sum)
    logger.debug(class_agg)

    class_sum = group_class.sum()
    logger.debug(class_sum)
    #    print()
    #    print()
    #    print(class_sum)
    #    print(group_class.size())
    #    print()
    #    print(group_class.describe())
    #    print()
    #    print(group_class.nunique())
    #    print()
    #    print(group_class.std())

    #    print()
    #    print(group_class["sepal_width"].agg([np.sum, np.mean, np.std]))

    #    print()
    # print(
    #     group_class.agg(
    #         max_sepal_width=pd.NamedAgg(column="sepal_width", aggfunc=max),
    #         min_sepal_width=pd.NamedAgg(column="sepal_width", aggfunc="min"),
    #         mean_sepal_width=pd.NamedAgg(column="sepal_width", aggfunc=np.mean),
    #         range_sepal_width=pd.NamedAgg(column="sepal_width", aggfunc=lambda x: max(x) - min(x)),
    #     ),
    # )

    #    print(iris_data.head())
    transformed = group_class.transform(lambda x: x.fillna(x.mean()))
    logger.debug(transformed)
    #    print(transformed)

    # print()

    dma = iris_data["sepal_width"].to_frame()
    #    dma.to_frame()
    # print(type(dma))
    # print(dma.head(10))
    # print()
    dma["MA"] = dma.rolling(window=5).mean()
    # print(type(dma))
    # print(dma.head(10))

    # print()

    ma_5_iris = moving_avg(iris_data["sepal_width"].to_frame(), 5)
    logger.debug(ma_5_iris)
    # print(ma_5_iris)
