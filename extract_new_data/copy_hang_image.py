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

IMAGE_DIR = 'C:/Users\lr\Desktop\error/'
HANG_DIR = 'C:/Users\lr\Desktop\error_img/'
imgs = get_all_file_from_dir(IMAGE_DIR)
index = 1
for i in imgs:
    index = index + 1
    if i.find("txt") >= 0 or i.find("DMG") >= 0:
        continue

    new_path = HANG_DIR + str(uuid.uuid4()) + '.jpg'
    shutil.copyfile(i, new_path)
