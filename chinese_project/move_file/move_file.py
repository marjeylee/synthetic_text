#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 7:26
# @Author  : lr
# @Site    : 
# @File    : move_file.py
# @Software: PyCharm
import os
import shutil
import uuid

from utility.file_path_utility import get_all_file_from_dir

TXT_PATH = 'G:/dataset/data_train.txt'
IMG_DIR = 'G:/dataset/images/'
DES_DIR = 'G:/dataset/des_image/'


def get_image_mapping():
    """
    load txt file ,get file mapping
    :return:
    """
    mapping = {}
    with open(TXT_PATH, mode='r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if index % 1000 == 0:
                print(index)
            rows = line.split(' ')
            key = rows[0]
            value = ''
            for row in rows[1:]:
                value = value + str(row).replace('/n', '') + '_'
            value = value[:-1]
            mapping[key] = value
    return mapping


def get_file_mapping(files_path, file_type='jpg'):
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


def copy_file_to_des(IMG_DIR, content_mapping):
    """
    copy file
    :param IMG_DIR:

    :param content_mapping:
    :return:
    """
    keys = content_mapping.keys()
    if os.path.exists(IMG_DIR):
        path_dir = os.path.abspath(IMG_DIR)
        file_list = os.listdir(path_dir)
        length = len(file_list)
        for index, file in enumerate(file_list):
            if index % 1000 == 0:
                print(str(index * 1.0 / length))
            if file in keys:
                value = content_mapping[file].replace('\n', '') + '###' + str(uuid.uuid4()) + '.jpg'
                shutil.copy(IMG_DIR + file, DES_DIR + value)


def main():
    content_mapping = get_image_mapping()
    copy_file_to_des(IMG_DIR, content_mapping)
    pass


if __name__ == '__main__':
    main()
