#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 15:39
# @Author  : lr
# @Site    : 
# @File    : gen_text_area_from_points.py
# @Software: PyCharm
import cv2
import numpy as np
import matplotlib.pyplot as plt

from container_annotation.labelme.sort_point import resort_points


def get_new_bg_from_points(original_image, points):
    """
    get text area from image
    :param original_image:
    :param points:
    :return:
    """
    image_shape = original_image.shape
    bg = np.ones([image_shape[0], image_shape[1], 3]) * -1
    nd_points = np.array([[points]], dtype=np.int32)
    cv2.fillPoly(bg, nd_points, (1, 1, 1))
    bg = bg * original_image
    bg[np.where(bg < 0)] = 255
    return bg

def main():
    original_image = cv2.imread('1.jpg')
    points = [[94, 146], [111, 275], [591, 179], [592, 279]]
    points = resort_points(points)
    print(points)
    text_area = get_text_area_from_image(original_image, points)


if __name__ == '__main__':
    main()
