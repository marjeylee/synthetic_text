"""
utility module
"""
# -*- coding: utf-8 -*-
import cv2 as cv

from common.utility.file_path_utility import combine_file_path


def load_img_to_numpy(img_path):
    """
    加载图片为ndarray格式
    :param img_path:
    :return:
    """
    return cv.imread(img_path)


def clip_img(img, start, end):
    """
    裁剪图片
    :param img:ndarray格式的图片
    :param start: 起始位置:左上角点
    :param end: 结束位置：右下角点
    :return:
    """
    new_img = img[start[0]:end[0], start[1]:end[1], :]
    return new_img


def show_img(new_img):
    """
    显示图片
    :param new_img:
    :return:
    """
    cv.imshow("Image", new_img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def load_img_to_gray(img):
    """
    转变成灰度图片
    :param img:
    :return:
    """
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


def get_train_slip_img(x, y):
    """
    获得训练集数据
    :param x:
    :param y:
    :return:
    """
    path = combine_file_path('data/img/12.jpg')
    img = load_img_to_numpy(path)
    new_im = clip_img(img, (x, y), (x + 256, y + 256))
    gray_im = load_img_to_gray(new_im)
    return gray_im, new_im
