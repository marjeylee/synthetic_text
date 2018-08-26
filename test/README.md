---
title: python数字图像处理-图像噪声与去噪算法
date: 2017-12-16 17:19:29
tags:
---

# python数字图像处理-图像噪声与去噪算法

![figure_1.png](https://i.loli.net/2017/12/16/5a34e6accc01f.png)

## 图像噪声

### 椒盐噪声

**概述：** 椒盐噪声（salt & pepper noise）是数字图像的一个常见噪声，所谓椒盐，椒就是黑，盐就是白，椒盐噪声就是在图像上随机出现黑色白色的像素。椒盐噪声是一种因为信号脉冲强度引起的噪声，产生该噪声的算法也比较简单。

给一副数字图像加上椒盐噪声的步骤如下：

1. 指定信噪比 SNR （其取值范围在[0, 1]之间）
2. 计算总像素数目 SP， 得到要加噪的像素数目 NP = SP * (1-SNR)
3. 随机获取要加噪的每个像素位置P（i, j）
4. 指定像素值为255或者0。
5. 重复3,4两个步骤完成所有像素的NP个像素
6. 输出加噪以后的图像



### 高斯噪声

**概述：** 加性高斯白噪声(Additive white Gaussian noise，AWGN)在通信领域中指的是一种功率谱函数是常数(即白噪声), 且幅度服从高斯分布的噪声信号. 这类噪声通常来自感光元件, 且无法避免.

## 去噪算法

### 中值滤波

**概述：** 中值滤波是一种非线性空间滤波器, 它的响应基于图像滤波器包围的图像区域中像素的统计排序, 然后由统计排序结果的值代替中心像素的值. 中值滤波器将其像素邻域内的灰度中值代替代替该像素的值. 中值滤波器的使用非常普遍, 这是因为对于一定类型的随机噪声, 它提供了一种优秀的去噪能力, 比小尺寸的均值滤波器模糊程度明显要低. 中值滤波器对处理脉冲噪声(也称椒盐噪声)非常有效, 因为该噪声是以黑白点叠加在图像上面的.

与中值滤波相似的还有最大值滤波器和最小值滤波器.

### 均值滤波

**概述：** 均值滤波器的输出是包含在滤波掩模领域内像素的简单平均值. 均值滤波器最常用的目的就是减噪. 然而, 图像边缘也是由图像灰度尖锐变化带来的特性, 所以均值滤波还是存在不希望的边缘模糊负面效应.

均值滤波还有一个重要应用, 为了对感兴趣的图像得出一个粗略描述而模糊一幅图像. 这样, 那些较小物体的强度与背景揉合在一起了, 较大物体变得像斑点而易于检测.掩模的大小由即将融入背景中的物体尺寸决定.

### 代码

见[https://github.com/wangshub/python-image-process](https://github.com/wangshub/python-image-process)
