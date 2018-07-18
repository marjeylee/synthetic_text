"""
生成旋转的图片
"""
import cv2

from gen.gen_char_image import get_all_orig_char_path
from utility.normal_distribution import get_normal_data


def rotate_img(image, angle, center=None, scale=1.0):
    """
    以图片中心为原点旋转图片
    :param image: 图片
    :param angle: 度数
    :param center: 中点
    :param scale: 范围
    :return:
    """
    (h, w) = image.shape[:2]
    if center is None:
        center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)

    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


def gen_normal_rotate_image(image_path):
    """
    产生一个随机旋转角度的图像
    :param image_path:
    :return:
    """
    image = cv2.imread(image_path)
    mu, sigma, sample_nom = 0, 4, 1
    angle = get_normal_data(mu, sigma, sample_nom)
    image = rotate_img(image, angle)
    return image


def main():
    file_paths = get_all_orig_char_path()
    for path in file_paths:
        gen_normal_rotate_image(path)


if __name__ == '__main__':
    main()
