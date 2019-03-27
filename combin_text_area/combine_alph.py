# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     combine_alph
   Description :
   Author :       'li'
   date：          2018/11/26
-------------------------------------------------
   Change Activity:
                   2018/11/26:
-------------------------------------------------
"""
import os

import cv2
import numpy as np

from utility.file_path_utility import get_all_file_from_dir

char_path = 'E:\dataset\seg_char\hor_class/1'
char_paths = get_all_file_from_dir(char_path)


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
            key = name.split('-')[0]
            if key not in mapping.keys():
                mapping[key] = []
            mapping[key].append(p)
    return mapping


def load_mapping():
    return get_mapping(char_paths, 'jpg')


char_str = 'WERTYUIOPASDFGHJKLZXCVBNM'
chars = []
for c in char_str:
    chars.append(c)


def horizontal_splicing_picture(img1, img2):
    """
    水平拼接两张图片
    :param img1:
    :param img2:
    :return:
    """
    shape1 = img1.shape
    radio1 = shape1[0] / 32
    shape2 = img2.shape
    radio2 = shape2[0] / 32
    img1 = cv2.resize(img1, (int(shape1[1] / radio1), 32))
    img2 = cv2.resize(img2, (int(shape2[1] / radio2), 32))
    return np.concatenate((img1, img2), axis=1)


def main():
    mapping = load_mapping()
    random_chars = np.random.choice(chars, size=4)
    bg = None
    for c in random_chars:
        img_path = np.random.choice(mapping[c], size=1)[0]
        img = cv2.imread(img_path)
        if bg is None:
            bg = img
            continue
        bg = horizontal_splicing_picture(bg, img)
    return bg


if __name__ == '__main__':
    for i in range(100):
        tmp_img = main()
        tmp_img = cv2.cvtColor(tmp_img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('img/' + str(i) + '.jpg', tmp_img)
