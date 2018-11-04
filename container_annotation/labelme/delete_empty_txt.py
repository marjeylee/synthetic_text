# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     delete_empty_txt
   Description :
   Author :       'li'
   date：          2018/10/14
-------------------------------------------------
   Change Activity:
                   2018/10/14:
-------------------------------------------------
"""
import os

from utility.file_path_utility import get_all_file_from_dir

DIR_PATH = 'E:\dataset\detection/training_data/'
paths = get_all_file_from_dir(DIR_PATH)
for p in paths:
    is_delete = False
    if p.find('txt') > 0:
        with open(p, encoding='utf8', mode='r') as file:
            lines = file.readlines()

            if len(lines) == 0:
                is_delete = True
    if is_delete:
        _dir, name = os.path.split(p)
        new_name = name.replace('txt', 'jpg')
        try:
            os.remove(p)
            os.replace(DIR_PATH + name)
        except Exception as e:
            print(e)
