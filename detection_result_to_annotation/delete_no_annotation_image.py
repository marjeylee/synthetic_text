# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     delete_no_annotation_image
   Description :
   Author :       'li'
   date：          2018/8/31
-------------------------------------------------
   Change Activity:
                   2018/8/31:
-------------------------------------------------
"""
import os

from utility.file_path_utility import get_all_file_from_dir

__author__ = 'li'
save_annotation_dir = 'F:\BaiduNetdiskDownload/annotation/'
images_path = 'F:\BaiduNetdiskDownload/uuid_image'


def load_map(path):
    paths = get_all_file_from_dir(path)
    map = {}
    for p in paths:
        dir_, name = os.path.split(p)
        key = name.split('.')[0]
        map[key] = p
    return map


if __name__ == '__main__':
    img_map = load_map(images_path)
    anns_map = load_map(save_annotation_dir)
    for k in img_map.keys():
        if k not in anns_map.keys():
            os.remove(img_map[k])
    pass
