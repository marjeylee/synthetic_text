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

PARENT_DIR_PATH = 'F:\dataset\seg/6'

DES_PATH = 'F:\dataset\seg\dup/'


def delete_6():
    for dirpath, dirnames, filenames in os.walk(PARENT_DIR_PATH):
        for d in dirnames:
            sub_dir = os.path.join(dirpath, d)
            files = get_all_file_from_dir(sub_dir)
            if len(files) >= 1:
                diractory = ''
                for f in files:
                    diractory, name = os.path.split(f)
                    des_p = os.path.join(DES_PATH, name)
                    shutil.move(f, des_p)
                    print(f)
                os.removedirs(diractory)


def main():
    delete_6()
    # delete_6()


if __name__ == '__main__':
    main()
