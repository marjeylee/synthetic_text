# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     rename_file
   Description :
   Author :       'li'
   date：          2018/8/30
-------------------------------------------------
   Change Activity:
                   2018/8/30:
-------------------------------------------------
"""
import os
import shutil
import uuid


def get_all_file_from_dir(path_dir):
    """
    遍历获得所有文件夹和子文件夹下的文件
    :param path_dir:
    :return:
    """
    file_path = []
    if os.path.exists(path_dir):
        path_dir = os.path.abspath(path_dir)
        for i in os.listdir(path_dir):
            path_i = os.path.join(path_dir, i)
            if os.path.isfile(path_i):
                file_path.append(path_i)
            else:
                file_path.extend(get_all_file_from_dir(path_i))
    return file_path


__author__ = 'li'
if __name__ == '__main__':
    path = 'C:/Users\lr\Desktop/to_check'
    des_dir_path = 'C:/Users\lr\Desktop/rename/'
    paths = get_all_file_from_dir(path)
    for p in paths:
        try:
            dir_path, name = os.path.split(p)
            label = name.split('-')[1].split('.')[0]
            if len(label) > 7:
                continue
            des_path = des_dir_path + label + '----' + str(uuid.uuid4()) + '.jpg'
            print(des_path)
            shutil.copyfile(p, des_path)
        except Exception as e:
            print(e)
