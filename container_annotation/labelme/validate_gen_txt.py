# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     validate_gen_txt
   Description :
   Author :       'li'
   date：          2018/10/14
-------------------------------------------------
   Change Activity:
                   2018/10/14:
-------------------------------------------------
"""
import numpy as np

from utility.file_path_utility import get_all_file_from_dir

TXT_DIR = 'E:\dataset\detection/training_data/'

paths = get_all_file_from_dir(TXT_DIR)


def polygon_area(poly):
    '''
    compute area of a polygon
    :param poly:
    :return:
    '''
    edge = [
        (poly[1][0] - poly[0][0]) * (poly[1][1] + poly[0][1]),
        (poly[2][0] - poly[1][0]) * (poly[2][1] + poly[1][1]),
        (poly[3][0] - poly[2][0]) * (poly[3][1] + poly[2][1]),
        (poly[0][0] - poly[3][0]) * (poly[0][1] + poly[3][1])
    ]
    return np.sum(edge) / 2.


for p in paths:
    if p.find('txt') > 0:
        with open(p, mode='r', encoding='utf8') as file:
            lines = file.readlines()
            for l in lines:
                rows = l.split(',')
                poly = [
                    [int(rows[0]), int(rows[1])],
                    [int(rows[2]), int(rows[3])],
                    [int(rows[4]), int(rows[5])],
                    [int(rows[6]), int(rows[7])]
                ]
                p_area = polygon_area(poly)
                if abs(p_area) < 1:
                    print(poly)
                    print('invalid poly')
                    # continue
                if p_area > 0:
                    print('poly in wrong direction')
                    poly = poly[(0, 3, 2, 1), :]
