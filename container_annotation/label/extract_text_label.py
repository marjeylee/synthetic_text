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
ANNOTATION_PATH = 'F:/dataset/container_dataset/annotation'
IMAGE_PATH = 'F:/dataset/container_dataset/image/'
TEXT_AREA_DIR_PATH = 'F:/dataset/container_dataset/text_area/'


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
    for info in annotation_info:
        name = info['image_name']
        if 'region' not in info.keys():
            continue
        region = info['region']
        if region is None or len(region) == 0:
            continue
        image_path = IMAGE_PATH + name
        original_image = cv2.imread(image_path)
        for r in region:
            try:
                label = r['label']
                print(label)
                p1 = r['p1']
                p2 = r['p2']
                text_area = original_image[int(p1[0]):int(p2[0]), int(p1[1]):int(p2[1]), :]
                path = TEXT_AREA_DIR_PATH + label + '-' + str(uuid.uuid4()) + '.jpg'
                save_img(text_area, path)
                print(label)
            except Exception as e:
                print(e)


def main():
    annotation_info = load_annotation_info()
    image_map = load_image_info()
    clip_label_image(annotation_info, image_map)


if __name__ == '__main__':
    main()
