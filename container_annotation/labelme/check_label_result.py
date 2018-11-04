# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     check_label_result
   Description :
   Author :       'li'
   date：          2018/10/19
-------------------------------------------------
   Change Activity:
                   2018/10/19:
-------------------------------------------------
"""
import os

import cv2

from utility.file_path_utility import get_all_file_from_dir


def get_mapping(files_path, file_type):
    """
    get mapping
    :param files_path:
    :param file_type:
    :return:
    """
    files_path = get_all_file_from_dir(files_path)
    mapping = {}
    for p in files_path:
        if p.find(file_type) >= 0:
            _, name = os.path.split(p)
            mapping[name.split('.')[0]] = p
    return mapping


def write_line(new_txt_path, new_line):
    with open(new_txt_path, mode='a', encoding='utf8') as file:
        file.write(new_line)


if __name__ == '__main__':
    image_dir = 'D:\dataset\detection\detection/training_data\img'
    txt_dir = 'D:\dataset\detection\detection/training_data/txt'
    des_path = 'D:\dataset\detection\detection/training_data\check_txt/'
    img_map = get_mapping(image_dir, 'jpg')
    txt_map = get_mapping(txt_dir, 'txt')
    txt_keys = txt_map.keys()
    for k in img_map.keys():
        if k in txt_keys:
            txt_path = txt_map[k]
            img_path = img_map[k]
            shape = cv2.imread(img_path).shape
            with open(txt_path, mode='r', encoding='utf8') as file:
                lines = file.readlines()
                for line in lines:
                    row = line.split(',')
                    assert len(row) >= 8
                    new_line = ''
                    for index in range(8):
                        v = float(row[index])
                        if v <= 0:
                            print(v)
                            v = 0
                        elif index % 2 == 0:
                            if v >= shape[1]-1:
                                print(str(v) + '-' + str(shape[1]))
                                v = shape[1] - 2
                        elif index % 2 == 1:
                            if v >= shape[0]-1:
                                print(str(v) + '-' + str(shape[0]))
                                v = shape[0] - 2
                        new_line += str(int(v)) + ','
                    new_line += 'un\n'
                    new_txt_path = des_path + str(k) + '.txt'
                    write_line(new_txt_path, new_line)
