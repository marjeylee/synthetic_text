"""
生成背景
"""
import cv2
import numpy as np

from config import *
from utility.file_path_utility import get_all_file_from_dir


def get_background_path():
    """
    获取背景图路径
    :return:
    """
    return get_all_file_from_dir(BACKGROUND_DIR_PATH)


bg_paths = get_background_path()


def gen_background():
    """
    生成背景
    :return:
    """
    path = np.random.choice(bg_paths, 1)[0]
    img = cv2.imread(path)
    shape = img.shape
    max_h = shape[0] - FORMAT_IMAGE_HEIGHT
    max_w = shape[1] - FORMAT_IMAGE_WIDTH
    h = np.random.randint(0, max_h)
    w = np.random.randint(0, max_w)
    return img[h:h + FORMAT_IMAGE_HEIGHT, w:w + FORMAT_IMAGE_WIDTH, :]


def main():
    gen_background()


if __name__ == '__main__':
    main()
