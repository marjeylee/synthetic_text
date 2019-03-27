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
import os
import shutil

from utility.file_path_utility import get_all_file_from_dir

dir_path = 'E:\dataset\\11-25\horizontal/'
des_path = 'C:\\Users\lr\Desktop\small/'
paths = get_all_file_from_dir(dir_path)
for path in paths:
    size = os.path.getsize(path)
    if size < 700:
        print(path)
        _, file_name = os.path.split(path)
        shutil.move(path, des_path + file_name)
