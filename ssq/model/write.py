#!/usr/bin/env python
# -*- coding:utf8 -*-
# auth:fy
"""
抓取数据写入execl
"""

import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)


def wri():
	from model import read
	from model import reptilian
	import xlwt

	path = r'%s\dbfile\双色球test.xls' % basedir  # 新建文件名
	path1 = r'%s\dbfile\双色球.xls' % basedir  # 原文件名
	try:
		html_in = reptilian.rep()
		execl_in = read.read_execl()
		# print(html_in)
		# print(execl_in)
		execl_in.update(html_in)  # 字典合并
		# print(execl_in)
		print('数据写入execl.............')
		file = xlwt.Workbook()
		data = file.add_sheet('Sheet 1')

		for i in range(2):
			for k, v in execl_in.items():
				data.write(k, i, execl_in[k][i])
		file.save(path)
		os.remove(path1)
		os.rename(path, path1)
		print('写入完成')
		for x, c in html_in.items():
			print(c[0], c[1])
	except (TypeError, PermissionError) as e:
		print(e.message)


if __name__ == '__main__':
	wri()
