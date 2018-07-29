"""
生成图片文本模板
"""

import uuid

import cv2
import numpy as np

from config import FORMAT_IMAGE_HEIGHT, FORMAT_IMAGE_WIDTH, GENERATE_DIE_PATH
from gen.clip_image import clip_image
from gen.gen_background import gen_background
from gen.gen_char_image import get_all_orig_char_path, CHAR_MAX_NUM_PER_IMAGE
from gen.gen_rotate_char import gen_normal_rotate_image
from utility import show_img
from utility.image_utility import save_img
from utility.normal_distribution import get_normal_data

orig_file_path = get_all_orig_char_path()


def get_random_orig_image_path():
    path = np.random.choice(orig_file_path, 1)[0]
    strs = str(path).split('\\')
    if len(strs[-2]) > 2:
        raise Exception('字符解析出错')
    return path, strs[-2]
    pass


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
            random_margin = int(get_normal_data(10, 3, 1))
            margin = np.zeros((0, random_margin, 3), dtype=np.int)
            img = horizontal_splicing_picture(img, margin)
            img = horizontal_splicing_picture(img, images[i])
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
        rotate_img = gen_normal_rotate_image(path)
        rotate_img = clip_image(rotate_img)
        images.append(rotate_img)
        label.append(char)
    if len(images) > 0:
        text_image = combine_horizontal_image(images)
        label_str = ''
        for l in label:
            label_str = label_str + l
        return text_image, label_str
    else:
        return None


def gen_template_text_image():
    """
    生成模板文件主方法
    :return:
    """
    text_img, label = get_rotate_chars()
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


def main():
    for i in range(1000000):
        try:
            print(i)
            text_img, label = gen_template_text_image()
            background = gen_background()
            if i % 3 == 0:
                background[text_img > 150] = np.random.choice(range(0, 30), 1)[0]
            else:
                background[text_img > 150] = np.random.choice(range(200, 255), 1)[0]
            path = GENERATE_DIE_PATH + '/data/' + label + '-' + str(uuid.uuid4()) + '.jpg'
            save_img(background, path)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
