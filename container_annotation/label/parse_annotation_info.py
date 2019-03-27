# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     extract_from_image
   Description :
   Author :       'li'
   date：          2018/7/29
-------------------------------------------------
   Change Activity:
                   2018/7/29:
-------------------------------------------------
"""
from utility.file_path_utility import get_all_file_from_dir
from xml.dom.minidom import parse

"""
slip label image from original image and annotation info 
"""
__author__ = 'li'
ANNOTATION_PATH = 'D:\dataset/xml/'
IMAGE_PATH = 'D:\dataset\d/'
DETECTION_LABEL_PATH = 'D:\dataset\des/'


def get_unrelated_image():
    """
    get image path that do not relate annotation path
    :return:
    """
    unrelated_image = []
    an_path = get_all_file_from_dir(ANNOTATION_PATH)
    image_path = get_all_file_from_dir(IMAGE_PATH)
    for p in image_path:
        is_related = False
        name = p.split('\\')[-1].split('.')[0]
        for a in an_path:
            if a.find(name) > 0:
                is_related = True
        if not is_related:
            unrelated_image.append(p)
    return unrelated_image


def parse_xml_file(path):
    """
    解析xml文件
    :param path:
    :return:
    """
    dom = parse(path)
    image_name = str(dom.getElementsByTagName('filename')[0].firstChild.data)
    regions = dom.getElementsByTagName('object')
    obj = {'image_name': image_name}
    reg = []
    for r in regions:  # format {label:label,p1:[h,w],p2:[h,w]}
        label = str(r.getElementsByTagName('name')[0].firstChild.data)
        x_min = str(r.getElementsByTagName('xmin')[0].firstChild.data)
        y_min = str(r.getElementsByTagName('ymin')[0].firstChild.data)
        x_max = str(r.getElementsByTagName('xmax')[0].firstChild.data)
        y_max = str(r.getElementsByTagName('ymax')[0].firstChild.data)
        reg.append({'label': label, 'p1': [y_min, x_min], 'p2': [y_max, x_max]})
    obj['region'] = reg
    return obj


def load_annotation_info():
    """
    load annotation info
    :return:
    """
    an_path = get_all_file_from_dir(ANNOTATION_PATH)
    annotation_info = []
    for path in an_path:
        parse_info = parse_xml_file(path)
        annotation_info.append(parse_info)
    return annotation_info


def write_annotation(annotation_info):
    """
    write annotation to file        
    :return:
    """
    for info in annotation_info:
        image_name = info['image_name'].replace('.jpg', '.txt')
        regions = info['region']
        if len(regions) > 0:
            with open(DETECTION_LABEL_PATH + image_name, mode='w', encoding='utf8') as file:
                for r in regions:
                    label = str(r['label'])
                    p1 = r['p1']
                    p2 = r['p2']
                    # coordinate = str(p2[1]) + ',' + str(p2[0]) + ',' \
                    #              + str(p2[1]) + ',' + str(p1[0]) + ',' \
                    #              + str(p1[1]) + ',' + str(p1[0]) + ',' \
                    #              + str(p1[1]) + ',' + str(p2[0]) + ',' + label + '\n'
                    coordinate = str(p1[1]) + ',' + str(p1[0]) + ',' \
                                 + str(p2[1]) + ',' + str(p1[0]) + ',' \
                                 + str(p2[1]) + ',' + str(p2[0]) + ',' \
                                 + str(p1[1]) + ',' + str(p2[0]) + ',' + label + '\n'
                    file.write(coordinate)


def main():
    # unrelated_image = get_unrelated_image()
    annotation_info = load_annotation_info()
    write_annotation(annotation_info)


if __name__ == '__main__':
    main()
