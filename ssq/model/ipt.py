#!/usr/bin/env python
# -*- coding:utf8 -*-
# __auth__:fy
"""
输入模块
"""


def iput():
	ar = {}
	tag = True
	while tag:
		userodd = input('请输入奇值: ').strip()
		usereven = input('请输入偶值: ').strip()
		a = int(usereven) + int(userodd)
		if userodd.isdigit() and usereven.isdigit() and a == 6:
			ar['oddnum'] = userodd
			ar['evennum'] = usereven
			tag = False
		else:
			print('输入错误')
	return ar


if __name__ == '__main__':
	iput()
