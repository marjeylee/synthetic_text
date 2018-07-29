# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     load_training_data
   Description :
   Author :       'li'
   date：          2018/7/24
-------------------------------------------------
   Change Activity:
                   2018/7/24:
-------------------------------------------------
"""
from config import GENERATE_DIE_PATH
from utility.file_path_utility import get_all_file_from_dir

__author__ = 'li'

training_data_path = GENERATE_DIE_PATH + '/training_data/'
file_paths = get_all_file_from_dir(training_data_path)

for path in file_paths:
    str_arr = path.split('\\')
    file_name = str_arr[-1].split('.')[0]

    print(path)
