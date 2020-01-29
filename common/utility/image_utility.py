"""
image common function
"""
# -*- coding: utf-8 -*-
import cv2 as cv


def show_img(new_img):
    """
    显示图片
    :param new_img:
    :return:
    """
    cv.imshow("Image", new_img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def save_img(img, path):
    """
    保存图片
    :param img:图片
    :param path: 路径
    :return:
    """
    cv.imwrite(path, img)
