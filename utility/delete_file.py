# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     delete_file
   Description :
   Author :       'li'
   date：          2018/8/19
-------------------------------------------------
   Change Activity:
                   2018/8/19:
-------------------------------------------------
"""
import os

from utility.file_path_utility import get_all_file_from_dir

__author__ = 'li'


def delete_file_in_dir(dir_path):
    paths = get_all_file_from_dir(dir_path)
    for p in paths:
        try:
            os.remove(p)
        except Exception as  e:
            print(e)


if __name__ == '__main__':
    dir_path = 'C:/Users\mar\Desktop\ocr'
    delete_file_in_dir(dir_path)
