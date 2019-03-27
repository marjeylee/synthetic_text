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

ORIGINAL_PATH = 'C:\\Users\lr\Desktop\\black/'

BLACK_PATH = 'C:/Users\lr\Desktop/b1/'


def get_black_images():
    images_path = get_all_files_under_directory(ORIGINAL_PATH)
    for p in images_path:
        try:
            img = cv2.imread(p)
            mean = np.mean(np.mean(img, axis=0), axis=0)
            if mean[0] < 40 and mean[1] < 40 and mean[2] < 40:
                _, file_name = os.path.split(p)
                print(file_name)
                # os.remove(p)
                shutil.move(p, BLACK_PATH + file_name)
        except Exception as e:
            print(e)
            print(p)


if __name__ == '__main__':
    get_black_images()
