# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     six_image_move
   Description :
   Author :       'li'
   date：          2018/9/23
-------------------------------------------------
   Change Activity:
                   2018/9/23:
-------------------------------------------------
"""
import os
import shutil

from utility.delete_file import delete_file_in_dir
from utility.file_path_utility import get_all_file_from_dir

__author__ = 'li'

PARENT_DIR_PATH = 'E:\dataset/new_seg/6/'
DES_DIR_PATH = 'E:\dataset\six_uncheck/'
for dirpath, dirnames, filenames in os.walk(PARENT_DIR_PATH):
    for d in dirnames:
        sub_dir = os.path.join(dirpath, d)

        files = get_all_file_from_dir(sub_dir)
        if len(files) <= 2:
            for f in files:
                dir_p, name = os.path.split(f)
                print(f)
                shutil.move(f, DES_DIR_PATH + name)
