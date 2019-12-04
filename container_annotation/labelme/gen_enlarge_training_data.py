# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     gen_training_data
   Description :
   Author :       'li'
   date：          2018/10/7
-------------------------------------------------
   Change Activity:
                   2018/10/7:
-------------------------------------------------
"""
import base64
import json
import math
import os

import cv2

from utility.file_io_utility import read_all_content
from utility.file_path_utility import get_all_file_from_dir, create_dir
import numpy as np


JSON_DIR = 'D:/label_result/label_result/car_number/json/'
TRAINING_DATA_DIR = 'D:/label_result/label_result/car_number/txt/'
create_dir(TRAINING_DATA_DIR)


def save_image(image_str, i, file_name):
    image_path = TRAINING_DATA_DIR + file_name + '.jpg'
    fh = open(image_path, "wb")
    fh.write(base64.b64decode(image_str))
    fh.close()
    img = cv2.imread(image_path)
    shape = img.shape
    new_width, new_height = 512, 512
    if shape[0] > new_height:
        new_height = shape[0]
    if shape[1] > new_width:
        new_width = shape[1]
    bg = np.ones(shape=(new_height, new_width, 3)) * 255
    bg[0:shape[0], 0:shape[1], :] = img
    cv2.imwrite(image_path, bg)
    # image_path = TRAINING_DATA_DIR + 'img_' + str(i + 1) + '.jpg'
    # fh = open(image_path, "wb")
    # fh.write(base64.b64decode(image_str))
    # fh.close()


def get_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def get_nearest_points(points):
    nearest_points = []
    emu = [[[0, 1], [2, 3]], [[0, 2], [1, 3]], [[0, 3], [1, 2]]]
    for e in emu:  # e :[[0, 1], [2, 3]]
        sum_dis = get_distance(points[e[0][0]], points[e[0][1]]) + get_distance(points[e[1][0]], points[e[1][1]])
        if len(nearest_points) == 0:
            nearest_points = [e, sum_dis]
        else:
            if sum_dis < nearest_points[1]:
                nearest_points = [e, sum_dis]
    return nearest_points


def get_middle_points(points, nearest_points):
    p1x = (points[nearest_points[0][0][0]][0] + points[nearest_points[0][0][1]][0]) / 2
    p1y = (points[nearest_points[0][0][0]][1] + points[nearest_points[0][0][1]][1]) / 2
    p2x = (points[nearest_points[0][1][0]][0] + points[nearest_points[0][1][1]][0]) / 2
    p2y = (points[nearest_points[0][1][0]][1] + points[nearest_points[0][1][1]][1]) / 2
    # print([(p1x, p1y), (p2x, p2y)])
    return [(p1x, p1y), (p2x, p2y)]


def get_angle(middle_points):
    # if middle_points[0][0] > middle_points[1][0]:
    #     middle_points = [middle_points[1], middle_points[0]]
    middle_distance = get_distance(middle_points[0], middle_points[1])
    h = abs(middle_points[0][1] - middle_points[1][1])
    return math.asin(h / middle_distance) * 180 / math.pi


def horizontal_points(points, nearest_points, middle_points):
    return_points = [None, None, None, None]
    ups = []
    downs = []
    if points[nearest_points[0][0][0]][1] < middle_points[0][1]:
        ups.append(points[nearest_points[0][0][0]])
        downs.append(points[nearest_points[0][0][1]])
    else:
        ups.append(points[nearest_points[0][0][1]])
        downs.append(points[nearest_points[0][0][0]])
    if points[nearest_points[0][1][0]][1] < middle_points[1][1]:
        ups.append(points[nearest_points[0][1][0]])
        downs.append(points[nearest_points[0][1][1]])
    else:
        ups.append(points[nearest_points[0][1][1]])
        downs.append(points[nearest_points[0][1][0]])
    if ups[0][0] < ups[1][0]:
        return_points[0] = ups[0]
        return_points[1] = ups[1]
    else:
        return_points[0] = ups[1]
        return_points[1] = ups[0]
    if downs[0][0] > downs[1][0]:
        return_points[2] = downs[0]
        return_points[3] = downs[1]
    else:
        return_points[2] = downs[1]
        return_points[3] = downs[0]
    return return_points


def vertical_points(points, nearest_points, middle_points):
    return_points = [None, None, None, None]
    left = []
    right = []
    if points[nearest_points[0][0][0]][0] < middle_points[0][0]:
        left.append(points[nearest_points[0][0][0]])
        right.append(points[nearest_points[0][0][1]])
    else:
        left.append(points[nearest_points[0][0][1]])
        right.append(points[nearest_points[0][0][0]])
    if points[nearest_points[0][1][0]][0] < middle_points[1][0]:
        left.append(points[nearest_points[0][1][0]])
        right.append(points[nearest_points[0][1][1]])
    else:
        left.append(points[nearest_points[0][1][1]])
        right.append(points[nearest_points[0][1][0]])
    if left[0][1] < left[1][1]:  # y axis
        return_points[0] = left[0]
        return_points[3] = left[1]
    else:
        return_points[0] = left[1]
        return_points[3] = left[0]
    if right[0][1] < right[1][1]:
        return_points[1] = right[0]
        return_points[2] = right[1]
    else:
        return_points[1] = right[1]
        return_points[2] = right[0]
    return return_points


def resort_points(points):
    nearest_points = get_nearest_points(points)
    middle_points = get_middle_points(points, nearest_points)
    middle_angle = get_angle(middle_points)
    if -45 < middle_angle < 45:
        return horizontal_points(points, nearest_points, middle_points)
    else:
        return vertical_points(points, nearest_points, middle_points)


def save_txt(shapes, i, file_name):
    txt_path = TRAINING_DATA_DIR + file_name + '.txt'
    # txt_path = TRAINING_DATA_DIR + 'img_' + str(i + 1) + '.txt'
    with open(txt_path, mode='w', encoding='utf8')as file:
        for shape in shapes:
            label = shape['label']
            if label is None or label == '':
                label = 'undefined'
            points = shape['points']
            points = resort_points(points)
            line = ''
            for point in points:
                line = line + str(int(point[0])) + ',' + str(int(point[1])) + ','
            line += label + '/n'
            file.write(line)


def main():
    paths = get_all_file_from_dir(JSON_DIR)
    for i, p in enumerate(paths):
        # if i != 117:
        #     continue
        print(i)
        print(p)
        _, file_name = os.path.split(p)
        print(file_name)
        content = read_all_content(p)
        obj = json.loads(content)
        save_image(obj['imageData'], i, file_name)
        save_txt(obj['shapes'], i, file_name)


if __name__ == '__main__':
    main()
