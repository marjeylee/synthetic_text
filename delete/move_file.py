# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     move_file
   Description :
   Author :       'li'
   date：          2018/9/8
-------------------------------------------------
   Change Activity:
                   2018/9/8:
-------------------------------------------------
"""
import os
import shutil

from utility.file_path_utility import get_all_file_from_dir, get_all_files_under_directory

__author__ = 'li'

DELETE_PATH = 'G:/line/'
PARENT_DIR_PATH = 'D:/image/tmp/'
DES_PATH = 'G:/des/'


def get_key(all_paths):
    keys = set()
    for path in all_paths:
        _, name = os.path.split(path)
        key = name.split('.')[0]
        keys.add(key)
    return keys


def main():
    all_paths = get_all_files_under_directory(PARENT_DIR_PATH)
    delete_paths = get_all_files_under_directory(DELETE_PATH)
    all_keys = get_key(all_paths)
    delete_keys = get_key(delete_paths)
    index = 0
    for key in all_keys:
        if key not in delete_keys:
            print(key)
            shutil.copy(PARENT_DIR_PATH + key + '.jpg', DES_PATH + str(index) + '_' + key + '.jpg')
            index = index + 1


if __name__ == '__main__':
    main()
