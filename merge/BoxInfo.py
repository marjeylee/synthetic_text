# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     BoxInfo
   Description :
   Author :       'li'
   date：          2018/7/24
-------------------------------------------------
   Change Activity:
                   2018/7/24:
-------------------------------------------------
"""
__author__ = 'li'


class BoxInfo:
    def __init__(self, box_type=None, p1=None, p2=None):
        self.p1 = p1  # 左上角的点
        self.p2 = p2  # 右下角的点
        info = str(box_type).split('/')
        self.box_type = info[-2]
        self.label = info[-1].split('-')[0]
