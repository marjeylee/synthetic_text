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

from container_annotation.copy_file import GetFileMd5
from utility.file_path_utility import get_all_files_under_directory, create_dir

SOURCE_DIR = 'I:\img\original'
DES_DIR = 'I:\img\md5/'


def __main():
    img_paths = get_all_files_under_directory(SOURCE_DIR)
    for index, path in enumerate(img_paths):
        if '.jpg' not in path:
            continue
        if index % 10 == 0:
            print(index)
        _, name = os.path.split(path)
        dir_name = name.split('_')[0]
        md5_name = GetFileMd5(path)
        des_path = DES_DIR + md5_name + '.jpg'
        shutil.copy(path, des_path)


if __name__ == '__main__':
    __main()
