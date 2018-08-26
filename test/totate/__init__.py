# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       'li'
   date：          2018/8/6
-------------------------------------------------
   Change Activity:
                   2018/8/6:
-------------------------------------------------
"""
import shutil

from utility.file_path_utility import get_all_file_from_dir

__author__ = 'li'

dir_path = 'C:/Users/mar/Desktop/predict/'
des_path = 'C:/Users/mar/Desktop/tmp/'
paths = get_all_file_from_dir(dir_path)
for path in paths:
    name = path.split('\\')[-1].split('-')[0]
    if len(name) == 2:
        new_path = path.replace('predict', 'tmp')
        shutil.move(path, new_path)
