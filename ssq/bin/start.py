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
write.wri()
tag = 0
while tag == 0:
	userip = input('1: 自选\t2: 机选\t3: 退出\n#> ').strip()
	if userip.isdigit() == 1:
		contrast.con()
	elif userip.isdigit() == 2:
		oddandeven.oad()
	elif userip.isdigit() == 3:
		tag = 1
	else:
		print("输入错误.")

