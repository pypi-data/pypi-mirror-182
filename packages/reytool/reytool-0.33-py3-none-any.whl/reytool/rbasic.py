# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
══════════════════════════════
@Time    : 2022-12-05 14:09:42
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Rey"s basic methods
══════════════════════════════
"""


from warnings import warn as warnings_warn
from varname import argname

from .rtype import Function, Method, errors


def error(error_info: "object"=None, error_type: "BaseException"= AssertionError) -> "None":
    """
    Throw error.

    Parameters
    ----------
    *error_info : object
        Error information.
    error_type : BaseException
        Error type.
    """
    
    check_parm(error_type, *errors)
    
    if error_info == None:
        raise error_type
    raise error_type(error_info)

def warn(*warn_infos: "object", warn_type: "BaseException"= UserWarning, stacklevel: "int"=3) -> "None":
    """
    Throw warning.

    Parameters
    ----------
    *warn_info : object
        Warn informations.
    warn_type : BaseException
        Warn type.
    stacklevel : int
        Warning code location, number of recursions up the code level.
    """
    
    check_parm(warn_type, *errors)
    
    if warn_infos == ():
        warn_infos = "Warning!"
    elif len(warn_infos) == 1:
        warn_info_type = type(warn_infos[0])
        if warn_info_type == str:
            warn_infos = warn_infos[0]
        else:
            warn_infos = str(warn_infos[0])
    else:
        warn_infos = str(warn_infos)
    warnings_warn(warn_infos, warn_type, stacklevel)

def check_parm(value: "object", *targets: "object | str", check_element: "bool"=False) -> "None":
    """
    Check the content or type of the value, when check fail, then throw error.

    Parametes
    ---------
    value : object
        Check object.
    *targets : object or str {'_iterable'}
        Correct target, can be type.

        - object : Check whether it is the target.
        - '_iterable' : Check whether it can be iterable.

    check_element : bool
        Whether check element in value.
    """

    if check_element:
        values = value
    else:
        values = [value]
    for element in values:
        if "_iterable" in targets and is_iterable(element):
            continue
        if type(element) in targets:
            continue
        targets_id = [id(target) for target in targets]
        if id(element) in targets_id:
            continue
        try:
            var_name = argname("value")
            var_name = " '%s'" % var_name
        except:
            var_name = ""
        correct_targets_str = ", ".join([repr(target) for target in targets])
        if check_element:
            error_text = "parameter%s the elements content or type must in [%s], now: %s" % (var_name, correct_targets_str, repr(value))
        else:
            error_text = "parameter%s the content or type must in [%s], now: %s" % (var_name, correct_targets_str, repr(value))
        error(error_text, ValueError)
    
def check_parm_least_one(*values: "object") -> "None":
    """
    Check that at least one of multiple values is not None, when check fail, then throw error.

    Parameters
    ----------
    *values : object
        Check values.
    """

    for value in values:
        if value != None:
            return
    try:
        vars_name = argname("values")
    except:
        vars_name = None
    if vars_name:
        vars_name_str = " " + " and ".join(["\"%s\"" % var_name for var_name in vars_name])
    else:
        vars_name_str = ""
    error_text = "at least one of parameters%s is not None" % vars_name_str
    error(error_text, ValueError)

def check_parm_only_one(*values: "object") -> "None":
    """
    Check that at most one of multiple values is not None, when check fail, then throw error.

    Parameters
    ----------
    *values : object
        Check values.
    """

    none_count = 0
    for value in values:
        if value != None:
            none_count += 1
    if none_count > 1:
        try:
            vars_name = argname("values")
        except:
            vars_name = None
        if vars_name:
            vars_name_str = " " + " and ".join(["\"%s\"" % var_name for var_name in vars_name])
        else:
            vars_name_str = ""
        error_text = "at most one of parameters%s is not None" % vars_name_str
        error(error_text, ValueError)

def is_iterable(obj: "object", exclude_type: "list"=[str, bytes]) -> "bool":
    """
    Judge whether it is iterable.

    Parameters
    ----------
    obj : object
        Judge object.
    exclude_type : list [type, ...]
        Exclusion type.

    Returns
    -------
    bool
        Judgment result.
    """

    check_parm(exclude_type, list)

    obj_type = type(obj)
    if obj_type in exclude_type:
        return False
    try:
        obj_dir = obj.__dir__()
    except TypeError:
        return False
    if "__iter__" in obj_dir:
        return True
    else:
        return False

def is_number_str(text: "str", return_value: "bool"=False) -> "bool | int | float":
    """
    Judge whether it is number string.

    Parameters
    ----------
    text : str
        Judge text.
    return_value : bool
        Whether return value.
    
    Returns
    -------
    bool or int or float
        Judgment result or transformed value.
    """

    check_parm(text, str)
    check_parm(return_value, bool)

    try:
        if "." in text:
            number = float(text)
        else:
            number = int(text)
    except ValueError:
        return False
    if return_value:
        return number
    return True

def get_first_notnull(*values: "object", default: "object"=None, exclude: "list"=[]) -> object:
    """
    Get first notnull element.
    """

    check_parm(exclude, list)
    
    for value in values:
        if value not in [None, *exclude]:
            return value
    return default

def ins(obj: "object", *arrays: "iter") -> "bool":
    """
    Judge whether the object is in multiple array.

    Parameters
    ----------
    obj : object
        Judge object.
    *arrays : iterator
        Array.

    Returns
    -------
    bool
        Judge result.
    """

    check_parm(arrays, "_iterable", check_element=True)

    for array in arrays:
        if obj in array:
            return True
    return False

def mutual_in(*arrays: "iter") -> "bool":
    """
    Whether the same element exists in multiple array.

    Parameters
    ----------
    *arrays : iterator
        Array.

    Returns
    -------
    bool
        Judge result.
    """
    
    check_parm(arrays, "_iterable", check_element=True)
    
    arrays = list(arrays)
    for n, array in enumerate(arrays):
        for after_array in arrays[n+1:]:
            for element in array:
                if ins(element, after_array):
                    return True
    return False

def convert_type(obj: "object", to_type: "type", method: "Function | Method | type"=None) -> "object":
    """
    Convert object type.

    Parameters
    ----------
    obj : object
        Convert object.
    to_type : type
        Target type.
    method : Function or Method or type or None
        Convert method.

        - Function or Method or type : Use this method.
        - None : Use value of parameter to_type.
    
    Returns
    -------
    object
        Converted object.
    """

    check_parm(to_type, type)
    check_parm(method, Function, Method, type, None)

    if type(obj) == to_type:
        return obj
    if method != None:
        return method(obj)
    else:
        return to_type(obj)