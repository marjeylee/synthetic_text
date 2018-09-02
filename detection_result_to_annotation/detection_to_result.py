# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     detection_to_result
   Description :
   Author :       'li'
   date：          2018/8/31
-------------------------------------------------
   Change Activity:
                   2018/8/31:
-------------------------------------------------
"""
import json
import os

from utility.file_io_utility import read_all_content
from utility.file_path_utility import get_all_file_from_dir, create_dir
from xml.dom.minidom import Document

__author__ = 'li'

result_dir_path = 'F:\BaiduNetdiskDownload/results'
result_paths = get_all_file_from_dir(result_dir_path)
save_annotation_dir = 'F:\BaiduNetdiskDownload/annotation/'
create_dir(save_annotation_dir)


def load_result(result_paths):
    """
    load result
    :param result_paths:
    :return:
    """
    objs = []
    for p in result_paths:
        json_str = read_all_content(p)
        json_obj = json.loads(json_str)
        save_annotation(json_obj)
        objs.append(json_obj)
    return objs


def save_annotation(result):
    """
    save annotation xml
    :param result:
    :return:
    """
    text_lines = result['text_lines']
    if len(text_lines) == 0:
        return
    image_path = result['original_image_path']
    dir_path, file_name = os.path.split(image_path)
    xml_str = '<annotation>'
    """filename"""
    xml_str = xml_str + '<filename>' + file_name + '</filename>'
    """"""
    for line in text_lines:
        xml_str = xml_str + '<object>' + '<name>undefined</name><pose>Unspecified</pose><truncated>0</truncated><difficult>0</difficult><bndbox>'
        xml_str = xml_str + '<xmin>' + str(int(line['x0'])) + '</xmin>' + '<ymin>' + str(int(
            line['y0'])) + '</ymin>' + '<xmax>' + str(int(line[
                                                              'x2'])) + '</xmax>' + '	<ymax>' + str(int(
            line['y2'])) + '</ymax>   </bndbox></object>'
    xml_str = xml_str + '</annotation>'
    file_name = file_name.replace('jpg', 'xml')
    with open(save_annotation_dir + file_name, mode='w', encoding='utf8') as file:
        file.write(xml_str)


def main():
    result = load_result(result_paths)


if __name__ == '__main__':
    main()
