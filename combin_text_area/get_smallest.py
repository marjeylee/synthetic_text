# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     get_smallest
   Description :
   Author :       'li'
   date：          2018/11/23
-------------------------------------------------
   Change Activity:
                   2018/11/23:
-------------------------------------------------
"""
import os
import shutil

import cv2

from delete.copy_file import get_all_file_from_dir

PARENT_DIR_PATH = 'E:\dataset\wrong\wrong_recognize_result/'
DES_DIR_PATH = 'E:\dataset\wrong/1/'


def get_smallest(files):
    p = None
    sm_img = None
    for f in files:
        if p is None:
            p = f
            sm_img = cv2.imread(p)
            continue
        tmp_img = cv2.imread(f)
        if tmp_img.shape[0] * tmp_img.shape[1] < sm_img.shape[0] * sm_img.shape[1]:
            p = f
            sm_img = cv2.imread(p)
    return p


for dirpath, dirnames, filenames in os.walk(PARENT_DIR_PATH):
    for d in dirnames:
        sub_dir = os.path.join(dirpath, d)
        files = get_all_file_from_dir(sub_dir)
        img_path = get_smallest(files)
        _, img_name = os.path.split(img_path)
        shutil.copy(img_path, DES_DIR_PATH + img_name)
