# -*- coding: utf-8 -*-
"""
获取工程绝对路径
"""
import os

PROJECT_PATH = None


def get_absolute_project_path():
    """
    获取项目的绝对路径，在此列中，是在dm层
    :return:
    """
    global PROJECT_PATH
    if PROJECT_PATH is None:
        path = os.path.realpath(__file__)
        utility_path = os.path.split(path)[0]
        common_path = os.path.split(utility_path)[0]
        PROJECT_PATH = os.path.split(common_path)[0]
    return PROJECT_PATH


def combine_file_path(relative_path):
    """
    相对路径与绝对路径合成
    :param relative_path:
    :return:
    """
    return os.path.join(get_absolute_project_path(), relative_path)


def get_all_files_under_directory(directory):
    """
    获取路径下的所有文件
    :param directory:
    :return:
    """
    files_list = []
    for root, _, files in os.walk(directory, topdown=False):  # topdown 优先遍历同等级
        for name in files:
            files_list.append(os.path.join(root, name))
    return files_list


def get_all_file_from_dir(path_dir):
    """
    遍历获得所有文件夹和子文件夹下的文件
    :param path_dir:
    :return:
    """
    file_path = []
    if os.path.exists(path_dir):
        path_dir = os.path.abspath(path_dir)
        for i in os.listdir(path_dir):
            path_i = os.path.join(path_dir, i)
            if os.path.isfile(path_i):
                file_path.append(path_i)
            else:
                file_path.extend(get_all_file_from_dir(path_i))
    return file_path


def create_dir(dir_path):
    """
    create directory
    :param dir_path:
    :return:
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def _main():
    """
    main
    :return:
    """
    project_path = get_absolute_project_path()
    print(project_path)


if __name__ == '__main__':
    _main()

    # data_path = combine_file_path('./national_medicine/data')
    # files = get_all_files_under_directory(data_path)
