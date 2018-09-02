# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     upload_set_img
   Description :
   Author :       'li'
   date：          2018/8/31
-------------------------------------------------
   Change Activity:
                   2018/8/31:
-------------------------------------------------
"""
import os
import shutil

from utility.file_path_utility import get_all_file_from_dir, create_dir

__author__ = 'li'

upload_path = 'F:/BaiduNetdiskDownload/upload/'
annotation_path = 'F:\BaiduNetdiskDownload/annotation'
img_path = 'F:\BaiduNetdiskDownload/uuid_image'


def load_map(path):
    paths = get_all_file_from_dir(path)
    map = {}
    for p in paths:
        dir_, name = os.path.split(p)
        key = name.split('.')[0]
        map[key] = p
    return map


img_map = load_map(img_path)
anns_map = load_map(annotation_path)
for k in img_map.keys():
    dir_name = upload_path + str(k[0])
    img_dir = dir_name + '/img/'
    ann_dir = dir_name + '/ann/'
    create_dir(img_dir)
    create_dir(ann_dir)
    if k in anns_map.keys():
        shutil.copy(img_map[k], img_dir + str(k) + '.jpg')
        shutil.copy(anns_map[k], ann_dir + str(k) + '.xml')

pass
