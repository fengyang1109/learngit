#!/usr/bin/env python
# -*- coding:utf8 -*-
# auth:fy
"""
自选用户输入
"""
import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)


import re
from model import read

def ball_select():
	a = read.read_execl()
	ball_list = []
	num = 1
	N = True
	result = True
	while N:
		while num < 7:
			user_redball = input("请输入第%s红球>>: " % num).strip()
			ze = re.match(r"^[1-9]{1,2}$", user_redball)
			if user_redball.isdigit() and ze:
				numredball = int(user_redball)
				if numredball < 34:
					if numredball not in ball_list:
						ball_list.append(numredball)
						num += 1
					else:
						print("红球以选.")
				else:
					print("红球是1-33,输入错误.")
			else:
				print('输入错误,请输入1-33整数.')
		ball_list.sort()
		# print(ball_list)
		while N:
			user_blueball = input("请输入篮球>>: ").strip()
			ze = re.match(r"^[1-9]{1,2}$", user_blueball)
			if user_blueball.isdigit() and ze:
				numblueball = int(user_blueball)
				if numblueball < 17:
					ball_list.append(numblueball)
					N = False
				else:
					print("篮球是1-16,输入错误.")
					continue
			else:
				print('输入错误,请输入1-16的数字.')
				continue
	for k, v in a.items():
		ball_list_test = v[1].split(',')
		ball_list_test = list(map(int, ball_list_test))
		# print(ball_list_test)
		if ball_list == ball_list_test:
			print('!!!!!!!!!!!!!!组合以在奖池中出现过!!!!!!!!!!!!!!!')
			result = False

	if result:
		print('#####################组合未在已开奖池中出现########################')
	return ball_list


if __name__ == '__main__':
	print(ball_select())
