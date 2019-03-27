# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     delete_chinese_char
   Description :
   Author :       'li'
   date：          2018/12/29
-------------------------------------------------
   Change Activity:
                   2018/12/29:
-------------------------------------------------
"""
import uuid

from utility.file_path_utility import get_all_files_under_directory

des_path = 'C:/Users\lr\Desktop\dd/'
files = get_all_files_under_directory('D:\dataset\\xiangzu')
for json_file in files:
    with open(json_file, mode='r', encoding='ansi') as file:
        lines = file.readlines()
        new_lines = []
        for l in lines:
            if 'imagePath' not in l:
                new_lines.append(l)
        with open(des_path + str(uuid.uuid1()) + '.json', mode='a', encoding='utf8') as des_file:
            for l in new_lines:
                des_file.write(l + '\n')
