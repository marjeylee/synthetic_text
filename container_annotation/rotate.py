# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     rotate
   Description :
   Author :       'li'
   date：          2019/1/4
-------------------------------------------------
   Change Activity:
                   2019/1/4:
-------------------------------------------------
"""
import uuid

import cv2
import numpy as np

from utility.file_path_utility import get_all_file_from_dir

des_path = 'C:/Users\lr\Desktop\h/'
dir_path = 'C:/Users\lr\Desktop\label'
paths = get_all_file_from_dir(dir_path)
for p in paths:
    img = cv2.imread(p)
    shape = img.shape
    name = uuid.uuid4()
    if shape[0] == 540:
        img = np.rot90(img)
    cv2.imwrite(des_path + name + '.jpg', img)
