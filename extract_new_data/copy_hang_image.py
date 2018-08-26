# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     copy_hang_image
   Description :
   Author :       'li'
   date：          2018/8/18
-------------------------------------------------
   Change Activity:
                   2018/8/18:
-------------------------------------------------
"""
import shutil
import uuid

from utility.file_path_utility import get_all_file_from_dir

__author__ = 'li'

IMAGE_DIR = 'F:\dataset/07/'
HANG_DIR = 'F:/dataset/all_image\other/'
imgs = get_all_file_from_dir(IMAGE_DIR)
index = 1
for i in imgs:
    index = index + 1
    if i.find("LAND_1.jpg") >= 0 or i.find("LAND_2.jpg") >= 0 or i.find("LEFT_1.jpg") >= 0 or i.find(
            "RIGHT_1.jpg") >= 0 or i.find("SEA_1.jpg") >= 0 or i.find("SEA_2.jpg") >= 0 or i.find("RIGHT_1.jpg") >= 0:
        print(index)
        if index < 27000:
            continue
        new_path = HANG_DIR + str(uuid.uuid4()) + '.jpg'
        shutil.copyfile(i, new_path)
