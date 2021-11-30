#!/usr/bin/env python3
"""
These are reusable decorators that I might be interested in using someday
"""
import logging
import sys
from functools import wraps
from typing import Dict, List, Any
import time
import libs.me_globals as me_globals

def me_decorators(args=None):
    # for decorators, I want the logger name to be from the calling function
    # so it makes sense to set the name per method in this class
    # [ though this method should really be located elsewhere, since it's not an actual decorator ]
    logger = logging.getLogger('DECORATOR')
    logger.info("me_decorator")

    if args:
        print(vars(args))
        logger.info(vars(args))


# decorator boilerplate:

def decorator_boilerplate(func):
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


# https://betterprogramming.pub/six-advanced-decorator-patterns-5ffe67552691
def log_output(fun, result: Any, kw: Dict, check_state: List ) -> None:

    logger = logging.getLogger(fun.__name__)

    for key in kw:
        keyl = key.lower()
        if keyl in check_state:
            if kw[key]:
                eval('logger.' + keyl)("function: {}, result: {}".format(fun.__name__, result))

def log_call(*a, **kw):
    """
    decorator with @log_call wraps the function with log events
    """
    def decorator(fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            #PRE
            result = fun(*args, **kwargs)
            #POST
            check_state = ('debug', 'info', 'success', 'warning', 'error', 'critical')
            log_output(fun,result, kw, check_state)
            return result
        return wrapper
    return decorator



#def timing(f):
#    @wraps(f)
#    def wrap(*args, **kw):
#        ts = time()
#        result = f(*args, **kw)
#        te = time()
#        print('func:%r args:[%r, %r] took: %2.4f sec').format(f.__name__, args, kw, te-ts)
#        return result
#    return wrap

def timer(func):
    """Print the runtime of the decorated function"""
    logger = logging.getLogger(func.__name__)
    logger.info("timer decorator")
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        #print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        logger.info(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

def debug(func):
    """Print the function signature and return value"""
    @wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

#PLUGINS = dict()
def register(func):
    """Register a function as a plug-in"""
    me_globals.PLUGINS[func.__name__] = func
    return func

def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

