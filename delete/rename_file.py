# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     rename_file
   Description :
   Author :       'li'
   date：          2018/11/6
-------------------------------------------------
   Change Activity:
                   2018/11/6:
-------------------------------------------------
"""
import os
import shutil
import uuid

from utility.file_path_utility import get_all_file_from_dir, create_dir

ori_path = 'D:\dataset\delete/'

des_path = 'C:/Users\lr\Desktop/de/'


def main():
    index = 0
    paths = get_all_file_from_dir(ori_path)

    for index, p in enumerate(paths):
        seg = int(index / 2000) + 1
        _, name = os.path.split(p)
        label = name.split('-')[0]
        new_name = str(index) + '-' + str(uuid.uuid4()) + '.jpg'
        index += 1
        d_path = des_path + new_name
        shutil.copy(p, d_path)


if __name__ == '__main__':
    main()
