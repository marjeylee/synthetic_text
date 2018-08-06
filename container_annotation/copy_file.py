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
import shutil
import uuid

from utility.file_path_utility import get_all_file_from_dir

"""
抽取所有图片到一个文件夹
"""
__author__ = 'li'

ORIGINAL_IMAGE_DIR_PATH = 'F:/dataset/第二次标注图片\original_image/'
NEW_IMAGE_DIR_PATH = 'F:/dataset/第二次标注图片/image/'


def get_all_image_path():
    """
    获得所有图片路径
    :return:
    """
    paths = get_all_file_from_dir(ORIGINAL_IMAGE_DIR_PATH)
    images_path = []
    for p in paths:
        if p.find('.jpg') > 0:
            images_path.append(p)
    return images_path


def copy_image(images_path):
    """
    copy images
    :param images_path:
    :return:
    """
    for p in images_path:
        file_name = p.split('\\')[-1].split('.')[0] + '.jpg'
        des_path = NEW_IMAGE_DIR_PATH + file_name
        shutil.copyfile(p, des_path)


def main():
    images_path = get_all_image_path()
    copy_image(images_path)
    pass


if __name__ == '__main__':
    main()
