# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     copy_delete
   Description :
   Author :       'li'
   date：          2018/10/23
-------------------------------------------------
   Change Activity:
                   2018/10/23:
-------------------------------------------------
"""
import os
import shutil

from utility.file_path_utility import get_all_file_from_dir

ALL_PATH = 'C:/Users\lr\Desktop/traing_data/1'
DELETE_PATH = 'C:/Users\lr\Desktop\lines'


def get_mapping(files_path, file_type='jpg'):
    """
    get mapping
    :param files_path:
    :param file_type:
    :return:
    """
    mapping = {}
    files_path = get_all_file_from_dir(files_path)
    for p in files_path:
        if p.find(file_type) >= 0:
            _, name = os.path.split(p)
            mapping[name.split('.')[0]] = p
    return mapping


DES_PATH = 'C:/Users\lr\Desktop\des/'
all_map = get_mapping(ALL_PATH)
delete_map = get_mapping(DELETE_PATH).keys()
for p in all_map:
    if p not in delete_map:
        shutil.copy(all_map[p], DES_PATH + p + '.jpg')
