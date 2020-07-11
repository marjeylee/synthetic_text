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
from chinese_project.move_file.rename_file_md5 import GetFileMd5
from llib.cv_utility.image_opt_utility import read_image, write_image
from utility.file_io_utility import read_all_content
from utility.file_path_utility import get_all_file_from_dir, create_dir
import numpy as np

JSON_DIR = '/data/data/dangerous_bb/tt/project/daokou/data/json/'
TRAINING_DATA_DIR = 'G:/tmp/txt/'
create_dir(TRAINING_DATA_DIR)

enlarge_radio = 0.9


def save_image(image_str, i, file_name):
    if enlarge_radio == 1:
        image_path = TRAINING_DATA_DIR + file_name.replace('.json', '') + '.jpg'
    else:
        image_path = TRAINING_DATA_DIR + file_name.replace('.json', '') + \
                     str(enlarge_radio).replace('.', '_') + '.jpg'
    fh = open(image_path, "wb")
    fh.write(base64.b64decode(image_str))
    fh.close()
    img = read_image(image_path)
    shape = img.shape
    img = cv2.resize(img, (int(shape[1] * enlarge_radio), int(shape[0] * enlarge_radio)))
    write_image(image_path, img)
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
    """
    vertical points
    :param points:
    :param nearest_points:
    :param middle_points:
    :return:
    """
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
    if enlarge_radio == 1:
        txt_path = TRAINING_DATA_DIR + file_name.replace('.json', '') + '.txt'
    else:
        txt_path = TRAINING_DATA_DIR + file_name.replace('.json', '') + \
                   str(enlarge_radio).replace('.', '_') + '.txt'
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
                line = line + str(int(point[0] * enlarge_radio)) + ',' + str(int(point[1] * enlarge_radio)) + ','
            line += label + '\n'
            file.write(line)


def get_file_name(image_str):
    image_path = 'tmp.jpg'
    fh = open(image_path, "wb")
    fh.write(base64.b64decode(image_str))
    fh.close()
    md5 = GetFileMd5(image_path)
    os.remove(image_path)
    return md5


def main():
    paths = get_all_file_from_dir(JSON_DIR)
    # try:
    for i, p in enumerate(paths):
        try:
            if '.json' not in p:
                continue
            print(i)
            if i < 0:
                continue
            content = read_all_content(p)
            obj = json.loads(content)
            file_name = os.path.split(p)[1].split('.')[0]
            # file_name = get_file_name(obj['imageData'])
            save_image(obj['imageData'], i, file_name)
            save_txt(obj['shapes'], i, file_name)
        except:
            pass


# except Exception as e:
#     print(p)
#     print(e)


if __name__ == '__main__':
    main()
