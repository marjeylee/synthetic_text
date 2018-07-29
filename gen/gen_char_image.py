"""
产生字符图片
"""
import random
import uuid

import numpy as np
from PIL import ImageFont, Image, ImageDraw

from config import *
from utility.file_path_utility import get_all_files_under_directory, create_dir, get_all_file_from_dir
from utility.image_utility import save_img


def get_fonts_paths():
    """
    获取字体格式文件路径
    :return:
    """
    file_name = get_all_files_under_directory(FONTS_DIR_PATH)
    fonts_paths = []
    for i in range(CHOOSE_FONTS_SIZE):
        files = random.choice(file_name)
        fonts_paths.append(files)
    return fonts_paths


def save_orig_char(im, char):
    """
    保存生成的原始图片
    :param im:
    :param char:
    :return:
    """
    dir_path = GENERATE_ORIG_CHAR_DIE_PATH + char + '/'
    create_dir(dir_path)

    path = dir_path + str(uuid.uuid4()) + '.jpg'
    save_img(im, path)


def gen_chars():
    """
    生成字符图片
    :return:
    """
    fonts_paths = get_fonts_paths()
    font_path = random.choice(fonts_paths)
    font = ImageFont.truetype(font_path, FONT_SIZE)
    im = Image.new("RGB", (FONT_SIZE * 2, FONT_SIZE * 2))
    draw = ImageDraw.Draw(im)
    x, y = (FONT_SIZE * 0.5, FONT_SIZE * 0.5)
    char = random.choice(GENERATE_CHARACTER)
    draw.text((x, y), char, font=font)
    im = np.array(im)
    save_orig_char(im, char)


def get_all_orig_char_path():
    """
    获取所有初始图片文本
    :return:
    """
    dir_path = GENERATE_DIE_PATH + 'orig'
    file_paths = get_all_file_from_dir(dir_path)
    return file_paths


def main():
    for i in range(100000):
        print(i)
        gen_chars()


if __name__ == '__main__':
    main()
