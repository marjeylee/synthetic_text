# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     move_useless_text
   Description :
   Author :       'li'
   date：          2018/11/5
-------------------------------------------------
   Change Activity:
                   2018/11/5:
-------------------------------------------------
"""
import os
import shutil

from utility.delete_file import delete_file_in_dir
from utility.file_path_utility import get_all_file_from_dir

__author__ = 'li'

PARENT_DIR_PATH = 'E:\dataset/text_area/valid\class/tocheck\des/4'

DES_PATH = 'E:\dataset/text_area/valid\class/tocheck\des/2/'


def delete_6():
    paths = get_all_file_from_dir(PARENT_DIR_PATH)
    for p in paths:
        _, name = os.path.split(p)
        label = name.split('-')[0]
        is_move = False
        for c in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
            if label.find(c) >= 0:
                is_move = True
                break
        if is_move:
            print(p)
            shutil.move(p, DES_PATH + name)


def move():
    for dirpath, dirnames, filenames in os.walk(PARENT_DIR_PATH):
        for d in dirnames:
            try:
                sub_dir = os.path.join(dirpath, d)
                files = get_all_file_from_dir(sub_dir)
                _, image_name = os.path.split(files[0])
                try:
                    if len(files) <= 4:
                        for p in files:
                            shutil.move(p, DES_PATH + image_name)
                            print('delete' + sub_dir)
                            continue
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)


def main():
    # delete_4()
    move()


if __name__ == '__main__':
    main()
