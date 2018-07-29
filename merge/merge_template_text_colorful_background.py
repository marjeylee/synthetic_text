# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     merge_template_text_colorful_background
   Description :
   Author :       'li'
   date：          2018/7/24
-------------------------------------------------
   Change Activity:
                   2018/7/24:
-------------------------------------------------
"""
import json
import random
import uuid

import cv2
import numpy as np

from config import *
from utility import show_img
from utility.file_path_utility import get_all_file_from_dir
from utility.image_utility import save_img

__author__ = 'li'
bg_file_path = []
with open('./gb_list.txt', 'r', encoding='utf8')as file:
    lines = file.readlines()
    for line in lines:
        bg_file_path.append(line.replace('\n', ''))
text_template_path = []
with open('./template_list.txt', 'r', encoding='utf8')as file:
    lines = file.readlines()
    for line in lines:
        text_template_path.append(line.replace('\n', ''))


def merge_image():
    """
    合并图片
    :return:
    """
    for i in range(100000000):
        print(i)
        try:
            bg_path = np.random.choice(bg_file_path, size=1)[0]
            num = np.random.randint(0, 10, size=1)[0]  # 随机有多少个出现
            template_path_list = np.random.choice(text_template_path, size=num)
            merge_image_template(bg_path, template_path_list)
        except Exception as e:
            print(e)


def get_endpoints(point, text_shape):
    """
    获得端点,顺时针方向
    :param point:
    :param text_shape:
    :return:
    """
    h, w = point[0], point[1]
    return [(h, w), (h, w + text_shape[1]), (h + text_shape[0], w + text_shape[1]), (h + text_shape[0], w)]


def mat_inter(box1, area):
    """
    # 判断两个矩形是否相交
    :param box1:
    :param area:
    :return:
    """
    x01, y01, x02, y02 = box1
    margin = 8
    h_range = np.random.randint(x01, x02, 1000)
    w_range = np.random.randint(y01, y02, 1000)
    for i in range(1000):
        if area[0][0] - margin < h_range[i] < area[0][1] + margin and \
                area[1][0] - margin < w_range[i] < area[1][1] + margin:
            return True  # 相交
    return False


def get_available_point(bg_shape, text_area, text_shape):
    """
    获取可用的点
    :param bg_shape:
    :param text_area:[[[h_start,h_end],[w_start,w_end]]。。。。。]
    :param text_shape:
    :return:
    """
    h, w = np.random.randint(10, bg_shape[0] - 10 - text_shape[0], size=1)[0], \
           np.random.randint(10, bg_shape[1] - 10 - text_shape[1], size=1)[0]  # 随机生成一个左上角点,在范围以内
    if len(text_area) == 0:
        return h, w
    endpoints = get_endpoints((h, w), text_shape)

    for area in text_area:  # [[h_start,h_end],[w_start,w_end]]
        box1 = (h, w, h + text_shape[0], w + text_shape[1])
        # box2 = (area[0][0] - margin, area[1][0] - margin, area[1][0] + margin, area[1][1] + margin)
        if mat_inter(box1, area):
            return get_available_point(bg_shape, text_area, text_shape)
            # for p in endpoints:  # 所四个端点有一个在区域内的话
            #     if area[0][0] - margin < p[0] < area[0][1] + margin and area[1][0] - margin < p[1] < area[1][
            #         1] + margin:
            #         return get_available_point(bg_shape, text_area, text_shape)
    return h, w  # 点符合要求的话


def get_random_text_color():
    """
    获取随机字体颜色
    :return:
    """
    r = np.random.randint(180, 256, size=1)[0]
    g = np.random.randint(180, 256, size=1)[0]
    b = np.random.randint(190, 256, size=1)[0]
    return r, g, b


def resize_text_img(text_img):
    """
    重定义大小
    :param text_img:
    :return:
    """
    shape = text_img.shape
    value = np.random.randint(FORMAT_IMAGE_HEIGHT - 8, FORMAT_IMAGE_HEIGHT, 1)[0]
    if shape[0] < shape[1]:
        h = shape[0]
        ratio = h / value
        w = int(shape[1] / ratio)
        return cv2.resize(text_img, (w, value))
    else:
        w = shape[1]
        ratio = w / value
        h = int(shape[0] / ratio / 1.8)
        return cv2.resize(text_img, (int(value / 1.8), h))


def merge_image_template(bg_path, template_path_list):
    """
    合成文本模板和图片
    :param bg_path:
    :param template_path_list:
    :return:
    """
    bg = cv2.imread(bg_path)
    bg_shape = bg.shape
    text_area = []  # [[[h_start,h_end],[w_start,w_end]]。。。。。]
    region = []
    for template_path in template_path_list:
        text_img = cv2.imread(template_path)
        text_img = resize_text_img(text_img)
        text_shape = text_img.shape
        point = get_available_point(bg_shape, text_area, text_shape)
        text_area.append([[point[0], point[0] + text_shape[0]], [point[1], point[1] + text_shape[1]]])
        text_color = np.array(get_random_text_color())
        select_bg = bg[point[0]:point[0] + text_shape[0], point[1]: point[1] + text_shape[1], :]
        location = np.where(text_img > 120)
        for i in range(len(location[0])):
            select_bg[location[0][i], location[1][i], :] = text_color
        start_point = [int(point[0]), int(point[1])]
        end_point = [int(text_shape[0] + point[0]), int(point[1] + text_shape[1])]

        info = {"info": template_path, "p1": start_point, "p2": end_point}
        region.append(info)
    """保存相关图片和信息"""
    image_size = int(bg_shape[0]), int(bg_shape[1])
    file_name = str(uuid.uuid4())
    training_data_dir = GENERATE_DIE_PATH + '/training_data/'
    image_info = {'image_size': image_size, 'region': region, 'image_name': file_name + '.jpg'}
    save_image_path = training_data_dir + file_name + '.jpg'
    save_json_path = training_data_dir + file_name + '.json'
    save_img(bg, save_image_path)
    with open(save_json_path, 'w') as f:
        r = json.dumps(image_info)
        f.write(r)


def test():
    bg_path = 'F:/dataset/SUN397/SUN397/a/abbey/sun_aaalbzqrimafwbiv.jpg'
    template_path_list = [
        'F:/code/orc/dataset/gen/text_template/v_4_a/AAHI-c72338fb-7474-4fde-99b9-b5638dd16bbb.jpg',
        'F:/code/orc/dataset/gen/text_template/v_4_a/AAHI-c72338fb-7474-4fde-99b9-b5638dd16bbb.jpg',
    ]
    merge_image_template(bg_path, template_path_list)


def main():
    merge_image()
    # test()


if __name__ == '__main__':
    main()
