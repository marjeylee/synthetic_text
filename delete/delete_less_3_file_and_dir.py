# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     delete_less_3_file_and_dir
   Description :
   Author :       'li'
   date：          2018/9/8
-------------------------------------------------
   Change Activity:
                   2018/9/8:
-------------------------------------------------
"""
import os

from utility.delete_file import delete_file_in_dir
from utility.file_path_utility import get_all_file_from_dir

__author__ = 'li'

PARENT_DIR_PATH = 'C:/Users\lr\Desktop\class/6'


def delete_4():
    for dirpath, dirnames, filenames in os.walk(PARENT_DIR_PATH):
        for d in dirnames:
            sub_dir = os.path.join(dirpath, d)

            files = get_all_file_from_dir(sub_dir)
            if len(files) <= 2:
                delete_file_in_dir(sub_dir)
                print('delete' + sub_dir)
                continue
            # _, image_name = os.path.split(files[0])
            # label = image_name.split('-')[-1].split('.')[0]
            #
            # if len(files) <= 3 and label.isdigit():
            #     delete_file_in_dir(sub_dir)
            #     print('delete' + sub_dir)
            #     continue
            #
            # if len(files) <= 3 and 'A' <= label[0] <= 'Z' and '0' <= label[2] <= '9':
            #     delete_file_in_dir(sub_dir)
            #     print('delete' + sub_dir)
            #     continue
            # if len(files) <= 3 and '0' <= label[0] <= '9' and '0' <= label[1] <= '9':
            #     delete_file_in_dir(sub_dir)
            #     print('delete' + sub_dir)
            #     continue


def delete_6():
    for dirpath, dirnames, filenames in os.walk(PARENT_DIR_PATH):
        for d in dirnames:
            sub_dir = os.path.join(dirpath, d)
            files = get_all_file_from_dir(sub_dir)
            if len(files) == 0:
                delete_file_in_dir(sub_dir)
                print('delete' + sub_dir)
                continue
            _, image_name = os.path.split(files[0])
            is_delete = False
            for c in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
                if image_name.find(c) >= 0:
                    is_delete = True
                    break
            if len(files) > 2:
                delete_file_in_dir(sub_dir)
                print('delete' + sub_dir)
                continue
            if is_delete:
                if len(files) == 1:
                    print('delete' + sub_dir)
                    delete_file_in_dir(sub_dir)


def main():
    # delete_4()
    delete_6()


if __name__ == '__main__':
    main()
