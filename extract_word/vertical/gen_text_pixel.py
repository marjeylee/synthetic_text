# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     gen_text_pixel
   Description :
   Author :       'li'
   date：          2018/11/4
-------------------------------------------------
   Change Activity:
                   2018/11/4:
-------------------------------------------------
"""

import cv2
from sklearn.cluster import k_means
import numpy as np


def to_gray(copy_img):
    return cv2.cvtColor(copy_img, cv2.COLOR_BGR2GRAY)


def get_txt_pixels(img):
    shape = img.shape
    gray_img = to_gray(img)
    gray_img = gray_img.reshape(gray_img.size, 1)
    kmeans = k_means(gray_img, n_clusters=2)
    kmeans = kmeans[1].reshape((shape[0], shape[1]))
    zeros_pos = np.where(kmeans == 0)
    ones_pos = np.where(kmeans == 1)
    if not zeros_pos[0].size > ones_pos[0].size:
        kmeans[zeros_pos] = 1
        kmeans[ones_pos] = 0
    cv2.imwrite('c' + str(1) + '.jpg', kmeans * 255)
    return kmeans


def main():
    path = 'seg0.jpg'
    img = cv2.imread(path)
    txt_pixels = get_txt_pixels(img)
    ones_pos = np.where(txt_pixels == 0)
    # img[:, :, :] = 180
    img[ones_pos] = 112

    cv2.imwrite('b.jpg', img)


if __name__ == '__main__':
    main()
