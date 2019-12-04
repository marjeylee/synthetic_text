# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     gen_labelme_json
   Description :
   Author :       'li'
   date：          2018/10/6
-------------------------------------------------
   Change Activity:
                   2018/10/6:
-------------------------------------------------
"""
import base64
import copy
import json
import os
import uuid
import numpy as np
import cv2

from container_annotation.labelme.gen_text_area_from_points import get_new_bg_from_points
from container_annotation.labelme.sort_point import resort_points, get_rotate_img
from delete import get_uuid_str
from utility.file_path_utility import get_all_file_from_dir

IMAGE_LABEL_DIR = 'D:/data/danzheng/txt/'
JSON_LABEL_DIR = 'C:/Users/lr/Desktop/area/'


def get_mapping(files_path, file_type):
    """
    get mapping
    :param files_path:
    :param file_type:
    :return:
    """
    mapping = {}
    for p in files_path:
        if p.find(file_type) >= 0:
            _, name = os.path.split(p)
            mapping[name.split('.')[0].replace('res_', '')] = p
    return mapping


def load_shapes(txt_path, image_path):
    """
    load point to shape
    :param txt_path:
    :return:
    """
    with open(txt_path, mode='r', encoding='utf8') as file:
        lines = file.readlines()
        if len(lines) == 0:
            return []
        image = cv2.imread(image_path)
        txt_name = os.path.split(txt_path)[1].split('.')[0]
        for l in lines:
            points = l.split(',')
            points = [[int(points[0]), int(points[1])], [int(points[2]), int(points[3])],
                      [int(points[4]), int(points[5])], [int(points[6]), int(points[7])]]
            points = resort_points(points)
            tmp_image = copy.deepcopy(image)
            tmp_image = get_new_bg_from_points(tmp_image, points)
            cnt = np.array(points)
            rect = cv2.minAreaRect(cnt)  # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
            box = cv2.boxPoints(rect)  # cv2.boxPoints(rect) for OpenCV 3.x 获取最小外接矩形的4个顶点
            box = np.int0(box).tolist()
            points = resort_points(box)
            area = get_rotate_img(tmp_image, points[0], points[1], points[2], points[3])
            cv2.imwrite('C:/Users/lr/Desktop/area/' + str(txt_name) + '--' + get_uuid_str() + '.jpg', area)


def load_image_str(image_path):
    with open(image_path, "rb") as imageFile:
        image_s = base64.b64encode(imageFile.read())
        image_s = str(image_s).replace('b\'', '')
        image_s = str(image_s).replace('\'', '')
        return str(image_s)


if __name__ == '__main__':
    paths = get_all_file_from_dir(IMAGE_LABEL_DIR)
    image_mapping = get_mapping(paths, file_type='jpg')
    txt_mapping = get_mapping(paths, file_type='txt')
    txt_mapping_keys = txt_mapping.keys()
    index = 1
    for key in image_mapping.keys():
        if key in txt_mapping_keys:
            shapes = load_shapes(txt_mapping[key], image_mapping[key])
