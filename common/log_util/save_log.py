#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 8:30
# @Author  : lr
# @Site    : 
# @File    : save_log.py
# @Software: PyCharm
import datetime

from common.utility import combine_file_path
from common.utility.file_path_utility import create_dir

LOG_DIR = combine_file_path('log/')
create_dir(LOG_DIR)
LOG_PATH = LOG_DIR = combine_file_path('log/log.log')


def get_current_time():
    """
    get current time
    :return:
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def __save_log_to_file(log_content):
    """
    save log to file
    :param log_content:
    :return:
    """
    with open(LOG_PATH, mode='a', encoding='utf8') as file:
        file.write(log_content + '\n')


def save_log(content, level='INFO'):
    """
    save log
    :param content:
    :param level: info  launch error
    :return:
    """
    current_time = get_current_time()
    log_content = current_time + ' [' + level + '] ' + content
    __save_log_to_file(log_content)
    print(log_content)


def main():
    log_info = 'dsadsad'
    level = 'INFO'
    save_log(content=log_info, level=level)


if __name__ == '__main__':
    main()
