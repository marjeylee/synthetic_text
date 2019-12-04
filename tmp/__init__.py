# --------------------------
"""
@author:Sui yue
@describe: 对比增强，线性变换
@time: 2019/09/15 14:21:44
"""
import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 主函数

if __name__ == "__main__":
    # 读图像
    I = cv2.imread('1.jpg')
    # 线性变换
    a = 0.6
    O = float(a) * I
    O[0 > 255] = 255
    # 数据类型转换
    O = np.round(O)
    cv2.imwrite('2.jpg', O)
