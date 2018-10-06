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
import json
import os
import uuid

from utility.file_path_utility import get_all_file_from_dir

IMAGE_LABEL_DIR = 'E:\dataset\detection_2018-9-27\ICPR2018'
JSON_LABEL_DIR = 'E:\dataset\detection\json_label/'


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
            mapping[name.split('.')[0]] = p
    return mapping


def load_shapes(txt_path):
    """
    load point to shape
    :param txt_path:
    :return:
    """
    with open(txt_path, mode='r', encoding='utf8') as file:
        lines = file.readlines()
        if len(lines) == 0:
            return []
        shapes = []
        for l in lines:
            points = l.split(',')
            x1, y1, x2, y2 = int(points[0]), int(points[1]), int(points[4]), int(points[5])
            shape = {"label": "dsada", "line_color": None, "fill_color": None,
                     "points": [[x1, y1], [x1, y2], [x2, y2], [x2, y1]]
                     }
            shapes.append(shape)
        return shapes


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
    for key in image_mapping.keys():
        if key in txt_mapping_keys:
            shapes = load_shapes(txt_mapping[key])
            image_str = load_image_str(image_mapping[key])
            json_obj = {
                "flags": {},
                "shapes": shapes,
                "lineColor": [0, 255, 0, 128],
                "fillColor": [255, 0, 0, 128],
                "imagePath": "",
                "imageData": image_str
            }
            json_str = json.dumps(json_obj)
            json_str = json_str.replace('b\'', '')
            json_str = json_str.replace('\'', '')
            p = JSON_LABEL_DIR + str(key) + '.json'
            with open(p, mode='w', encoding='utf8') as file:
                file.write(json_str)
