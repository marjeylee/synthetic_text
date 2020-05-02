# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     get_img
   Description :
   Author :       'li'
   date：          2020/1/10
-------------------------------------------------
   Change Activity:
                   2020/1/10:
-------------------------------------------------
"""
import os
import shutil

from common.utility.file_path_utility import get_all_files_under_directory

names = {'truck20200110152407365.jpg', 'truck20200110144814840.jpg', 'truck20200110152344196.jpg',
         'truck20200110144834899.jpg', 'truck20200110152033256.jpg', 'truck20200110160146216.jpg',
         'truck20200110150544529.jpg', 'truck20200110153759285.jpg', 'truck20200110144826549.jpg',
         'truck20200110150652291.jpg', 'truck20191231211420468.jpg', 'truck20200110153807638.jpg',
         'truck20200110151828896.jpg', 'truck20200110150347879.jpg', 'truck20191231211539293.jpg',
         'truck20200110152427654.jpg', 'truck20200110152328351.jpg', 'truck20191231211631648.jpg',
         'truck20200110150557630.jpg', 'truck20191231211632195.jpg', 'truck20200110152306498.jpg',
         'truck20191231211542825.jpg', 'truck20191231211540324.jpg', 'truck20200110150638314.jpg',
         'truck20200110150534700.jpg', 'truck20200110153752609.jpg', 'truck20191231211342723.jpg',
         'truck20200110150607462.jpg', 'truck20191231211345319.jpg', 'truck20191231211833759.jpg',
         'truck20200110151835108.jpg', 'truck20200110150604185.jpg', 'truck20200110160210409.jpg',
         'truck20191231211632336.jpg', 'truck20200110151831769.jpg', 'truck20200110145225796.jpg',
         'truck20200110150344537.jpg', 'truck20191231211629164.jpg', 'truck20200110150537981.jpg',
         'truck20200110152430774.jpg', 'truck20200110140232061.jpg', 'truck20200110144806497.jpg',
         'truck20191231211342098.jpg', 'truck20200110140254697.jpg', 'truck20200110152325229.jpg',
         'truck20191231211541653.jpg', 'truck20200110152946843.jpg', 'truck20200110145235812.jpg',
         'truck20200110153809307.jpg', 'truck20200110145219119.jpg', 'truck20200110140243713.jpg',
         'truck20200110144823203.jpg', 'truck20200110150551081.jpg', 'truck20200110152426095.jpg',
         'truck20200110150554355.jpg', 'truck20200110150346207.jpg', 'truck20191231211833259.jpg',
         'truck20200110150647706.jpg', 'truck20200110150641593.jpg', 'truck20200110160323095.jpg',
         'truck20200110152036594.jpg', 'truck20200110150635039.jpg', 'truck20200110151545738.jpg',
         'truck20191231211733481.jpg', 'truck20200110150547804.jpg', 'truck20191231211341284.jpg',
         'truck20200110144829889.jpg', 'truck20191231211603303.jpg', 'truck20191231211732449.jpg',
         'truck20191231211629039.jpg', 'truck20200110153857806.jpg', 'truck20200110151915325.jpg',
         'truck20200110152322108.jpg', 'truck20200110151847717.jpg', 'truck20200110144811503.jpg',
         'truck20200110140224278.jpg', 'truck20200110154023030.jpg', 'truck20200110145158765.jpg',
         'truck20200110145229135.jpg', 'truck20200110152303377.jpg', 'truck20200110153757616.jpg'}

dir_path = 'J:/BaiduNetdiskDownload/wuhu_car_num/all'
des_dir = 'J:/BaiduNetdiskDownload/wuhu_car_num/left/'
img_paths = get_all_files_under_directory(dir_path)
for index, path in enumerate(img_paths):
    _, name = os.path.split(path)
    # name = name.replace('.jpg', '')
    if name in names:
        print(index)
        des_path = des_dir + name + '.jpg'
        shutil.copy(path, des_path)
