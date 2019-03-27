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

from utility.file_path_utility import get_all_file_from_dir

__author__ = 'li'

PARENT_DIR_PATH = 'E:\dataset\\11-28\horizontal\p321'

DES_PATH = 'E:\dataset\\11-28\horizontal\\true/'


def delete_6():
    files = get_all_file_from_dir(PARENT_DIR_PATH)
    for path in files:
        _, file_name = os.path.split(path)
        ls = file_name.split('-')
        tr_label = ls[0]
        label = ls[1]
        re_label = tr_label.replace('O', '0')
        if re_label == label:
            shutil.move(path, DES_PATH + file_name)


def main():
    delete_6()
    # delete_6()


if __name__ == '__main__':
    main()
