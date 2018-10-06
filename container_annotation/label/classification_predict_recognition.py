# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     cluster_predict_recognition
   Description :
   Author :       'li'
   date：          2018/9/7
-------------------------------------------------
   Change Activity:
                   2018/9/7:
-------------------------------------------------
"""
import os
import shutil
import uuid

from utility.file_path_utility import get_all_files_under_directory, create_dir

ORIGINAL_PATH = 'E:\dataset/text_area\horizontal/'
DESTINATION_PATH = 'E:\dataset/text_area\horizontal_classify/'


def classification_images():
    images_path = get_all_files_under_directory(ORIGINAL_PATH)
    images_size = len(images_path)
    for index in range(images_size):
        p = images_path[index]
        if index % 100 == 0:
            print(str(index) + '/' + str(images_size))
        dir_path, image_name = os.path.split(p)
        label = str(image_name.split('-')[0]).replace('#', '').replace(' ', '')
        if label == '':
            dir_name = 'unrecognize'
        else:
            length = len(label)
            dir_name = str(length)
        new_path = os.path.join(DESTINATION_PATH, dir_name)
        new_path = os.path.join(new_path, label)
        create_dir(new_path)
        # if label[0] == '4':
        # label = label.replace('\\', '').replace('/', '')
        image_name = label + '-' + str(uuid.uuid4()) + '.jpg'
        des_path = os.path.join(new_path, image_name)
        # if len(label) == 4:
        shutil.copy(p, des_path)


if __name__ == '__main__':
    classification_images()
