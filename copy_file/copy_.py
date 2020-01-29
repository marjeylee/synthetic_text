# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     copy_
   Description :
   Author :       'li'
   date：          2020/1/7
-------------------------------------------------
   Change Activity:
                   2020/1/7:
-------------------------------------------------
"""
import os
import shutil

from utility.file_path_utility import get_all_files_under_directory, create_dir

SOURCE_DIR = 'J:/dangerous_mark/waier'
DES_DIR = 'J:/dangerous_mark/wai_er_dir/'


def __main():
    img_paths = get_all_files_under_directory(SOURCE_DIR)
    for index, path in enumerate(img_paths):
        if index % 10 == 0:
            print(index)
        _, name = os.path.split(path)
        dir_name = name.split('_')[0]
        des_dir = DES_DIR + str(dir_name) + '/'
        create_dir(des_dir)
        des_path = des_dir + name
        shutil.copy(path, des_path)


if __name__ == '__main__':
    __main()
