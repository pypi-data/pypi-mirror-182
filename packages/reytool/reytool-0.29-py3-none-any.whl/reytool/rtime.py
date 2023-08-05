# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
══════════════════════════════
@Time    : 2022-12-05 14:11:50
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Rey's time methods
══════════════════════════════
"""


import time
import datetime
from pandas import DataFrame, concat as pd_concat

from .rbasic import error, check_parm, is_number_str
from .rtext import rprint
from .rregular import re_search


class RTMark():
    """
    Rey's time mark type.
    """

    # Mark record.
    record = []
    
    def __init__(self) -> "None":
        """
        Mark now time.
        """

        self.mark()
        
    def mark(self) -> "dict":
        """
        Mark now time and return mark time information.

        Returns
        -------
        dict {'index', 'timestamp', 'datetime', 'datetime_str', 'interval_timestamp', 'interval_timedelta', 'interval_timedelta_str'}
            Mark time information.
        """

        record_len = len(self.record)
        mark_info = {
            "index": record_len,
            "timestamp": now("timestamp"),
            "datetime": now("datetime"),
            "datetime_str": now(),
        }
        if record_len == 0:
            mark_info["interval_timestamp"] = None
            mark_info["interval_timedelta"] = None
            mark_info["interval_timedelta_str"] = None
        else:
            last_datetime = self.record[-1]["datetime"]
            last_timestamp = self.record[-1]["timestamp"]
            mark_info["interval_timestamp"] = mark_info["timestamp"] - last_timestamp
            mark_info["interval_timedelta"] = mark_info["datetime"] - last_datetime
            mark_info["interval_timedelta_str"] = time_to_str(mark_info["interval_timedelta"])
        self.record.append(mark_info)
        return mark_info

    def report(self) -> "DataFrame":
        """
        Print and return mark time information.

        Returns
        -------
        DataFrame object
            Mark time information, object from pandas package.
        """

        data = [
            {
                "timestamp": round(row["timestamp"], 1),
                "datetime": row["datetime_str"],
                "interval": row["interval_timedelta_str"]
            }
            for row in self.record
        ]
        report_df = DataFrame(data)
        interval_timedelta = self.record[-1]["datetime"] - self.record[0]["datetime"]
        interval = time_to_str(interval_timedelta)
        sum_df = DataFrame({"interval": interval}, index=["sum"])
        report_df = pd_concat([report_df, sum_df])
        report_df.fillna("-", inplace=True)
        title = "Time Mark"
        rprint(report_df, title=title)
        return report_df
        
def now(
    format: "str"="datetime_str"
) -> "str | int | datetime.datetime | datetime.date | datetime.time":
    """
    Get current time string or intger or object.

    Parameters
    ----------
    format : str {'datetime', 'date', 'time', 'datetime_str', 'date_str', 'time_str', 'timestamp', 'timestamp_int'}
        Format type.

        - 'datetime' : Return datetime object of datetime package.
        - 'date' : Return date object of datetime package.
        - 'time' : Return time object of datetime package.
        - 'datetime_str' : Return string in format '%Y-%m-%d %H:%M:%S'.
        - 'date_str' : Return string in format '%Y-%m-%d'.
        - 'time_str' : Return string in foramt '%H:%M:%S'.
        - 'timestamp' : Return time stamp.
        - 'timestamp_int' : Return time stamp of ten digit length.

    Returns
    -------
    str or int or datetime object or date object or time object
        Object of datetime package.
    """

    check_parm(format, "datetime", "date", "time", "datetime_str", "date_str", "time_str", "timestamp")

    if format == "datetime":
        return datetime.datetime.now()
    elif format == "date":
        return datetime.datetime.now().date()
    elif format == "time":
        return datetime.datetime.now().time()
    elif format == "datetime_str":
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elif format == "date_str":
        return datetime.datetime.now().strftime("%Y-%m-%d")
    elif format == "time_str":
        return datetime.datetime.now().strftime("%H:%M:%S")
    elif format == "timestamp":
        return time.time()
    elif format == "timestamp_int":
        return int(time.time())

def time_to_str(
        time_obj: "datetime.datetime | datetime.date | datetime.time | datetime.timedelta",
        format_str: "str"=None,
        throw_error: "bool"=False
    ) -> "str | object":
    """
    Format time object of datetime package as string

    Parameters
    ----------
    time_obj : datetime.datetime or datetime.date or datetime.time or datetime.timedelta
        Of datetime package.
    format_str : str or None
        Format string.

        - None : Automatic by type.
            * : When parameter time_obj is datetime.datetime, then format is '%Y-%m-%d %H:%M:%S'.
            * : When parameter time_obj is datetime.date, then format is '%Y-%m-%d'.
            * : When parameter time_obj is datetime.time, then format is '%H:%M:%S'.
            * : When parameter time_obj is datetime.timedelta, then format is 'days %H:%M:%S'.
        - str : Format by str.

    throw_error : bool
        Whether throw error, when parameter time_obj value error, otherwise return original value.

    Returns
    -------
    str or object
        String after foramt or original value.
    """

    check_parm(format_str, str, None)
    check_parm(throw_error, bool)
    if throw_error:
        check_parm(time_obj, datetime.datetime, datetime.date, datetime.time, datetime.timedelta)

    obj_type = type(time_obj)
    if obj_type == datetime.datetime:
        if format_str == None:
            string = str(time_obj)[:19]
        else:
            string = time_obj.strftime(format_str)
    elif obj_type == datetime.date:
        if format_str == None:
            string = str(time_obj)[:10]
        else:
            string = time_obj.strftime(format_str)
    elif obj_type == datetime.time:
        if format_str == None:
            string = str(time_obj)[:8]
        else:
            string = time_obj.strftime(format_str)
    elif obj_type == datetime.timedelta:
        if format_str == None:
            string = str(time_obj)
            if "day" in string:
                day, char, string = string.split(" ")
            else:
                day = "0"
            if string[1] == ":":
                string = "0" + string
            string = "%s %s" % (day, string[:8])
        else:
            seconds = time_obj.seconds
            time_obj = time.gmtime(seconds)
            string = time.strftime(format_str, time_obj)
    else:
        return time_obj
    return string

def str_to_time(
        string: "str",
        to_type: "str"=None,
        format_str: "str"=None,
        throw_error=False
    ) -> "datetime.datetime | datetime.date | datetime.time | datetime.timedelta | int | object":
    """
    Format string as time object of datetime package

    Parameters
    ----------
    string : str
    to_type : str {'datetime', 'date', 'time', 'datedelata', 'timestamp'} or None
        Format type.

        - 'datetime' : Return datetime object of datetime package.
        - 'date' : Return date object of datetime package.
        - 'time' : Return time object of datetime package.
        - 'timedelta' : Return timedelta object of datetime package.
        - 'timestamp' : Return time stamp of ten digit length.
        - None : Automatic judgment.

    format_str : str or None
        Format string.

        - None : Default format method.
            * When parameter to_type is 'datetime', then format string is '%Y-%m-%d %H:%M:%S'.
            * When parameter to_type is 'date', then format string is '%Y-%m-%d'.
            * When parameter to_type is 'time', then format string is '%H:%M:%S'.
            * When parameter to_type is 'timedelta', then format string is 'days %H:%M:%S'.
            * When parameter to_type is 'timestamp', then format string is '%Y-%m-%d %H:%M:%S'.
            * When parameter to_type is None, then automatic judgment.
        - str : Format by str.

    throw_error : bool
        Whether throw error, when parameter time_obj value error, otherwise return original value.

    Returns
    -------
    datetime.datetime or datetime.date or datetime.time or datetime.timedelta or int or object.
        Time object of datetime package or time stamp or original value.
    """

    check_parm(string, str)
    check_parm(to_type, "datetime", "date", "time", "timedelta", "timestamp", None)
    check_parm(format_str, str, None)
    check_parm(throw_error, bool)

    if to_type == None:
        str_len = len(string)
        if " " in string and "-" not in string:
            format_str = "%H:%M:%S"
            to_type = "timedelta"
        elif str_len == 19:
            format_str = "%Y-%m-%d %H:%M:%S"
            to_type = "datetime"
        elif str_len == 14:
            format_str = "%Y%m%d%H%M%S"
            to_type = "datetime"
        elif str_len == 10:
            format_str = "%Y-%m-%d"
            to_type = "date"
        elif str_len == 8:
            if string[2] == ":":
                format_str = "%H:%M:%S"
                to_type = "time"
            else:
                format_str = "%Y%m%d"
                to_type = "date"
        elif str_len == 6:
            format_str = "%H%M%S"
            to_type = "time"
        elif str_len == 4:
            format_str = "%Y"
            to_type = "date"
        else:
            return string
    elif to_type in ["datetime", "date", "time", "timestamp"]:
        if format_str == None:
            format_dir = {
                "datetime": "%Y-%m-%d %H:%M:%S",
                "date": "%Y-%m-%d",
                "time": "%H:%M:%S",
                "timestamp": "%Y-%m-%d %H:%M:%S"
            }
            format_str = format_dir[to_type]
    elif to_type == "timedelta":
        if format_str == None:
            format_str = "%H:%M:%S"
    if to_type == "timedelta":
        if " " in string:
            strings = string.split(" ")
            day_str, time_str = strings[0], strings[-1]
        else:
            day = "0"
        try:
            day = int(day_str)
        except ValueError:
            if throw_error:
                error("failed to format string as time object")
            return string
    try:
        time_obj = datetime.datetime.strptime(time_str, format_str)
    except ValueError:
        if throw_error:
            error("failed to format string as time object")
        return string
    if to_type == "date":
        time_obj = time_obj.date()
    elif to_type == "time":
        time_obj = time_obj.time()
    elif to_type == "timestamp":
        time_obj = int(time_obj.timestamp())
    elif to_type == "timedelta":
        second = time_obj.second
        second += day * 86400
        time_obj = datetime.timedelta(seconds=second)
    return time_obj

def is_sql_time(content: "str | int", return_value: "bool"=False) -> "bool | tuple":
    """
    Judge whether it conforms to SQL time format.

    Parameters
    ----------
    content : str or int
        Judge object.
    return_value : bool
        Whether return value.
    
    Returns
    -------
    bool or tuple [int, ...] with length of 6
        Judgment result or transformed values.
    """

    check_parm(content, str, int)

    content_type = type(content)
    if content_type == str:
        content_len = len(content)
        if content_len < 5:
            return False
        if is_number_str(content[4]):
            if content_len == 8:
                datetimes_str = [content[0:4], content[4:6], content[6:8], None, None, None]
            else:
                pattern = "^(\d{2}|\d{4})(\d{2})(\d{1,2})(\d{0,2})(\d{0,2})(\d{0,2})$"
                result = re_search(pattern, content)
                datetimes_str = list(result)
        else:
            pattern = "^(\d{2}|\d{4})[\W_](\d{2})[\W_](\d{2})[\W_]?(\d{2})?[\W_]?(\d{2})?[\W_]?(\d{2})?$"
            result = re_search(pattern, content)
            datetimes_str = list(result)
    elif content_type == int:
        content = str(content)
        content_len = len(content)
        if content_len < 3:
            return False
        elif content_len <= 8:
            pattern = r"^(\d{0,4}?)(\d{1,2}?)(\d{2})$"
            result = re_search(pattern, content)
            datetimes_str = list(result)
            datetimes_str += [None, None, None]
        else:
            pattern = r"^(\d{0,4}?)(\d{1,2})(\d{2})(\d{2})(\d{2})(\d{2})$"
            result = re_search(pattern, content)
            datetimes_str = list(result)
    year_len = len(datetimes_str[0])
    datetimes_str[0] = "2000"[0:4-year_len] + datetimes_str[0]
    try:
        year, month, day, hour, minute, second = [
            0 if int_str in ["", None] else int(int_str)
            for int_str in datetimes_str
        ]
        datetime.datetime(year, month, day, hour, minute, second)
        if return_value:
            return year, month, day, hour, minute, second
        return True
    except ValueError:
        pass
    return False