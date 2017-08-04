#!/usr/bin/env python3

from typing import Tuple


def formatter(cmd: str, k: str, v: str or dict or list) -> str:
    def dict_format(data: dict) -> Tuple[int, str]:
        arg_num = len(data) * 2
        data_list = []
        for k, v in data.items():
            i = f"${len(k)}\r\n{k}\r\n${len(str(v))}\r\n{str(v)}\r\n"
            data_list.append(i)
        data_str = "".join(data_list)
        return tuple([arg_num, data_str])
    
    x = "\r\n"
    arg_num = 2

    if type(v) == dict:
        i, v = dict_format(v)
        arg_num += i
    elif type(v) == list:
        a = ""
        for val in v:
            i, v = dict_format(val)
            a += v
            arg_num += i
        v = a
    else:
        v = f"${len(str(v))}{x}{str(v)}{x}"
        arg_num += 1
        
    return f"*{str(arg_num)}{x}${len(cmd)}{x}{cmd}{x}${len(k)}{x}{k}{x}{v}"
    