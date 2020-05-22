# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     get_all_file_path
   Description :
   Author :       'li'
   date：          2020/1/18
-------------------------------------------------
   Change Activity:
                   2020/1/18:
-------------------------------------------------
"""
import os

from llib.cv_utility.image_opt_utility import read_image, write_image
from utility.file_path_utility import get_all_files_under_directory

img_dir = 'J:/BaiduNetdiskDownload/0506'
des_path = 'J:/BaiduNetdiskDownload/plate_recognize/img/'
paths = get_all_files_under_directory(img_dir)
for path in paths:
    _, name = os.path.split(path)
    image = read_image(path)
    write_image(des_path + name, image)
