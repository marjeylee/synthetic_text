# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     file_io_utility
   Description :
   Author :       'li'
   date：          2018/8/3
-------------------------------------------------
   Change Activity:
                   2018/8/3:
-------------------------------------------------
"""


def read_all_content(file_path, encoding='utf8'):
    """
    read files content
    :param file_path:
    :param encoding:
    :return:
    """
    with open(file_path, mode='r', encoding=encoding) as file:
        lines = file.readlines()
        content = ''
        for line in lines:
            content = content + line
        return content
