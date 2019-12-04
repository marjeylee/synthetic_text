# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     copy_file
   Description :
   Author :       'li'
   date：          2018/11/11
-------------------------------------------------
   Change Activity:
                   2018/11/11:
-------------------------------------------------
"""
import os
import shutil

from chinese_project.move_file.rename_file_md5 import GetFileMd5


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


ori_path = 'D:/image/container_door/'
des_path = 'D:/image/sort_img/'
all_paths = get_all_file_from_dir(ori_path)
if __name__ == '__main__':
    for index, p in enumerate(all_paths):
        if index % 100 == 0:
            print(p)
        if '.jpg' not in p:
            continue
        md5_name = GetFileMd5(p)
        file_name = str(index) + '_' + md5_name + '.jpg'
        shutil.copy(p, des_path + file_name)
        # label = file_name.split('-')[0]
        # if label.find('bg') >= 0 and label.find('jpg') >= 0:
        #     print(p)
        #     shutil.move(p, des_path + file_name)
