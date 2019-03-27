# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     move_all_num
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

from utility.delete_file import delete_file_in_dir
from utility.file_path_utility import get_all_file_from_dir

num_path = 'E:\dataset/text_area/valid\class/4'
DES_path = 'E:\dataset/text_area/valid\class/4wrong/'


def main():
    for dirpath, dirnames, filenames in os.walk(num_path):
        for d in dirnames:
            sub_dir = os.path.join(dirpath, d)
            files = get_all_file_from_dir(sub_dir)
            if len(files) == 0:
                # delete_file_in_dir(sub_dir)
                print('delete' + sub_dir)
                continue
            _, image_name = os.path.split(files[0])
            is_delete = False
            for c in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
                if image_name.find(c) >= 0:
                    is_delete = True
                    break
            if len(files) < 2:
                for p in files:
                    _, file_name = os.path.split(p)
                    shutil.move(p, DES_path + file_name)


if __name__ == '__main__':
    main()
