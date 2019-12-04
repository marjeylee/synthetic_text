#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 11:30
# @Author  : lr
# @Site    : 
# @File    : statistic_data.py
# @Software: PyCharm
TXT_PATH = 'G:/dataset/data_train.txt'


def _main():
    with open(TXT_PATH, mode='r') as file:
        a = set()
        lines = file.readlines()
        for index, line in enumerate(lines):
            if index % 1000 == 0:
                print(index)
            rows = line.split(' ')
            key = rows[0]
            value = ''
            for row in rows[1:]:
                a.add(int(row))
                value = value + str(row).replace('/n', '') + '_'
            value = value[:-1]
        print(a)


if __name__ == '__main__':
    _main()
