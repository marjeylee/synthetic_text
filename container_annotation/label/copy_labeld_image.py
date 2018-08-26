# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     copy_labeld_image
   Description :
   Author :       'li'
   date：          2018/8/18
-------------------------------------------------
   Change Activity:
                   2018/8/18:
-------------------------------------------------
"""
import os
import shutil

from utility.file_path_utility import get_all_file_from_dir

__author__ = 'li'
ORIGINAL_IMAGE_DIR = 'F:/dataset/all_image/original_data/'
DES_DIR = 'F:/dataset/all_image/image/'
LABEL_DIR = 'F:/dataset/all_image/annotation/'


def load_image_info(dir):
    """
    load image info
    :return:
    """

    image_paths = get_all_file_from_dir(dir)
    image_map = {}
    for p in image_paths:
        name = p.split('\\')[-1].split('.')[0]
        image_map[name] = p
    return image_map


def main():
    image_map = load_image_info(ORIGINAL_IMAGE_DIR)
    txt_map = load_image_info(LABEL_DIR)
    label_keys = txt_map.keys()
    for k in label_keys:
        print(k)
        txt_path = txt_map[k]
        file_size = os.path.getsize(txt_path)
        if file_size <= 0:
            continue
        if k not in image_map.keys():
            continue
        img_path = image_map[k]
        shutil.copyfile(img_path, DES_DIR + k + '.jpg')
        print(img_path)


if __name__ == '__main__':
    main()
