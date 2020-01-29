# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     validate_images
   Description :
   Author :       'li'
   date：          2018/9/4
-------------------------------------------------
   Change Activity:
                   2018/9/4:
-------------------------------------------------
"""
import hashlib
import os
import time

from common.utility import combine_file_path

__author__ = 'li'
upload_image_path = combine_file_path('tmp/upload_image/')

NO_IMAGE_ERROR = {'code': 1, 'msg': 'No pictures were received'}


def get_md5(image_path):
    """
    get md5
    :param image_path:
    :return:
    """
    hash_lib = hashlib.md5()
    f = open(image_path, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        hash_lib.update(b)
    f.close()
    return hash_lib.hexdigest()


def validate_images(dir_name, images_info, performance_log):
    """
    validate images transfer correct
    :param performance_log:
    :param dir_name:
    :param images_info:
    :return:
    """
    performance_log.image_MD5_check_start_time = time.time()
    images_dir = os.path.join(upload_image_path, dir_name)
    if len(images_info) == 0:
        performance_log.set_time(performance_log.image_MD5_check_end_time)
        return {'isSuccess': False, 'msg': NO_IMAGE_ERROR}
    try:
        for i in images_info:
            image_name = i['image_name']
            if str(image_name).find('.jpg') >= 0 or str(image_name).find('.png') >= 0:
                image_path = os.path.join(images_dir, image_name)
                if not os.path.isfile(image_path):
                    msg = 'Did not find image:' + image_name
                    performance_log.image_MD5_check_end_time = time.time()
                    return {'isSuccess': False, 'msg': {'code': 2, 'msg': msg}}
                python_md5 = (get_md5(image_path)).strip()
                java_md5 = str(i['md5']).strip()
                if java_md5 != python_md5:
                    msg = 'md5 not equal:' + image_name
                    performance_log.image_MD5_check_end_time = time.time()
                    return {'isSuccess': False, 'msg': {'code': 3, 'msg': msg}}
    except Exception as e:
        performance_log.image_MD5_check_end_time = time.time()
        return {'isSuccess': False, 'msg': {'code': 4, 'msg': str(e)}}
    performance_log.image_MD5_check_end_time = time.time()
    return {'isSuccess': True}
