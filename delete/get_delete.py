# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     get_delete
   Description :
   Author :       'li'
   date：          2018/11/7
-------------------------------------------------
   Change Activity:
                   2018/11/7:
-------------------------------------------------
"""
import os
import shutil

from utility.file_path_utility import get_all_file_from_dir

p2 = 'C:/Users/lr/Desktop/new/dele/'
p1 = 'C:/Users/lr/Desktop/new/wrong/'  # all
left = 'C:/Users/lr/Desktop/new/left/'
org_dir = 'C:/Users/lr/Desktop/new/wrong/'


def get_mapping(files_path, file_type='jpg'):
    """
    get mapping
    :param files_path:
    :param file_type:
    :return:D
    """
    mapping = {}
    files_path = get_all_file_from_dir(files_path)
    for p in files_path:
        if p.find(file_type) >= 0:
            _, name = os.path.split(p)
            mapping[name.split('.')[0]] = p
    return mapping


def main():
    p1_paths = get_mapping(p1)
    p2_paths = get_mapping(p2)
    p1_keys = set(p1_paths.keys())
    p2_keys = set(p2_paths.keys())
    name_json = []
    for name in p1_keys:
        try:
            if name in p2_keys:
                continue
            path = p1_paths[name]
            _, name = os.path.split(path)
            name_json.append(name)
            des_path = left + name
            org_path = org_dir + name
            shutil.copy(org_path, des_path)
        except Exception as e:
            print(e)
    print(name_json)


if __name__ == '__main__':
    main()
