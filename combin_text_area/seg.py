# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     seg
   Description :
   Author :       'li'
   date：          2018/11/22
-------------------------------------------------
   Change Activity:
                   2018/11/22:
-------------------------------------------------
"""
import os
import shutil

from utility.file_path_utility import get_all_file_from_dir
import cv2

or_path = 'C:/Users\lr\Desktop\combine'
paths = get_all_file_from_dir(or_path)
for p in paths:
    img = cv2.imread(p)
    shape = img.shape
    if shape[0] < shape[1]:
        _, img_name = os.path.split(p)
        shutil.copy(p, 'C:/Users\lr\Desktop\ho_comb/' + img_name)
