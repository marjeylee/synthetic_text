# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     cp_file
   Description :
   Author :       'li'
   date：          2020/1/13
-------------------------------------------------
   Change Activity:
                   2020/1/13:
-------------------------------------------------
"""
import os
import random
import shutil

from utility.file_path_utility import get_all_files_under_directory


def main():
    source_dir = 'J:/car_door/original_image'
    door_side_dir = 'J:/car_door/to_class/door_side/'
    other_side_dir = 'J:/car_door/to_class/other_side/'
    paths = get_all_files_under_directory(source_dir)
    random.shuffle(paths)
    for index, path in enumerate(paths):
        _, name = os.path.split(path)
        # if index < 4810:
        #     continue
        if index % 10 == 0:
            print(index)
        if 'Pos' in name:
            continue
        print(path)
        if 'Front' in name:
            des_path = door_side_dir + name
            shutil.copy(path, des_path)
        elif 'Rear' in name:
            des_path = other_side_dir + name
            shutil.copy(path, des_path)


if __name__ == '__main__':
    main()
