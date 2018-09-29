#!/usr/bin/env python
# -*- coding:utf8 -*-
# auth:fy
"""
输入与历史记录比较
"""
import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)


def con():
	from model import read
	from model import select
	a = read.read_execl()
	# print(a)
	b = select.ball_select()
	# print(b)
	result = True
	for k, v in a.items():
		ball_list = v[1].split(',')
		# print(ball_list)

		if b == ball_list:
			print('!!!!!!!!!!!!!!组合以在奖池中出现过!!!!!!!!!!!!!!!')
			result = False

	if result:
		print('#####################组合未在已开奖池中出现########################')


if __name__ == '__main__':
	con()
