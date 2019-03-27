# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     extract_file
   Description :
   Author :       'li'
   date：          2018/7/29
-------------------------------------------------
   Change Activity:
                   2018/7/29:
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


"""
抽取所有图片到一个文件夹
"""
__author__ = 'li'

ORIGINAL_IMAGE_DIR_PATH = '/data/data/json/new_xiangzu/'
NEW_IMAGE_DIR_PATH = '/data/data/json/new_xiangzu/'


def get_all_image_path():
    """
    获得所有图片路径
    :return:
    """
    paths = get_all_file_from_dir(ORIGINAL_IMAGE_DIR_PATH)
    images_path = []
    for p in paths:
        # if p.find('.png') > 0 and p.find('outp') >= 0:
        images_path.append(p)
    return images_path


def copy_image(images_path):
    """
    copy imagesr
    :param images_path:
    :return:
    """
    for index, p in enumerate(images_path):
        print(index)
        new_path = NEW_IMAGE_DIR_PATH + 'xiangzu-' + str(uuid.uuid4()) + '.npy'
        shutil.move(p, new_path)
        # _, file_name = os.path.split(p)
        # if 'jpg' not in file_name:
        #     continue
        # img = cv2.imread(p)
        # print(p)
        # shape = img.shape
        # if shape[0] == 1080 and shape[1] == 1920:
        #     print(index)
        #     des_path = NEW_IMAGE_DIR_PATH + str(index) + '--' + str(uuid.uuid4()) + '.jpg'
        #     shutil.copy(p, des_path)


def main():
    images_path = get_all_image_path()
    copy_image(images_path)
    pass


if __name__ == '__main__':
    main()
