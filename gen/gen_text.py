# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     gen_text
   Description :
   Author :       'li'
   date：          2018/7/24
-------------------------------------------------
   Change Activity:
                   2018/7/24:
-------------------------------------------------
生成黑底白字文本
"""
import os

__author__ = 'li'

import uuid

import cv2
import numpy as np

from config import FORMAT_IMAGE_HEIGHT, FORMAT_IMAGE_WIDTH, GENERATE_DIE_PATH, ALPHA_CHARACTER, NUM_CHARACTER
from gen.clip_image import clip_image
from gen.gen_char_image import get_all_orig_char_path, CHAR_MAX_NUM_PER_IMAGE
from gen.gen_rotate_char import *
from utility import show_img
from utility.image_utility import save_img
from utility.normal_distribution import get_normal_data

orig_file_path = get_all_orig_char_path()


def get_random_orig_image_path(scale=None):
    path = np.random.choice(orig_file_path, 1)[0]
    strs = str(path).split('\\')
    label = strs[-2]
    if len(label) > 2:
        raise Exception('字符解析出错')
    if scale is not None:
        if str(scale).find(label) > 0:
            return path, strs[-2]
    return get_random_orig_image_path(scale=scale)


def combine_horizontal_image(images):
    """
    图片合成
    :param images:
    :return:
    """
    img_size = len(images)
    if img_size > 0:
        offset = np.zeros((0, 1, 3), dtype=np.int)
        img = horizontal_splicing_picture(offset, images[0])
        for i in range(1, img_size):
            random_margin = int(get_normal_data(5, 3, 1))  # 随机间隔
            if random_margin < 0:
                random_margin = 0
            margin = np.zeros((0, random_margin, 3), dtype=np.int)
            img = horizontal_splicing_picture(img, margin)
            img = horizontal_splicing_picture(img, images[i])
        return img
    return None


def vertical_splicing_picture(img1, img2):
    """
        垂直拼接两张图片
        :param img1:
        :param img2:
        :return:
        """
    shape1 = img1.shape
    shape2 = img2.shape
    w = shape1[1]
    if shape1[1] < shape2[1]:  # 第二张图片宽的话
        w = shape2[1]
    bg = np.zeros((shape1[0] + shape2[0], w, 3), dtype=np.int)
    bg[0:shape1[0], int((w - shape1[1]) / 2):int((w - shape1[1]) / 2) + shape1[1], :] = img1
    bg[shape1[0]:shape1[0] + shape2[0], int((w - shape2[1]) / 2):int((w - shape2[1]) / 2) + shape2[1], :] = img2
    return bg


def combine_vertical_image(images):
    """
    图片垂直方向合成
    :param images:
    :return:
    """
    img_size = len(images)
    if img_size > 0:
        offset = np.zeros((1, 1, 3), dtype=np.int)  # 垂直方向padding
        img = vertical_splicing_picture(offset, images[0])
        for i in range(1, img_size):
            random_margin = int(get_normal_data(2, 3, 1))  # 随机间隔
            if random_margin < 0:
                random_margin = 0
            margin = np.zeros((0, random_margin, 3), dtype=np.int)
            img = vertical_splicing_picture(img, margin)
            img = vertical_splicing_picture(img, images[i])
        return img
    return None


def get_rotate_chars():
    """
    获取旋转过经过裁剪的图片
    :return:
    """
    num = np.random.randint(1, CHAR_MAX_NUM_PER_IMAGE + 1, dtype=int)  # 最少生成一个图片
    images = []
    label = []
    for i in range(num):  # 最多获取10个字符
        path, char = get_random_orig_image_path()
        rotate_image = gen_normal_rotate_image(path)
        rotate_image = clip_image(rotate_image)
        images.append(rotate_image)
        label.append(char)
    if len(images) > 0:
        text_image = combine_horizontal_image(images)
        label_str = ''
        for l in label:
            label_str = label_str + l
        return text_image, label_str
    else:
        return None


def get_random_size_img():
    """
    生成模板文件主方法
    :return:
    """
    text_img, label = get_rotate_chars()
    cv2.imwrite('./tmp4.jpg', text_img)
    shape = text_img.shape
    format_height = int(shape[1] * (shape[0] / FORMAT_IMAGE_WIDTH))
    if format_height > FORMAT_IMAGE_WIDTH:  # 压缩
        cv2.imwrite('./tmp4.jpg', text_img)
        text_img = cv2.imread('./tmp4.jpg')
        text_img = cv2.resize(text_img, (FORMAT_IMAGE_WIDTH, FORMAT_IMAGE_HEIGHT))
    else:
        radio = FORMAT_IMAGE_WIDTH / FORMAT_IMAGE_HEIGHT
        width = int(radio * shape[0])
        res = width - shape[1]
        res_arr = np.zeros((shape[0], res, 3), dtype=np.int)
        text_img = np.concatenate((text_img, res_arr), axis=1)
        cv2.imwrite('./tmp4.jpg', text_img)
        text_img = cv2.imread('./tmp4.jpg')
        text_img = cv2.resize(text_img, (FORMAT_IMAGE_WIDTH, FORMAT_IMAGE_HEIGHT))
    return text_img, label


def horizontal_splicing_picture(img1, img2):
    """
    水平拼接两张图片
    :param img1:
    :param img2:
    :return:
    """
    shape1 = img1.shape
    shape2 = img2.shape
    h = shape1[0]
    if shape1[0] < shape2[0]:  # 第二张图片高的话
        h = shape2[0]
    bg = np.zeros((h, shape1[1] + shape2[1], 3), dtype=np.int)
    bg[h - shape1[0]:h, 0:shape1[1], :] = img1
    bg[h - shape2[0]:h, shape1[1]:shape2[1] + shape1[1], :] = img2
    return bg


def gen_4_alpha_data():
    """
    产生四个字母数字
    :return:
    """
    images = []
    label = []
    for i in range(4):  # 最多获取10个字符
        path, char = get_random_orig_image_path(scale=ALPHA_CHARACTER)
        rotate_image = gen_normal_rotate_image(path)
        rotate_image = clip_image(rotate_image)
        images.append(rotate_image)
        label.append(char)
    return images, label


def generate_horizontal_image(img, labels):
    """
    通过每个字符的图片合成水平图
    :param img:
    :param labels:
    :return:
    """
    text_image = combine_horizontal_image(img)
    label_str = ''
    for l in labels:
        label_str = label_str + l
    return text_image, label_str


def gen_6_num_data():
    """
        产生10个数字
        :return:
        """
    images = []
    label = []
    for i in range(6):  # 最多获取10个字符
        path, char = get_random_orig_image_path(scale=NUM_CHARACTER)
        rotate_image = gen_normal_rotate_image(path)
        rotate_image = clip_image(rotate_image)
        images.append(rotate_image)
        label.append(char)
    return images, label


def rotate_text_image(text_image):
    """
    整块文字区域旋转一定的角度
    :param text_image:
    :return:
    """
    mu, sigma, sample_nom = 0, 2, 1
    angle = get_normal_data(mu, sigma, sample_nom)
    return rotate_img(text_image, angle)


def gen_alpha_num_mix_data():
    """
    生成类似AD2F的数据
    :return:
    """
    images = []
    label = []
    for i in range(4):  # 最多获取10个字符
        path, char = get_random_orig_image_path(scale=ALPHA_CHARACTER)
        if i == 2:
            path, char = get_random_orig_image_path(scale=NUM_CHARACTER)
        rotate_image = gen_normal_rotate_image(path)
        rotate_image = clip_image(rotate_image)
        images.append(rotate_image)
        label.append(char)
    return images, label


def gen_10_alpha_num_mix_data():
    """
    生成类似AD2F的数据
    :return:
    """
    images = []
    label = []
    for i in range(10):  # 最多获取10个字符
        path = ''
        char = ''
        if i < 4:
            path, char = get_random_orig_image_path(scale=ALPHA_CHARACTER)
        if 4 <= i < 10:
            path, char = get_random_orig_image_path(scale=NUM_CHARACTER)
        rotate_image = gen_normal_rotate_image(path)
        rotate_image = clip_image(rotate_image)
        images.append(rotate_image)
        label.append(char)
    return images, label


def gen_horizontal_image_template():  #
    """
    产生垂直模板
    :return:
    """
    img, labels = gen_4_alpha_data()
    text_image, label_str = generate_horizontal_image(img, labels)
    format_and_save(text_image, label_str, 'h_4_a')
    """合成是个字母"""
    img, labels = gen_6_num_data()
    text_image, label_str = generate_horizontal_image(img, labels)
    format_and_save(text_image, label_str, 'h_6_n')
    """合成四个字母和数据"""
    img, labels = gen_alpha_num_mix_data()
    text_image, label_str = generate_horizontal_image(img, labels)
    format_and_save(text_image, label_str, 'h_4_an')
    """合成10个字母和数据"""
    img, labels = gen_10_alpha_num_mix_data()
    text_image, label_str = generate_horizontal_image(img, labels)
    format_and_save(text_image, label_str, 'h_10_an')


def generate_vertical_image(img, labels):
    """
    合并垂直方向字符
    :param img:
    :param labels:
    :return:
    """
    text_image = combine_vertical_image(img)
    label_str = ''
    for l in labels:
        label_str = label_str + l
    return text_image, label_str


def format_and_save(text_image, label_str, classify):
    """
    模板图片预处理和保存
    :param text_image:
    :param label_str:
    :param classify:
    :return:
    """
    cv2.imwrite('./tmp2.jpg', text_image)
    text_image = cv2.imread('./tmp2.jpg')
    text_image = rotate_text_image(text_image)
    text_image = clip_image(text_image)
    dir_path = GENERATE_DIE_PATH + 'text_template/' + classify + '/'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = dir_path + label_str + '-' + str(uuid.uuid4()) + '.jpg'
    cv2.imwrite(file_path, text_image)


def gen_vertical_image_template():
    """
    产生垂直模板
    :return:
    """
    img, labels = gen_4_alpha_data()
    text_image, label_str = generate_vertical_image(img, labels)
    format_and_save(text_image, label_str, 'v_4_a')
    """合成是个字母"""
    img, labels = gen_6_num_data()
    text_image, label_str = generate_vertical_image(img, labels)
    format_and_save(text_image, label_str, 'v_6_n')
    """合成四个字母和数据"""
    img, labels = gen_alpha_num_mix_data()
    text_image, label_str = generate_vertical_image(img, labels)
    format_and_save(text_image, label_str, 'v_4_an')
    """合成10个字母和数据"""
    img, labels = gen_10_alpha_num_mix_data()
    text_image, label_str = generate_vertical_image(img, labels)
    format_and_save(text_image, label_str, 'v_10_an')


def gen_format_text_template():
    for i in range(1000000):
        print(i)
        try:
            gen_horizontal_image_template()
            gen_vertical_image_template()
        except Exception as e:
            print(e)
        continue
        # try:
        #     print(i)
        #     text_img, label = get_random_size_img()
        #     background = gen_background()
        #     if i % 3 == 0:
        #         background[text_img > 150] = np.random.choice(range(0, 30), 1)[0]
        #     else:
        #         background[text_img > 150] = np.random.choice(range(200, 255), 1)[0]
        #     path = GENERATE_DIE_PATH + '/data/' + label + '-' + str(uuid.uuid4()) + '.jpg'
        #     save_img(background, path)
        # except Exception as e:
        #     print(e)


def main():
    gen_format_text_template()


if __name__ == '__main__':
    main()
