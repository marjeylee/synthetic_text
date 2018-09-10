# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     delete_file
   Description :
   Author :       'li'
   date：          2018/8/19
-------------------------------------------------
   Change Activity:
                   2018/8/19:
-------------------------------------------------
"""
import os

from utility.file_path_utility import get_all_file_from_dir

__author__ = 'li'


def delete_file_in_dir(dir_path):
    paths = get_all_file_from_dir(dir_path)
    for p in paths:
        if p.find('DMG') >= 0:
            try:
                os.remove(p)
            except Exception as  e:
                print(e)
    os.removedirs(dir_path)


if __name__ == '__main__':
    dir_path = 'E:\BaiduNetdiskDownload\h122_08/'
    delete_file_in_dir(dir_path)
