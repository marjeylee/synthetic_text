# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     get_rotate_image
   Description :
   Author :       'li'
   date：          2018/10/23
-------------------------------------------------
   Change Activity:
                   2018/10/23:
-------------------------------------------------
"""
# -*- coding:utf-8 -*-
import cv2
from math import *
import numpy as np
import math
import re

'''旋转图像并剪裁'''


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
    """
    resort points
    :param points:
    :return:
    """
    nearest_points = get_nearest_points(points)
    middle_points = get_middle_points(points, nearest_points)
    middle_angle = get_angle(middle_points)
    if -45 < middle_angle < 45:
        return horizontal_points(points, nearest_points, middle_points)
    else:
        return vertical_points(points, nearest_points, middle_points)


def get_rotate_angle(pt1, pt2, pt3, pt4):
    dis_1_2 = get_distance(pt1, pt2)
    dis_1_4 = get_distance(pt1, pt4)
    if dis_1_2 >= dis_1_4:
        heightRect = math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
        angle = acos((pt2[0] - pt1[0]) / heightRect) * (180 / math.pi)  # 矩形框旋转角度
        if not pt2[1] > pt1[1]:
            angle = -angle
    else:
        abs_h = abs(pt4[1] - pt1[1])
        angle = acos(abs_h / dis_1_4) * (180 / math.pi)
        if pt1[0] < pt4[0]:
            angle = -angle
    return angle


def get_rotate_img(img, pt1, pt2, pt3, pt4):
    """
    get rotate image
    :param img:
    :param pt1:
    :param pt2:
    :param pt3:
    :param pt4:
    :return:
    """
    angle = get_rotate_angle(pt1, pt2, pt3, pt4)
    height = img.shape[0]  # 原始图像高度
    width = img.shape[1]  # 原始图像宽度
    rotateMat = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)  # 按angle角度旋转图像
    heightNew = int(width * fabs(sin(radians(angle))) + height * fabs(cos(radians(angle))))
    widthNew = int(height * fabs(sin(radians(angle))) + width * fabs(cos(radians(angle))))

    rotateMat[0, 2] += (widthNew - width) / 2
    rotateMat[1, 2] += (heightNew - height) / 2
    imgRotation = cv2.warpAffine(img, rotateMat, (widthNew, heightNew), borderValue=(255, 255, 255))
    # cv2.imshow('rotateImg2', imgRotation)
    # cv2.waitKey(0)

    # 旋转后图像的四点坐标
    [[pt1[0]], [pt1[1]]] = np.dot(rotateMat, np.array([[pt1[0]], [pt1[1]], [1]]))
    [[pt3[0]], [pt3[1]]] = np.dot(rotateMat, np.array([[pt3[0]], [pt3[1]], [1]]))
    [[pt2[0]], [pt2[1]]] = np.dot(rotateMat, np.array([[pt2[0]], [pt2[1]], [1]]))
    [[pt4[0]], [pt4[1]]] = np.dot(rotateMat, np.array([[pt4[0]], [pt4[1]], [1]]))
    # 处理反转的情况
    if pt2[1] > pt4[1]:
        pt2[1], pt4[1] = pt4[1], pt2[1]
    if pt1[0] > pt3[0]:
        pt1[0], pt3[0] = pt3[0], pt1[0]
    imgOut = imgRotation[int(pt2[1]):int(pt4[1]), int(pt1[0]):int(pt3[0])]
    return imgOut  # rotated image


def drawRect(img, pt1, pt2, pt3, pt4, color, lineWidth):
    cv2.line(img, pt1, pt2, color, lineWidth)
    cv2.line(img, pt2, pt3, color, lineWidth)
    cv2.line(img, pt3, pt4, color, lineWidth)
    cv2.line(img, pt1, pt4, color, lineWidth)


# 　读出文件中的坐标值
def ReadTxt(directory, imageName, last):
    fileTxt = './1.txt'
    getTxt = open(fileTxt, 'r')  # 打开txt文件
    lines = getTxt.readlines()
    length = len(lines)
    for i in range(0, length, 4):
        pt2 = list(map(float, lines[i].split(' ')[:2]))
        pt1 = list(map(float, lines[i + 1].split(' ')[:2]))
        pt4 = list(map(float, lines[i + 2].split(' ')[:2]))
        pt3 = list(map(float, re.split('\n| ', lines[i + 3])[:2]))
        # float转int
        pt2 = list(map(int, pt2))
        pt1 = list(map(int, pt1))
        pt4 = list(map(int, pt4))
        pt3 = list(map(int, pt3))

        imgSrc = cv2.imread(imageName)
        drawRect(imgSrc, tuple(pt1), tuple(pt2), tuple(pt3), tuple(pt4), (0, 0, 255), 2)
        cv2.imshow("img", imgSrc)
        cv2.waitKey(0)
        get_rotate_img(imgSrc, pt1, pt2, pt3, pt4)

def main():
    image = cv2.imread('1.jpg')
    a = [218, 614, 335, 639, 326, 677, 209, 652]

    points = [a[0], a[1]], [a[2], a[3]], [a[4], a[5]], [a[6], a[7]]
    # points = [1620, 675], [1620, 456], [1655, 456], [1655, 675]  # [x,y]
    points = resort_points(points)
    get_rotate_img(image, points[0], points[1], points[2], points[3])


if __name__ == "__main__":
    main()
