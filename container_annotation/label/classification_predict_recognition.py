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

from utility.file_path_utility import get_all_files_under_directory, create_dir

ORIGINAL_PATH = 'F:\dataset/combine_text_area/'
DESTINATION_PATH = 'F:\dataset\seg/'


def classification_images():
    images_path = get_all_files_under_directory(ORIGINAL_PATH)
    images_size = len(images_path)
    for index in range(images_size):
        p = images_path[index]
        if index % 100 == 0:
            print(str(index) + '/' + str(images_size))
        dir_path, image_name = os.path.split(p)
        label = str(image_name.split('-')[0])
        if label == '':
            label = 'unrecognize'
        elif label[0] == '#':
            label = label.replace('#', '')
            label = '#/' + label
        else:
            length = len(label)
            label = str(length) + '/' + label
        new_path = os.path.join(DESTINATION_PATH, label)
        create_dir(new_path)
        if label[0] == '4':
            des_path = os.path.join(new_path, image_name)
            shutil.copy(p, des_path)


if __name__ == '__main__':
    classification_images()
