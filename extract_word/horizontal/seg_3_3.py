# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     seg_every_char
   Description :
   Author :       'li'
   date：          2018/11/4
-------------------------------------------------
   Change Activity:
                   2018/11/4:
-------------------------------------------------
"""
import os
import uuid

import cv2
import numpy as np

from extract_word.vertical.gen_text_pixel import to_gray, get_txt_pixels
from utility.file_path_utility import get_all_file_from_dir


def append_text_area(text_array, current_array):
    """
    add and filter text area
    :param text_array:
    :param current_array:
    :return:
    """
    if len(current_array) > 3:
        text_array.append(current_array)


def get_text_array(local):
    text_array = []
    current_array = []
    for lo in local[0]:
        if len(current_array) == 0 or current_array[-1] + 1 == lo:
            current_array.append(lo)
        else:
            append_text_area(text_array, current_array)
            current_array = [lo]
    if len(current_array) > 0:
        append_text_area(text_array, current_array)
    return text_array


def add_boundary(text_array):
    length = len(text_array)
    if length < 2:
        return text_array
    for index, area in enumerate(text_array):
        if index + 1 < length:
            end = int((text_array[index + 1][0] + area[-1]) / 2)
            area.append(end)
            pass
    return text_array


def get_horizontal_seg_array(gray_img):
    """
    get horizontal text area,including 11 box num.
    :param gray_img:
    :return:
    """
    shape = gray_img.shape
    value = np.var(gray_img, axis=0)
    ave_value = np.sum(value) / shape[1]
    per_value = value / ave_value
    is_text = (per_value > 0.5)
    local = np.where(is_text == True)
    text_array = get_text_array(local)
    # text_array = add_boundary(text_array)
    return text_array


def get_vertical_seg_array(gray_img):
    """
    get horizontal text area,including 11 box num.
    :param gray_img:
    :return:
    """
    shape = gray_img.shape
    value = np.var(gray_img, axis=1)
    ave_value = np.sum(value) / shape[0]
    per_value = value / ave_value
    is_text = (per_value > 0.5)
    local = np.where(is_text == True)
    text_array = get_text_array(local)
    return text_array


def_path = 'E:\dataset\\11-28\horizontal\horizontal\seg_3_3/'


# def_path = './'


def seg_horozontal(label, img):
    gray_img = to_gray(img)
    text_array = get_horizontal_seg_array(gray_img)
    size = len(text_array)
    if len(label) != size:
        return
    tmp_img = img[:, 0:int((text_array[2][-1] + text_array[3][0]) / 2), :]
    cv2.imwrite(def_path + label[:3] + '-' + str(uuid.uuid4()) + '.jpg', tmp_img)
    tmp_img = img[:, int((text_array[2][-1] + text_array[3][0]) / 2):, :]
    cv2.imwrite(def_path + label[3:] + '-' + str(uuid.uuid4()) + '.jpg', tmp_img)


def main():
    dir_path = 'E:\dataset\\11-28\horizontal\horizontal\class\\6/'
    paths = get_all_file_from_dir(dir_path)
    for i, p in enumerate(paths):
        if i % 100 == 0:
            print(i)
        _, img_name = os.path.split(p)
        label = img_name.split('-')[0]
        if len(label) != 6:
            continue
        img = cv2.imread(p)
        seg_horozontal(label, img)


if __name__ == '__main__':
    main()
