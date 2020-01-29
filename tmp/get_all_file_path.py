# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     get_all_file_path
   Description :
   Author :       'li'
   date：          2020/1/18
-------------------------------------------------
   Change Activity:
                   2020/1/18:
-------------------------------------------------
"""
from utility.file_path_utility import get_all_files_under_directory

img_dir = 'J:/car_door/to_class'
paths = get_all_files_under_directory(img_dir)
for path in paths:
    with open('all.txt', mode='a', encoding='utf8') as file:
        file.write(path + '\n')
