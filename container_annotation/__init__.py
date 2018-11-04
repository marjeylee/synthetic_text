# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       'li'
   date：          2018/7/29
-------------------------------------------------
   Change Activity:
                   2018/7/29:
-------------------------------------------------
"""
import math

__author__ = 'li'
"""
真实环境标注信息
"""

import numpy as np


def get_vector_angle(v1, v2):
    v1 = np.array(v1).reshape((len(v1, )))
    v2 = np.array(v2).reshape((len(v2, )))
    dot = np.dot(v1, v2)
    a_angle = dot / (np.sqrt(np.sum(v1 ** 2)) * np.sqrt(np.sum(v2 ** 2)))  # * 180 / math.pi
    angle = math.acos(a_angle) * 180 / math.pi
    return angle


a = get_vector_angle([1, 0], [1, 1])
print(a)
