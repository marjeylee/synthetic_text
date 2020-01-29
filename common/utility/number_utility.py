"""
数字工具类
"""
# -*- coding: utf-8 -*-

import random


def get_random_number_range(num_size, num_range):
    """
    从指定范围内随机获取num_size个数的数据
    :param num_size:
    :param num_range:eg(100,1000)  100<=x<1000
    :return:
    """
    min_range = num_range[0]
    max_range = num_range[1]
    random_list = []
    for _ in range(num_size):
        random_list.append(random.randint(min_range, max_range))
    return random_list
