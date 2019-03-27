# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     gen_t
   Description :
   Author :       'li'
   date：          2018/12/19
-------------------------------------------------
   Change Activity:
                   2018/12/19:
-------------------------------------------------
"""
import os

from utility.file_path_utility import get_all_files_under_directory

image_dir = 'C:\\Users\lr\Desktop\lb\label_no_color'
paths = get_all_files_under_directory(image_dir)
with open('train.txt', mode='a', encoding='utf8')as file:
    for p in paths:
        name = os.path.split(p)[1].split('.')[0]
        print(name)
        file.write(name + '\n')
