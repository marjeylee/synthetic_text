"""
文字处理相关模块,统一以utf8模式进行编码
"""
# -*- coding: utf-8 -*-

import re


def is_chinese_character(ch):
    """
    判断该字符是否是汉字,可以使字或者字符串
    :param ch:
    :return:
    """
    pattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = pattern.search(ch)
    if match:
        return True
    else:
        return False


def remove_bracket(sentence):
    """
    移除括号
    :param sentence:
    :return:
    """
    re_str = r'（[\s\S\w\W]*?）'
    pattern = re.compile(re_str)
    match_obj = pattern.findall(sentence)
    for match in match_obj:
        sentence = sentence.replace(match, '')
    return sentence
