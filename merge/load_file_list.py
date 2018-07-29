# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     load_file_list
   Description :
   Author :       'li'
   date：          2018/7/24
-------------------------------------------------
   Change Activity:
                   2018/7/24:
-------------------------------------------------
"""
from config import BACKGROUND_DIR_PATH, TEXT_TEMPLATE_DIR_PATH
from utility.file_path_utility import get_all_file_from_dir

__author__ = 'li'
print("开始加载文件列表")
bg_file_path = get_all_file_from_dir(BACKGROUND_DIR_PATH)
text_template_path = get_all_file_from_dir(TEXT_TEMPLATE_DIR_PATH)
print("文件列表加载完成")
with open('./gb_list.txt', 'w', encoding='utf8')as file:
    for bg_path in bg_file_path:
        file.write(bg_path + '\n')
with open('./template_list.txt', 'w', encoding='utf8')as file:
    for template in text_template_path:
        file.write(template + '\n')
