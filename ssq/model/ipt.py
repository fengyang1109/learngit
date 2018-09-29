#!/usr/bin/env python
# -*- coding:utf8 -*-
# __auth__:fy
"""
机选输入模块
"""
import re

def iput():
	ar = {}
	tag = True
	while tag:

		userodd = input('请输入奇值: ').strip()
		usereven = input('请输入偶值: ').strip()
		oe = re.match(r"^[0-6]{1}", userodd)
		en = re.match(r"^[0-6]{1}", usereven)
		a = int(usereven) + int(userodd)
		if oe and en and a == 6:
			ar['oddnum'] = userodd
			ar['evennum'] = usereven
			tag = False
		else:
			print('输入错误,输入1-6整数,合为6.')
	return ar


if __name__ == '__main__':
	iput()
