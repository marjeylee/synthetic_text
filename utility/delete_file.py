# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     delete_file
   Description :
   Author :       'li'
   date：          2018/8/19
-------------------------------------------------
   Change Activity:
                   2018/8/19:
-------------------------------------------------
"""
import os
import shutil

from utility.rename_file import get_all_file_from_dir





def delete_file_in_dir(dir_path):
    paths = get_all_file_from_dir(dir_path)

    for index, p in enumerate(paths):
        try:
            if index % 1000 == 0:
                print(index)
            os.remove(p)
        except Exception as e:
            print(e)


if __name__ == '__main__':

    dir_path = 'D:/label_result_2020_3_10/container_num_text_area/vertical_or/'
    shutil.rmtree(dir_path)
    # delete_file_in_dir(dir_path)
