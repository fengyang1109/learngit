#!/usr/bin/env python
# -*- coding:utf8 -*-
# auth:fy

import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

from model import contrast
from model import write
from model import oddandeven
from model import sum
write.wri()
tag = 0
while tag == 0:
	userip = input('1: 自选\t2: 机选\t3: 退出\n#>: ').strip()
	if userip.isdigit() and userip == '1':
		contrast.con()
	elif userip.isdigit() and userip == '2':
		while tag == 0:
			urip = input('1: 随机选择\t2: 模式选择\n#>: ').strip()
			if urip.isdigit() and urip == '1':
				sum.sum_of_values()
				tag = 1
			elif urip.isdigit() and urip == '2':
				oddandeven.oad()
				tag = 1
			else:
				print("输入错误.")
	elif userip.isdigit() and userip == '3':
		tag = 1
	else:
		print("输入错误.")

