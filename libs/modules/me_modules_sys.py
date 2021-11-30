#!/usr/bin/env python3
"""sys module tests"""
import sys

import logging

# from numpy import empty


logger = logging.getLogger("SYS")


def me_modules_sys(args=None):
    logger.debug("me_modules_sys")
    # sys_test()
    sys_module_system()


def sys_module_system():  # noqa: WPS213
    sys_module_abiflags()
    sys_module_addaudithook()
    sys_module_api_version()
    sys_module_argv()
    sys_module_audit()
    sys_module_base_exec_prefix()
    sys_module_base_prefix()
    sys_module_breakpointhook()
    sys_module_builtin_sys_module_names()
    sys_module_byteorder()
    sys_module_call_tracing()
    sys_module_copyright()
    sys_module_displayhook()
    sys_module_dont_write_bytecode()
    sys_module_exc_info()
    sys_module_excepthook()
    sys_module_exec_prefix()
    sys_module_executable()
    sys_module_exit()
    sys_module_flags()
    sys_module_float_info()
    sys_module_float_repr_style()
    sys_module_get_asyncgen_hooks()
    sys_module_get_coroutine_origin_tracking_depth()
    sys_module_getallocatedblocks()
    sys_module_getdefaultencoding()
    sys_module_getdlopenflags()
    sys_module_getfilesystemencodeerrors()
    sys_module_getfilesystemencoding()
    sys_module_getprofile()
    sys_module_getrecursionlimit()
    sys_module_getrefcount()
    sys_module_getsizeof()
    sys_module_getswitchinterval()
    sys_module_gettrace()
    sys_module_hash_info()
    sys_module_hexversion()
    sys_module_implementation()
    sys_module_int_info()
    sys_module_intern()
    sys_module_is_finalizing()
    sys_module_maxsize()
    sys_module_maxunicode()
    sys_module_meta_path()
    sys_module_modules()
    sys_module_orig_argv()
    sys_module_path()
    sys_module_path_hooks()
    sys_module_path_importer_cache()
    sys_module_platform()
    sys_module_platlibdir()
    sys_module_prefix()
    sys_module_pycache_prefix()
    sys_module_set_asyncgen_hooks()
    sys_module_set_coroutine_origin_tracking_depth()
    sys_module_setdlopenflags()
    sys_module_setprofile()
    sys_module_setrecursionlimit()
    sys_module_setswitchinterval()
    sys_module_settrace()
    sys_module_stderr()
    sys_module_stdin()
    sys_module_stdlib_sys_module_names()
    sys_module_stdout()
    sys_module_thread_info()
    sys_module_unraisablehook()
    sys_module_version()
    sys_module_version_info()
    sys_module_warnoptions()


def sys_test():
    import libs.me_utilities

    logger.debug("SYS_TEST")

    libs.me_utilities.obj_functions(sys, gen_func=True)


def sys_module_abiflags():
    pass


def sys_module_addaudithook():
    pass


def sys_module_api_version():
    pass


def sys_module_argv():
    pass


def sys_module_audit():
    pass


def sys_module_base_exec_prefix():
    pass


def sys_module_base_prefix():
    pass


def sys_module_breakpointhook():
    pass


def sys_module_builtin_sys_module_names():
    pass


def sys_module_byteorder():
    pass


def sys_module_call_tracing():
    pass


def sys_module_copyright():
    pass


def sys_module_displayhook():
    pass


def sys_module_dont_write_bytecode():
    pass


def sys_module_exc_info():
    pass


def sys_module_excepthook():
    pass


def sys_module_exec_prefix():
    pass


def sys_module_executable():
    pass


def sys_module_exit():
    pass


def sys_module_flags():
    pass


def sys_module_float_info():
    pass


def sys_module_float_repr_style():
    pass


def sys_module_get_asyncgen_hooks():
    pass


def sys_module_get_coroutine_origin_tracking_depth():  # noqa: WPS118
    pass


def sys_module_getallocatedblocks():
    pass


def sys_module_getdefaultencoding():
    pass


def sys_module_getdlopenflags():
    pass


def sys_module_getfilesystemencodeerrors():
    pass


def sys_module_getfilesystemencoding():
    pass


def sys_module_getprofile():
    pass


def sys_module_getrecursionlimit():
    pass


def sys_module_getrefcount():
    pass


def sys_module_getsizeof():  # noqa: WPS210
    empty_str = sys.getsizeof("")
    t_str = sys.getsizeof("t")
    te_str = sys.getsizeof("te")
    tes_str = sys.getsizeof("tes")
    test_str = sys.getsizeof("test")

    zero_int = sys.getsizeof(int(0))
    one_int = sys.getsizeof(int(1))
    two_int = sys.getsizeof(int(2))
    three_int = sys.getsizeof(int(3))

    logger.info(empty_str)

    logger.info(t_str)
    logger.info(te_str)
    logger.info(tes_str)
    logger.info(test_str)

    logger.info(zero_int)
    logger.info(one_int)
    logger.info(two_int)
    logger.info(three_int)


def sys_module_getswitchinterval():
    pass


def sys_module_gettrace():
    pass


def sys_module_hash_info():
    pass


def sys_module_hexversion():
    pass


def sys_module_implementation():
    pass


def sys_module_int_info():
    pass


def sys_module_intern():
    pass


def sys_module_is_finalizing():
    pass


def sys_module_maxsize():
    pass


def sys_module_maxunicode():
    pass


def sys_module_meta_path():
    pass


def sys_module_modules():
    pass


def sys_module_orig_argv():
    pass


def sys_module_path():
    pass


def sys_module_path_hooks():
    pass


def sys_module_path_importer_cache():
    pass


def sys_module_platform():
    pass


def sys_module_platlibdir():
    pass


def sys_module_prefix():
    pass


def sys_module_pycache_prefix():
    pass


def sys_module_set_asyncgen_hooks():
    pass


def sys_module_set_coroutine_origin_tracking_depth():  # noqa: WPS118
    pass


def sys_module_setdlopenflags():
    pass


def sys_module_setprofile():
    pass


def sys_module_setrecursionlimit():
    pass


def sys_module_setswitchinterval():
    pass


def sys_module_settrace():
    pass


def sys_module_stderr():
    pass


def sys_module_stdin():
    pass


def sys_module_stdlib_sys_module_names():
    pass


def sys_module_stdout():
    pass


def sys_module_thread_info():
    pass


def sys_module_unraisablehook():
    pass


def sys_module_version():
    pass


def sys_module_version_info():
    pass


def sys_module_warnoptions():
    pass
