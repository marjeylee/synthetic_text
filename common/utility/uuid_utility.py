# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     uuid_utility
   Description :
   Author :       'li'
   date：          2019/3/12
-------------------------------------------------
   Change Activity:
                   2019/3/12:
-------------------------------------------------
"""
import uuid


def get_uuid_str():
    """
    generate uuid string of 40 size
    :return:
    """
    return str(uuid.uuid4()).replace('-', '')
