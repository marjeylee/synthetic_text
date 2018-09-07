# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     extract_text_label
   Description :
   Author :       'li'
   date：          2018/7/29
-------------------------------------------------
   Change Activity:
                   2018/7/29:
-------------------------------------------------
"""
import os
import uuid

import cv2

from container_annotation.label.parse_annotation_info import load_annotation_info
from utility import show_img
from utility.file_path_utility import get_all_file_from_dir
from utility.image_utility import save_img

__author__ = 'li'
"""
extract text area
"""
LABEL_DIR = 'F:\BaiduNetdiskDownload\label_txt/'
IMAGE_PATH = 'F:\BaiduNetdiskDownload/uuid_image/'
TEXT_AREA_DIR_PATH = 'F:\BaiduNetdiskDownload/text_area/'


def load_image_info():
    """
    load image info
    :return:
    """
    image_paths = get_all_file_from_dir(IMAGE_PATH)
    image_map = {}
    for p in image_paths:
        name = p.split('\\')[-1]
        image_map[name] = p
    return image_paths


def clip_label_image(annotation_info, image_map):
    """
    clip text area
    :param annotation_info:
    :param image_map:
    :return:
    """
    for name in annotation_info.keys():
        info = annotation_info[name]
        if len(info) < 1:
            continue
        image_path = IMAGE_PATH + name + '.jpg'
        if not os.path.exists(image_path):
            continue
        original_image = cv2.imread(image_path)
        for r in info:
            try:
                label = r['label'].replace('\n', '').replace('@', '#').replace(' ', '#')
                print(label)
                p1 = r['p1']
                p2 = r['p2']
                text_area = original_image[int(p1[0]):int(p2[0]), int(p1[1]):int(p2[1]), :]
                path = TEXT_AREA_DIR_PATH + label + '-' + str(uuid.uuid4()) + '.jpg'
                save_img(text_area, path)
                print(label)
            except Exception as e:
                print(e)


def load_seg_info():
    txt_paths = get_all_file_from_dir(LABEL_DIR)
    seg_info = {}
    for p in txt_paths:
        name = p.split('\\')[-1].split('.')[0]
        region = []
        with open(p, mode='r', encoding='utf8') as file:
            lines = file.readlines()
            for line in lines:
                if len(line) > 5:
                    columns = line.split(',')
                    obj = {'p1': [columns[1], columns[0]], 'p2': [columns[5], columns[4]]
                        , 'label': columns[8]}
                    region.append(obj)
        if len(region) > 0:
            seg_info[name] = region
    return seg_info


def main():
    seg_info = load_seg_info()
    image_map = load_image_info()
    clip_label_image(seg_info, image_map)


if __name__ == '__main__':
    main()
