#!/usr/bin/env python
# -*- coding:utf8 -*-
# __auth__:fy
"""
双色球机选
"""
import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)
import random


def sum_of_values():
	ball_list = []
	sign = 1
	while sign < 7:
		num = random.randint(1, 33)
		if num in ball_list:
			num = random.randint(1, 33)
		ball_list.append(num)
		sign += 1
	ball_list.sort()
	bull = random.randint(1, 16)
	ball_list.append(bull)
	print(ball_list)
	return ball_list


if __name__ == '__main__':
	sum_of_values()
