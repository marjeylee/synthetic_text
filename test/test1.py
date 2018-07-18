# -*- coding:utf-8 -*-

"""
* 0010
    使用 Python 生成类似于下图中的字母验证码图片
    2017/1/28
"""
import uuid

import numpy as np

import cv2
import random
from PIL import Image, ImageDraw, ImageFont

from utility import combine_file_path


def randomColor():
    r = random.randint(200, 256)
    g = random.randint(200, 256)
    b = random.randint(200, 256)
    return r, g, b


def colorDifference(bg_color, text_color):
    d = 0
    for i in range(0, 3):
        d += (text_color[i] - bg_color[i]) ^ 2
    return d


root = "0123456789 QWERTYUIOPLKJHGFDSAZXCVBNM"

# bgImg = Image.open("background.png")
# bgImg.show()

font = ImageFont.truetype(combine_file_path('F:/code/orc/dataset/TTF_Files/Fenix-Regular.ttf'),
                          30)  # 创建字体对象给ImageDraw中的text函数使用


def show_img(img):
    """
    显示图片
    :param img:
    :return:
    """
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)


def generate_bg(num_bg_images):
    global bg
    found = False
    while not found:
        fname = "../bgs/{:08d}.jpg".format(random.randint(0, num_bg_images - 1))
        bg = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
        if (bg.shape[1] >= 32 and
                bg.shape[0] >= 100):
            found = True
    """随机生成一个区域"""
    x = random.randint(0, bg.shape[1] - 100)
    y = random.randint(0, bg.shape[0] - 32)
    bg = bg[y:y + 32, x:x + 100]
    """新生成的文本区域"""
    return bg


for j in range(0, 80000):
    ans = ""
    for i in range(0, j % 9):
        ans += random.choice(root)
    # print(ans)

    bg_color = randomColor()
    bgImg = Image.new('RGB', (100, 32), (0, 0, 0))  # 新建一个图片对象, 背景颜色随机
    # bgImg.show()
    canvas = ImageDraw.Draw(bgImg)

    # text_color = randomColor()
    # while colorDifference(bg_color, text_color) < 100:  # 让字体颜色和背景颜色反差大一些，以防看不清
    text_color = randomColor()

    canvas.text((0, 0), 'DSJKALD5', text_color, font)
    bgImg.show()
    uuid_str = str(uuid.uuid4())
    name = ans + '-' + uuid_str + '.jpg'
    name = name.replace(' ', '', 10)  # 去掉空格
    bgImg.save('tmp', 'jpeg')
    text_img = cv2.imread('tmp', cv2.IMREAD_GRAYSCALE)
    bg_pic = generate_bg(100000)
    if j % 3 == 0:
        bg_pic[text_img > 190] = np.random.choice(range(0, 30), 1)[0]
    else:
        bg_pic[text_img > 190] = np.random.choice(range(190, 256), 1)[0]
    cv2.imwrite('F:/code/orc/dataset/4_alpha/' + name, bg_pic)
    print(j)
    #
    # inp = input('Please type in the characters in the image:')
    # while inp != ans:
    #     inp = input('Incorrect input. Please try again:')
