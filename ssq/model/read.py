#!/usr/bin/env python
# -*- coding:utf8 -*-
# auth:fy
"""
读取execl
"""
import xlrd
import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)
def read_execl():
    path = r'%s\dbfile\双色球.xls' % basedir
    file = xlrd.open_workbook(path)
    # print(book.sheet_names())
    data = file.sheets()[0]
    # print(data)
    row_num = data.nrows
    # col_num = data.ncols
    # print(row_num, col_num)
    data_list = {}
    for i in range(row_num):
        # print(i)
        d = data.row_values(i)
        # print(d)
        i += 1
        data_list[i] = d
    return data_list


if __name__ == '__main__':
    print(read_execl())
    # read_execl()