#!/usr/bin/env python
# -*- coding:utf8 -*-
# __auth__:fy
"""
红球大小和值
"""
import random
def sum_of_values():
	ball_list = []
	sign = 1
	while sign < 7:
		num = random.randint(1, 32)
		if num in ball_list:
			num = random.randint(1, 32)

		ball_list.append(num)
		sign += 1
	ball_list.sort()
	print(ball_list)
	return ball_list

if __name__ == '__main__':
	sum_of_values()