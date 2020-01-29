# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mp2
   Description :
   Author :       'li'
   date：          2020/1/8
-------------------------------------------------
   Change Activity:
                   2020/1/8:
-------------------------------------------------
"""
import os
import shutil

from utility.file_path_utility import get_all_files_under_directory

names = set()
with open('name.txt', mode='r', encoding='utf8') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if len(line) > 1:
            names.add(line)

image_dir = 'J:/dangerous_mark/tocheck/dele/no/'
des_dir = 'C:/Users/lr/Desktop/tolael/'
image_paths = get_all_files_under_directory(image_dir)
for path in image_paths:
    _, name = os.path.split(path)
    name = name.replace('.jpg', '')
    if name not in names:
        print(name)
        shutil.copy(path, des_dir + name + '.jpg')
