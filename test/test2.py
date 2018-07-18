import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np
from pylab import *


def show_img(new_img):
    """
    显示图片
    :param new_img:
    :return:
    """
    cv2.imshow("Image", new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def rotate(image, angle, center=None, scale=1.0):  # 1
    (h, w) = image.shape[:2]  # 2
    if center is None:  # 3
        center = (w // 2, h // 2)  # 4

    M = cv2.getRotationMatrix2D(center, angle, scale)  # 5

    rotated = cv2.warpAffine(image, M, (w, h))  # 6
    return rotated  # 7


font = ImageFont.truetype('F:/code/orc/dataset/TTF_Files/Fenix-Regular.ttf', 100)
im = Image.new("RGB", (200, 200))
draw = ImageDraw.Draw(im)
x, y = (10, 10)
draw.text((x, y), 'Y', font=font)
offsetx, offsety = font.getoffset('3')
width, height = font.getsize('3')
im = np.array(im)
cv2.rectangle(im, (offsetx + x, offsety + y), (offsetx + x + width, height + offsety), (255, 255, 255), 1)  # 绘出矩形框
im = rotate(im, -1)
im = cv2.GaussianBlur(im, (51, 51), 0)
show_img(im)
