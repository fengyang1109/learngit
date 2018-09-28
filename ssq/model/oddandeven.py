#!/usr/bin/env python
# -*- coding:utf8 -*-
# __auth__:fy
"""
生成奇偶随机数
"""

import os
import sys
import random

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

from model import ipt

odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]
even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
def oad():
	a = ipt.iput()
	oddsecond = int(a['oddnum'])
	evensecond = int(a['evennum'])
	oddlist = random.sample(odd, k=oddsecond)
	evenlist = random.sample(even, k=evensecond)
	redlist = oddlist + evenlist
	redlist.sort()
	print(redlist)
	return redlist


if __name__ == '__main__':
	print(oad())
