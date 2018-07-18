"""
裁剪图片
"""
import numpy as np

from gen.gen_char_image import get_all_orig_char_path
from gen.gen_rotate_char import gen_normal_rotate_image


def clip_image(image):
    """
    裁剪图片
    :param image:
    :return:
    """
    p1, p2 = [0, 0], [1, 1]
    points = np.where(image > 200)
    p1[0] = np.min(points[0])
    p2[0] = np.max(points[0])
    p1[1] = np.min(points[1])
    p2[1] = np.max(points[1])
    image = image[p1[0] - 1:p2[0] + 1, p1[1] - 1: p2[1] + 1, :]
    return image


def main():
    file_paths = get_all_orig_char_path()
    for path in file_paths:
        image = gen_normal_rotate_image(path)
        image = clip_image(image)


if __name__ == '__main__':
    main()
