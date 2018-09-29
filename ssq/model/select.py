#!/usr/bin/env python
# -*- coding:utf8 -*-
# auth:fy
"""
自选用户输入
"""
import re


def ball_select():
	ball_list = []
	num = 1
	N = True
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
	return ball_list


if __name__ == '__main__':
	print(ball_select())
