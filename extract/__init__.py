# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       'li'
   date：          2018/7/24
-------------------------------------------------
   Change Activity:
                   2018/7/24:
-------------------------------------------------
"""
import json

import cv2

from utility import show_img

__author__ = 'li'


def main():
    file_name = 'f201371e-fc55-4992-b1fb-3207aa5c50ff'
    image_path = 'F:/code/orc/dataset/gen/training_data/' + file_name + '.jpg'
    json_path = 'F:/code/orc/dataset/gen/training_data/' + file_name + '.json'
    with open(json_path, 'r', encoding='utf8')as file:
        json_str = file.readlines()[0]
        obj = json.loads(json_str)
        if 'region' in obj.keys() and obj['region'] is not None and len(obj['region']) > 0:
            region = obj['region']
            img = cv2.imread(image_path)
            show_img(img)
            for r in region:
                p1 = r['p1']
                p2 = r['p2']
                text_img = img[p1[0]:p2[0], p1[1]:p2[1]:]
                info_arr = str(r['info']).split('\\')
                type = info_arr[-2]
                label = info_arr[-1].split('-')[0]
                print(type)
                print(label)
                show_img(text_img)
        pass
    pass


if __name__ == '__main__':
    main()
