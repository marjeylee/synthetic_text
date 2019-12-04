# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       'li'
   date：          2018/9/8
-------------------------------------------------
   Change Activity:
                   2018/9/8:
-------------------------------------------------
"""
import os
import shutil
import uuid

from utility.file_path_utility import get_all_files_under_directory

__author__ = 'li'


def get_uuid_str():
    """
    generate uuid string of 40 size
    :return:
    """
    return str(uuid.uuid4()).replace('-', '')


def get_txt_mapping():
    with open('all.txt', mode='r', encoding='utf8') as file:
        lines = file.readlines()
        mapping = {}
        for line in lines:
            items = line.split('  ')
            assert len(items) > 0
            key = items[0]
            value = ''
            for i in range(1, len(items)):
                value = value + items[i] + ' '
            mapping[key] = value.strip()
    return mapping


def main():
    img_dir = 'C:/Users/lr/Desktop/txt_inage'
    img_paths = get_all_files_under_directory(img_dir)
    txt_mapping = get_txt_mapping()
    des_dir = 'C:/Users/lr/Desktop/genb/'
    for path in img_paths:
        _, name = os.path.split(path)
        name = name.split('_____')[0]
        if name not in txt_mapping:
            print(name)
            continue

        new_name = get_uuid_str()
        des_path = des_dir + new_name + '.jpg'
        shutil.copy(path, des_path)
        with open('result1.txt', mode='a', encoding='utf8') as file:
            line = new_name + ' ' + txt_mapping[name] + '\n'
            file.write(line)


if __name__ == '__main__':
    main()
