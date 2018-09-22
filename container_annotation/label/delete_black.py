# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     delete_black
   Description :
   Author :       'li'
   date：          2018/9/21
-------------------------------------------------
   Change Activity:
                   2018/9/21:
-------------------------------------------------
"""
import os
import shutil

import cv2

from utility.file_path_utility import get_all_files_under_directory
import numpy as np

ORIGINAL_PATH = 'E:\dataset\seg/'
BLACK_PATH = 'E:\dataset/black/'


def get_black_images():
    images_path = get_all_files_under_directory(ORIGINAL_PATH)
    for p in images_path:
        img = cv2.imread(p)
        mean = np.mean(np.mean(img, axis=0), axis=0)
        if mean[0] < 35 and mean[1] < 35 and mean[2] < 35:
            print(p)
            os.remove(p)


if __name__ == '__main__':
    get_black_images()
