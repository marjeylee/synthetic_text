# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     combine_10
   Description :
   Author :       'li'
   date：          2018/11/22
-------------------------------------------------
   Change Activity:
                   2018/11/22:
-------------------------------------------------
"""
import os
import uuid

import cv2

from utility.file_path_utility import get_all_file_from_dir
import numpy as np

BASE_DIE = 'C:/Users\lr\Desktop/right_recognize_result/'


def get_num_path(img_paths, num):
    for p in img_paths:
        _, image_name = os.path.split(p)
        label = image_name.split('-')[0]
        if len(label) == num:
            return p, label
    return None, None


def gen_11(tmp_dir):
    img_paths = get_all_file_from_dir(tmp_dir)
    alph, alph_label = get_num_path(img_paths, 4)
    six, six_label = get_num_path(img_paths, 6)
    one, one_label = get_num_path(img_paths, 1)
    if alph is not None and six is not None:
        alph = cv2.imread(alph)
        six = cv2.imread(six)
        one = cv2.imread(one)
        alph_shape = alph.shape
        six_shape = six.shape
        one_shape = one.shape
        if alph_shape[0] / alph_shape[1] > 1 and six_shape[0] / six_shape[1] > 1:  # vertical
            alph = cv2.resize(alph, (32, int(32 / alph_shape[1] * alph_shape[0])))
            six = cv2.resize(six, (32, int(32 / six_shape[1] * six_shape[0])))
            one = cv2.resize(one, (32, int(32 / one_shape[1] * one_shape[0])))
            return np.concatenate((alph, six, one), axis=0), alph_label + six_label + one_label
        if alph_shape[0] / alph_shape[1] < 1 and six_shape[0] / six_shape[1] < 1:  # horizontal
            alph = cv2.resize(alph, (int(32 / alph_shape[0] * alph_shape[1]), 32))
            six = cv2.resize(six, (int(32 / six_shape[0] * six_shape[1]), 32))
            one = cv2.resize(one, (int(32 / one_shape[0] * one_shape[1]), 32))
            return np.concatenate((alph, six, one), axis=1), alph_label + six_label + one_label
    return None, None


DES = 'C:/Users\lr\Desktop/11/'


def main():
    for root, dirs, files in os.walk(BASE_DIE):
        for name in dirs:
            try:
                tmp_dir = os.path.join(root, name)
                com, label = gen_11(tmp_dir)
                if com is not None:
                    cv2.imwrite(DES + label + '-' + str(uuid.uuid4()) + '.jpg', com)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()
