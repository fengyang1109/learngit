#!/usr/bin/env python
# -*- coding:utf8 -*-
# __auth__:fy
"""
双色球机选,避开已开奖号码
"""
import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)
from model import read
import random


def sum_of_values():
	tag = True
	ball_list = []
	while tag:
		sign = 1
		hislist = read.read_execl()
		while sign < 7:
			num = random.randint(1, 33)
			if num in ball_list:
				num = random.randint(1, 33)
			ball_list.append(num)
			sign += 1
		ball_list.sort()
		bull = random.randint(1, 16)
		ball_list.append(bull)
		for i in hislist.values():
			a = i[1].split(",")
			b = list(map(int, a))
			# print(b)
			if b == ball_list:
				break
			tag = False
	print(ball_list)
	return ball_list


if __name__ == '__main__':
	sum_of_values()
