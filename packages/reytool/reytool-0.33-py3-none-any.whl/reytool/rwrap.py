# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
══════════════════════════════
@Time    : 2022-12-05 14:12:25
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Rey's decorators
══════════════════════════════
"""


import time
from tqdm import tqdm as tqdm_tqdm
from threading import Thread
from functools import wraps as functools_wraps

from .rbasic import check_parm
from .rcommon import exc
from .rtext import print_frame
from .rtype import Function, Method
from .rtime import now


def wrap_frame(decorator: "Function | Method") -> "Function":
    """
    Decorative frame.

    Parameters
    ----------
    decorator : Function or Method
        Decorator function.

    Retuens
    -------
    Function
        Decorator after decoration.

    Examples
    --------
    Decoration function method one.

    >>> @wrap_func
    >>> def func(): ...
    >>> func_ret = func(parm_a, parm_b, parm_c=1, parm_d=2)

    Decoration function method two.

    >>> def func(): ...
    >>> func_ret = wrap_func(func, parm_a, parm_b, parm_c=1, parm_d=2)

    Decoration function method three.

    >>> def func(): ...
    >>> func_ret = wrap_func(func, _execute=True)
    
    Decoration function method four.

    >>> def func(): ...
    >>> func = wrap_func(func)
    >>> func_ret = func(parm_a, parm_b, parm_c=1, parm_d=2)

    Decoration function method five.

    >>> def func(): ...
    >>> func = wrap_func(func, parm_a, parm_c=1, _execute=False)
    >>> func_ret = func(parm_b, parm_d=2)
    """

    check_parm(decorator, Function, Method)

    @functools_wraps(decorator)
    def wrap(func: "Function | Method", *args: "object", _execute: "bool"=None, **kwargs: "object") -> "Function | object":
        """
        Decorative shell.

        Parameters
        ----------
        _execute : bool or None
            Whether execute function, otherwise decorate function.

            - bool : Use this value.
            - None : When parameter *args or **kwargs have values, then True, otherwise False.
        
        Returns
        -------
        Function or object
            Function after decoration or return of function.
        """
        
        check_parm(_execute, bool, None)

        if _execute == None:
            if args or kwargs:
                _execute = True
            else:
                _execute = False

        if _execute:
            func_ret = decorator(func, *args, **kwargs)
            return func_ret
        
        else:
            @functools_wraps(func)
            def wrap_sub(*_args: "object", **_kwargs: "object") -> "object":
                """
                Decorative sub shell.
                """

                func_ret = decorator(func, *args, *_args, **kwargs, **_kwargs)
                return func_ret
            return wrap_sub
    return wrap

def wraps(*wrap_funcs: "Function | Method") -> "Function":
    """
    Batch decorate.

    parameters
    ----------
    wrap_funcs : Function or Method
        Decorator function.

    Retuens
    -------
    Function
        Function after decoration.

    Examples
    --------
    Decoration function.

    >>> @wraps(print_funtime, state_thread)
    >>> def func(): ...
    >>> func_ret = func()
    
        Same up and down

    >>> @print_funtime
    >>> @state_thread
    >>> def func(): ...
    >>> func_ret = func()

        Same up and down

    >>> def func(): ...
    >>> func = print_funtime(func)
    >>> func = state_thread(func)
    >>> func_ret = func()
    """

    check_parm(wrap_funcs, Function, Method, check_element=True)

    def func(): ...
    for wrap_func in wrap_funcs:
        
        @functools_wraps(func)
        def wrap(func: "Function | Method") -> "Function":
            """
            Decorative shell
            """

            @functools_wraps(func)
            def wrap_sub(*args: "object", **kwargs: "object") -> "object":
                """
                Decorative sub shell
                """

                func_ret = wrap_func(func, *args, _execute=True, **kwargs)
                return func_ret
            return wrap_sub
        func = wrap
    return wrap

@wrap_frame
def runtime(func: "Function | Method", *args: "object", **kwargs: "object") -> "object":
    """
    Print run time of the function.

    Parameters
    ----------
    func : Function or Method
        Function to be decorated.
    *args : object
        Position parameter of input parameter decorated function.
    *kwargs : object
        Keyword parameter of input parameter decorated function.

    Returns
    -------
    object
        Return of decorated function.
    """

    check_parm(func, Function, Method)

    start_datetime = now()
    start_timestamp = now("timestamp")
    func_ret = func(*args, **kwargs)
    end_datatime = now()
    end_timestamp = now("timestamp")
    spend_timestamp = end_timestamp - start_timestamp
    spend_second = round(spend_timestamp, 2)
    print_content = "Start: %s -> Spend: %ss -> End: %s" % (start_datetime, spend_second, end_datatime)
    title = func.__name__
    print_frame(print_content, title=title)
    return func_ret

@wrap_frame
def start_thread(func: "Function | Method", *args: "object", _daemon: "bool"=True, **kwargs: "object") -> "None":
    """
    Function start in thread.

    Parameters
    ----------
    func : Function or Method
        Function to be decorated.
    *args : object
        Position parameter of input parameter decorated function.
    _daemon : bool
        Whether it is a daemon thread.
    *kwargs : object
        Keyword parameter of input parameter decorated function.
    """

    check_parm(func, Function, Method)
    check_parm(_daemon, bool)

    thread_name = "%s_%s" % (func.__name__, str(int(time.time() * 1000)))
    thread = Thread(target=func, name=thread_name, args=args, kwargs=kwargs)
    thread.daemon = _daemon
    thread.start()

@wrap_frame
def try_exc(
    func: "Function | Method",
    *args: "object",
    **kwargs: "object"
) -> "object | None":
    """
    Execute function with 'try' syntax and print error information.

    Parameters
    ----------
    func : Function or Method
        Function to be decorated.
    *args : object
        Position parameter of input parameter decorated function.
    *kwargs : object
        Keyword parameter of input parameter decorated function.

    Returns
    -------
    object or None
        Return of decorated function or no return.
    """
    
    check_parm(func, Function, Method)

    try:
        func_ret = func(*args, **kwargs)
        return func_ret
    except:
        func_name = func.__name__
        exc(func_name)

@wrap_frame
def update_tqdm(
    func: "Function | Method",
    tqdm: "tqdm_tqdm",
    *args: "object",
    _desc: "str"=None,
    _step: "int | float"=1,
    **kwargs: "object"
) -> "object":
    """
    Update progress bar tqdm object of tqdm package.

    Parameters
    ----------
    func : Function or Method
        Function to be decorated.
    tqdm : tqdm object
        Progress bar tqdm object.
    *args : object
        Position parameter of input parameter decorated function.
    _desc : str or None
        Progress bar description.

        - str : Add description.
        - None : no description.

    _step : int or float
        Progress bar step size.

        - When greater than 0, then forward.
        - When less than 0, then backward.

    *kwargs : object
        Keyword parameter of input parameter decorated function.

    Returns
    -------
    object or None
        Return of decorated function or no return.
    """

    check_parm(func, Function, Method)
    check_parm(tqdm, tqdm_tqdm)
    check_parm(_desc, str, None)
    check_parm(_step, int, float)

    if _desc != None:
        tqdm.set_description(_desc)
    func_ret = func(*args, **kwargs)
    tqdm.update(_step)
    return func_ret