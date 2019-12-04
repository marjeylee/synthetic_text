#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/17 18:27
# @Author  : lr
# @Site    : 
# @File    : draw_lines_bboxs.py
# @Software: PyCharm
import os

import numpy as np
import cv2

from utility.file_path_utility import get_all_file_from_dir


def get_detect_result(detect_result, img):
    """
    s
    :param img:
    :param detect_result:
    :return:
    """
    for result in detect_result:
        vector = np.array(result)
        vector = vector.reshape(-1, 2)
        cv2.polylines(img, [vector], isClosed=True, color=(255, 255, 0))
    return img


def get_points(txt_path):
    all_points = []
    with open(txt_path, encoding='utf8', mode='r') as file:
        lines = file.readlines()
        for line in lines:
            if len(line) < 3:
                continue
            points = line.split(',')[:-1]
            new_points = []
            for p in points:
                new_points.append(int(p))
            all_points.append(new_points)
    all_points = np.array(all_points)
    return all_points


def main():
    txt_and_image_paths = 'C:/Users/lr/Desktop/new/wuhan'
    des_line_dir = 'C:/Users/lr/Desktop/new/des/'
    paths = get_all_file_from_dir(txt_and_image_paths)
    try:
        for i, p in enumerate(paths):
            print(i)
            if '.jpg' not in p:
                continue
            img_name = os.path.split(p)[1].replace('.jpg', '')
            img = cv2.imread(p)
            txt_path = p.replace('.jpg', '.txt')
            points = get_points(txt_path)
            draw_image = get_detect_result(points, img)
            cv2.imwrite(des_line_dir + img_name + '.jpg', draw_image)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
