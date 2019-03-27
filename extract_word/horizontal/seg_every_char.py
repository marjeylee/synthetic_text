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
from utility.file_path_utility import get_all_file_from_dir, get_all_files_under_directory


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


def_path = 'E:\dataset\seg_char\hor/'


def seg_horozontal(label, img):
    gray_img = to_gray(img)
    text_array = get_horizontal_seg_array(gray_img)
    size = len(text_array)
    if len(label) != size:
        return
    for index in range(size):
        area = text_array[index]
        if index == 0:
            next_area = text_array[index + 1]
            tmp_img = img[:, 0:int((area[-1] + next_area[0]) / 2), :]

        elif index == size - 1:
            tmp_img = img[:, area[0]:, :]
        else:
            next_area = text_array[index + 1]
            last_area = text_array[index - 1]
            tmp_img = img[:, int((last_area[-1] + area[0]) / 2):int((area[-1] + next_area[0]) / 2), :]
        cv2.imwrite(def_path + label[index] + '-' + str(uuid.uuid4()) + '.jpg', tmp_img)


def main():
    ver = 'E:\dataset\horizontal'
    paths = get_all_files_under_directory(ver)
    for index, path in enumerate(paths):
        if index % 100 == 0:
            print(index)
        _, img_name = os.path.split(path)
        label = img_name.split('-')[0]
        img = cv2.imread(path)
        if len(label) < 2:
            continue
        seg_horozontal(label, img)


if __name__ == '__main__':
    main()
